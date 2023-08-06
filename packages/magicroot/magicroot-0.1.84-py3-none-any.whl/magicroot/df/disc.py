import pandas as pd
from dataclasses import dataclass
from . import compute
from .dt import shift as date_shift
import logging
from datetime import timedelta


log = logging.getLogger(__name__)


def component(
        cashflow, from_date, to_date, with_rate
):
    """
    Discounts cashflows
    :param df: Dataframe
        :column cashflow_columns: column(s) should be in the table
        :column disc_rate_column: column(s) should be in the table
    base to compute

    :param cashflow_columns: list
    containing columns with cashflows to discount

    :param disc_rate_column: str
    Column with the discount rate

    :param prefix: str, default 'disc_'
    column with the prefix to add to the column names with the discounted cashflows

    :param suffix: str, default ''
    column with the suffix to add to the column names with the discounted cashflows

    :return: Dataframe
        :column previous: all column(s) previously in the table
        :column prefix + cashflow_columns: computed columns
    result table
    """
    return cashflows(cashflow=cashflow, with_rate=with_rate, from_date=from_date, to_date=to_date) - cashflow


def cashflows(
        cashflow, from_date, to_date, with_rate
):
    """
    Discounts cashflows
    :param df: Dataframe
        :column cashflow_columns: column(s) should be in the table
        :column disc_rate_column: column(s) should be in the table
    base to compute

    :param cashflow_columns: list
    containing columns with cashflows to discount

    :param disc_rate_column: str
    Column with the discount rate

    :param prefix: str, default 'disc_'
    column with the prefix to add to the column names with the discounted cashflows

    :param suffix: str, default ''
    column with the suffix to add to the column names with the discounted cashflows

    :return: Dataframe
        :column previous: all column(s) previously in the table
        :column prefix + cashflow_columns: computed columns
    result table
    """
    return cashflow * factor(with_rate=with_rate, with_maturity=from_date - to_date)


def maturity(begin_date, end_date):
    """
    Computes maturity
    :param begin_date: str
    Series with the begin date

    :param end_date: str
    Series with the end date

    :return: func to be applied to a Dataframe
    """
    return (end_date - begin_date).where(end_date > begin_date, timedelta(days=0))


def factor(with_rate, with_maturity, days_in_year=365):
    """
    Computes discount rate

    :param with_rate: str
    Series with the spot rate

    :param with_maturity: str
    Series with the maturity

    :param days_in_year: int
    constant with the days in the year

    :return: func to be applied to a Dataframe
    """
    return 1 / (1 + with_rate).pow(with_maturity.dt.days / days_in_year)


def new_factor(from_date, to_date, with_rate, of_date, of_maturity, days_in_year=365):
    """
    Computes discount rate

    :param with_rate: str
    Series with the spot rate

    :param with_maturity: str
    Series with the maturity

    :param days_in_year: int
    constant with the days in the year

    :return: func to be applied to a Dataframe
    """
    with_rate = forward((from_date - of_date).days / days_in_year, with_rate)

    return 1 / f_factor(with_rate, (from_date - to_date).days / days_in_year)


def forward(value, of_rate):
    if isinstance(value, int):
        value = pd.Series([value]).repeat(len(of_rate))

    value = value.astype(int)
    numerator = f_factor(of_rate.shift(-1 * value + 1), value + 1)
    denominator = f_factor(of_rate.shift(-1 * value), value)

    return (numerator / denominator).fillna(numerator) - 1


def f_factor(with_rate, with_maturity):
    return (1 + with_rate) ** with_maturity


def new_factor(from_date, to_date, with_curve, days_in_year=365):
    """
    Computes discount rate

    :param with_rate: str
    Series with the spot rate

    :param with_maturity: str
    Series with the maturity

    :param days_in_year: int
    constant with the days in the year

    :return: func to be applied to a Dataframe
    """
    with_rate = forward((from_date - with_curve.date).days / days_in_year, with_curve.rate)

    return 1 / f_factor(with_rate, (from_date - to_date).days / days_in_year)


@dataclass
class Curve:
    date: pd.Timestamp
    maturity: pd.Series
    rate: pd.Series

    def __post_init__(self, *args, **kwargs):
        if len(self.rate) != len(self.maturity):
            raise ValueError(
                'When defining a discount curve the number of rates provided must be equal to'
                ' the number of maturities provided'
            )
        self.rate = self.rate.astype(float)
        self.maturity = self.maturity.astype(float)

    def discount(self, cashflows, to_date=None, from_date=None):
        to_date = to_date if to_date is not None else self.date
        if (to_date < self.date).all():
            raise ValueError(f'Cannot discount {to_date=} with curve of {self.date}')
        if (to_date > self.date).all():
            if (to_date.dt.month == self.date.month).all() and (to_date.dt.day == self.date.day).all():
                return self.forward((to_date.dt.year - self.date.year).max()).discount(
                    cashflows=cashflows, to_date=to_date, from_date=from_date)
            else:
                raise ValueError(f'Cannot discount please check that {to_date=} and {self.date=} satisfy '
                                 f'{(to_date.dt.month==self.date.month).all()=} and '
                                 f'{(to_date.dt.month==self.date.month).all()=}')
        if (from_date < to_date).all():
            print(f'{from_date=}')
            print(f'{to_date=}')
            raise NotImplementedError
        if (from_date == to_date).all():
            return cashflows

        # to_date == self.date and from_date > to_date
        return cashflows * self.factor(from_date)

    def factor(self, maturities):
        return self.factor_formula(self.get_rates(maturities), self.get_act_act_maturities(maturities))

    @staticmethod
    def factor_formula(with_rate, with_maturity):
        return 1 / (1 + with_rate).pow(with_maturity)

    def get_rates(self, for_maturities=None):
        if for_maturities is None:
            return self.rate
        df = self.to_dataframe()
        return pd.DataFrame({'MATURITY_DT': for_maturities}).merge(self.to_dataframe(), how='left')['QUOTE_RT']

    def get_act_act_maturities(self, for_maturities=None):
        for_maturities = for_maturities if for_maturities else self.maturity
        return (date_shift(self.date, for_maturities, 'Y') - self.date).days

    @staticmethod
    def curves_dic_from_dataframe(df, by, quote_date_col, maturity_col, quote_rate_col):
        groups = df.groupby(by)
        curves = {}
        for curve_name in groups.groups:
            group = groups.get_group(curve_name)
            date = group[quote_date_col].unique()
            if len(date) != 1:
                raise ValueError('More than one quote date per curve')
            curves[curve_name] = Curve(date=pd.to_datetime(date[0]), maturity=group[maturity_col], rate=group[quote_rate_col])

        return curves

    def to_dataframe(
            self,
            maturity_years_col='MATURITY_YEARS',
            maturity_act_act_col='MATURITY_ACT_ACT',
            maturity_days_col='MATURITY_DAYS',
            maturity_dt_col='MATURITY_DT',
            quote_rate_col='QUOTE_RT', quote_date_col='QUOTE_DT'
    ):
        df = pd.DataFrame({
            maturity_years_col: self.maturity,
            quote_rate_col: self.rate
        })
        df[quote_date_col] = self.date
        df[maturity_dt_col] = date_shift(df[quote_date_col], df[maturity_years_col].astype(int), 'Y')
        df[maturity_days_col] = df[maturity_dt_col] - df[quote_date_col]
        df[maturity_act_act_col] = df[maturity_days_col].dt.days / 365
        return df[[
            quote_date_col, maturity_dt_col, maturity_days_col, maturity_years_col, maturity_act_act_col, quote_rate_col
        ]]

    def shift(self, by):
        return self.to_dataframe()[['MATURITY_DT']].assign(MATURITY_DT=lambda x: x + by).merge(self.to_dataframe())

    def forward(self, value):
        numerator = f_factor(self.rate.shift(-1 * value + 1), value + 1)
        denominator = f_factor(self.rate.shift(-1 * value), value)

        rate = (numerator / denominator).fillna(numerator) - 1
        print(value)
        return Curve(date=date_shift(self.date, value, 'Y'), maturity=self.maturity, rate=rate)


