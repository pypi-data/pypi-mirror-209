from lib2to3.pgen2.pgen import DFAState

from ..df.dt import shift as date_shift
import pandas as pd
from dataclasses import dataclass
from .. import df as mrdf
from typing import ClassVar
from ..errors import DiscountValueError, DiscountTypeError


def forward(quotes, forward, col_rate='QUOTE_RT', col_mat='MATURITY_DT'):
    if isinstance(forward, int):
        quotes['FORWARD'] = forward

    fwr_quotes = quotes.merge(quotes.rename(columns={col_rate: 'QUOTE_FWR_DEN'}).assign(
        MATURITY_DT=lambda x: x[col_mat] - quotes['FORWARD']
    ), how='left')
    quotes = fwr_quotes.merge(quotes.rename(columns={col_rate: 'QUOTE_FWR_NUM'}).assign(
        MATURITY_DT=lambda x: x[col_mat] - quotes['FORWARD'] + 1
    ), how='left')

    quotes[col_rate] = \
        (
                (1 + quotes['QUOTE_FWR_NUM']) ** (quotes['FORWARD'] + 1) /
                (1 + quotes['QUOTE_FWR_DEN']) ** quotes['FORWARD']
        ).fillna((1 + quotes['QUOTE_FWR_NUM']) ** (quotes['FORWARD'] + 1)) - 1
    quotes = quotes.drop(columns=['QUOTE_FWR_DEN', 'QUOTE_FWR_NUM'])
    quotes = quotes.sort_values(
        [col for col in quotes.columns if col not in [col_mat, 'FORWARD', col_rate]] + [col_mat]
    ).fillna(method='ffill')
    return quotes


def f_factor(with_rate, with_maturity):
    return (1 + with_rate) ** with_maturity


def factor_formula(with_rate, with_maturity):
    return 1 / (1 + with_rate).pow(with_maturity)


def maturity(maturity_dt, ref_dt, divide_days_by=365):
    return (maturity_dt - ref_dt).dt.days / divide_days_by


def forward_of_order(s, order=1, interpolation=None):
    s.index = s.index.astype(float)
    s_n_minus_k = mrdf.interpolate.series(s, in_index=(s.index+order).to_series(), method=interpolation)
    num = (1 + s) ** s.index
    num.index = s_n_minus_k.index
    return (num / (1 + s_n_minus_k) ** (s.index - order)) ** (1 / order) - 1


@dataclass
class Curve:
    date: pd.Timestamp = None
    rate: pd.Series = None
    maturity: pd.Series = None
    id: str = None
    fwrd: float = None

    all_dates: ClassVar[dict] = None

    def __post_init__(self, *args, **kwargs):
        if self.rate is not None:
            self.rate = self.rate.astype(float)
            self.id = self.id if self.id is not None else 'unnamed'
            if self.maturity is None:
                df = self.rate.to_frame('Date').assign(Maturity=mrdf.gen.counting_col())
                self.maturity = date_shift(self.date, df.Maturity, 'Y')
            if len(self.rate) != len(self.maturity):
                raise ValueError(
                    'When defining a discount curve the number of rates provided must be equal to'
                    ' the number of maturities provided'
                )
            self.maturity = pd.to_datetime(self.maturity)
            self.all_dates = self.all_dates if self.all_dates is not None else {}
            self.all_dates[(self.id, self.date, self.fwrd)] = self

    @classmethod
    def load(cls, ids, rates, dates, maturities=None):
        """
        Loads quotes from dataframe to magicroot.fs.disc.Curve.



        """
        ids, rates, dates, maturities = mrdf.gen.coupled_series(ids, rates, dates, maturities)
        df = pd.concat([ids, rates, dates, maturities], axis=1, keys=['ids', 'rates', 'dates', 'maturities'])
        cls.all_dates = cls.all_dates if cls.all_dates is not None else {}
        for quote_id in df.ids.drop_duplicates():
            for date in df.dates.drop_duplicates():
                current = df[(df.ids == quote_id) & (df.dates == date)]
                if len(current) > 0:
                    if current.maturities.notnull().all():
                        Curve(date=date, maturity=current.maturities, rate=current.rates, id=quote_id)
                    Curve(date=date, rate=current.rates, id=quote_id)
        return cls.all_dates

    def to_frame(self, maturity_dt_col='maturity', quote_rate_col='rate', quote_date_col='date'):
        df = pd.DataFrame({maturity_dt_col: self.maturity, quote_rate_col: self.rate})
        df[quote_date_col] = self.date
        return df[[quote_date_col, maturity_dt_col, quote_rate_col]].copy()

    def rates_with_maturity_index(self):
        rates = self.rate.copy()
        rates.index = self.maturity
        return rates

    def get_rates(self, for_maturities=None, interpolation=None):
        mrdf.format.guarantee(
            dates=for_maturities.rename('for_maturities'), error=DiscountTypeError)
        
        index = for_maturities.index
        for_maturities = for_maturities.reset_index(drop=True)
 
        s = mrdf.tec.interpolate(
            self.rates_with_maturity_index(), in_index=for_maturities, method=interpolation
        )

        df = for_maturities.to_frame('maturity').merge(
            s.to_frame('rate').assign(maturity=lambda x: x.index).reset_index(drop=True), how='left', validate='m:1'
        )
        df.index = index
        return df['rate']

    def discount_to_date(self, cashflows, from_date, with_detail=False):
        mrdf.format.guarantee(
            dates=from_date.rename('from_date'), error=DiscountTypeError)
        
        cashflows, from_date = mrdf.gen.coupled_series(cashflows, from_date)

        ic = self.get_rates(for_maturities=from_date, interpolation=None)
        print('was able to get rates')
        return cashflows * factor_formula(ic, (from_date - self.date).dt.days / 365) - cashflows

    def shift(self, by):
        return self.to_frame().maturity.assign(maturity=lambda x: x + by).merge(self.to_frame())

    def forward(self, n=None, to_date=None, order=1):
        if n and to_date:
            raise ValueError('Cannot provide both \'n\' and \'to_date\'')
        order = n if n else (to_date - self.maturity.min()).days / 365
        rates = forward_of_order(self.rate.reset_index(drop=True), order=order)
        maturity = self.maturity.copy()
        maturity.index = rates.index
        return Curve(
            date=self.maturity.min(),
            maturity=maturity, rate=rates, fwrd=order, id=self.id
        )

    def some_shift(self, to_date):
        return (to_date - self.maturity.min()).days / 365

    @classmethod
    def get_curve(cls, to_date, with_quote, with_date=None):
        df = mrdf.gen.dataframe_from_series(
            to_date=to_date, with_date=with_date, with_quote=with_quote
        )
        dic = df.drop_duplicates().merge(cls.loaded(), how='cross')[
            lambda x: (x['to_date'] >= x['Date']) &
                      (x['with_quote'].isnull() | (x['with_quote'] == x['Id'])) &
                      (x['with_date'].isnull() | (x['with_date'] == x['Date']))
        ].assign(Curve=lambda x: tuple(zip(x.Id, x.Date, x.forward))).sort_values(
            ['Date', 'to_date', 'with_date', 'with_quote'], ascending=False
        )
        x = dic[['to_date', 'with_date', 'with_quote', 'Curve']].groupby(
            ['to_date', 'with_date', 'with_quote'], dropna=False
        ).nth(0).reset_index()
        df = df.merge(x, how='left', validate='m:1')

        # weed out errors
        with_out_curve = df[df['Curve'].isnull()]
        if len(with_out_curve):
            raise DiscountValueError(
                f'Unable to find Curves for some dates: \n'
                ' {with_out_curve.sample(min(len(with_out_curve), 10))}')
        return df['Curve']
    
    @classmethod
    def discount(cls, cashflows, from_date, to_date, with_quote, with_dates=None):
        df = mrdf.gen.dataframe_from_series(
            cashflows=cashflows, from_date=from_date, to_date=to_date, 
            with_quote=with_quote, with_date=with_dates
        )
        df = df.reset_index(drop=True)
        df['curve'] = cls.get_curve(
            to_date=df['to_date'], with_date=df['with_date'].astype('datetime64[ns]'), 
            with_quote=df['with_quote']
        )
        print(mrdf.format.compared(df=df))
        print(df.head())
        df['disc'] = df.groupby([
            'to_date', 'with_date', 'with_quote'
        ], group_keys=True, dropna=False).apply(
            lambda x: cls.all_dates[x['curve'].iloc[0]].discount_to_date(
                cashflows=x['cashflows'], from_date=x['from_date']
            )
        ).reset_index([0, 1, 2], drop=True)

        df.index = cashflows.index

        return df['disc']

    def interpolated(self, for_maturities, with_detail=False):
        self_frame = self.to_frame()
        df = pd.DataFrame({'maturity': for_maturities})
        all_maturities = pd.concat([self_frame.maturity, df['maturity']]).drop_duplicates().sort_values()
        quotes = mrdf.merge.tagged(
            all_maturities.to_frame(), self_frame, how='left', on='maturity', validate='m:1',
            left_tag='Interpolated', right_tag='Original', both_tag='Original', tag_col='METHOD'
        )
        quotes = quotes.set_index('maturity')
        quotes['rate'] = quotes['rate'].interpolate(method='time', limit_area='inside').fillna(0)

        quotes = quotes.reset_index().assign(
            date=self.date,
            maturity_days=lambda x: maturity(x['maturity'], x['date'], 1),
            maturity=lambda x: maturity(x['maturity'], x['date'])
        )
        if with_detail:
            return quotes
        return quotes.rate

    def forward_int(self, value):
        numerator = f_factor(self.rate.shift(-1 * value + 1), value + 1)
        denominator = f_factor(self.rate.shift(-1 * value), value)

        rate = (numerator / denominator).fillna(numerator) - 1
        return Curve(date=date_shift(self.date, value, 'Y'), maturity=self.maturity, rate=rate)

    @classmethod
    def loaded(cls, for_dates=None, for_ids=None):
        df = pd.DataFrame.from_records(list(cls.all_dates.keys()), columns=['Id', 'Date', 'forward'])
        for_ids = for_ids if for_ids is not None else df['Id'].drop_duplicates()
        for_dates = for_dates if for_dates is not None else df['Date'].drop_duplicates()
        return df[df['Id'].isin(for_ids) & df['Date'].isin(for_dates)]

    @classmethod
    def has_loaded(cls, for_dates=None, for_ids=None):
        return len(cls.loaded(for_dates=for_dates, for_ids=for_ids)) > 0

    def plot(self):
        df = self.to_frame()[['maturity', 'rate']]
        df.plot(x='maturity', y='rate', kind='scatter')

    def get_rates_for_existing(self, for_maturities=None):
        if for_maturities is None:
            return self.rate
        return pd.DataFrame({'MATURITY_DT': for_maturities}).merge(self.to_frame(), how='left')['QUOTE_RT']

    def get_act_act_maturities(self, for_maturities=None):
        for_maturities = for_maturities if for_maturities else self.maturity
        return (date_shift(self.date, for_maturities, 'Y') - self.date).days

    def factor(self, maturities):
        return factor_formula(self.get_rates(maturities), self.get_act_act_maturities(maturities))

    def gen_maturities_frame(
            self,
            maturities, ref_date,
            maturity_years_col='MATURITY_YEARS',
            maturity_act_act_col='MATURITY_ACT_ACT',
            maturity_days_col='MATURITY_DAYS',
            maturity_dt_col='MATURITY_DT',
            quote_rate_col='QUOTE_RT', quote_date_col='QUOTE_DT'
    ):
        df = pd.DataFrame({maturity_dt_col: maturities, quote_date_col: ref_date})
        df[quote_date_col] = self.date
        df[maturity_dt_col] = date_shift(df[quote_date_col], df[maturity_years_col].astype(int), 'Y')
        df[maturity_days_col] = df[maturity_dt_col] - df[quote_date_col]
        df[maturity_act_act_col] = df[maturity_days_col].dt.days / 365
        return df[[
            quote_date_col, maturity_dt_col, maturity_days_col, maturity_years_col, maturity_act_act_col, quote_rate_col
        ]]

    @classmethod
    def __getitem__(cls, item):
        try:
            return cls.all_dates[item]
        except KeyError:
            idq, dt, n = item[0], item[1], item[2]
            return cls.all_dates[(idq, dt, None)].forward(to_date=dt + pd.to_timedelta(n*365, unit='D'))

    def __repr__(self):
        return self.to_frame().__repr__()

    @staticmethod
    def curves_dic_from_dataframe(df, by, quote_date_col, quote_rate_col, maturity_col=None):
        groups = df.groupby(by)
        curves = {}
        for curve_name in groups.groups:
            group = groups.get_group(curve_name)
            date = group[quote_date_col].unique()
            if len(date) != 1:
                raise ValueError('More than one quote date per curve')
            if maturity_col is not None:
                curves[curve_name] = Curve(date=pd.to_datetime(date[0]), maturity=group[maturity_col], rate=group[quote_rate_col])
            curves[curve_name] = Curve(date=pd.to_datetime(date[0]), rate=group[quote_rate_col].reset_index(drop=True))

        return curves





