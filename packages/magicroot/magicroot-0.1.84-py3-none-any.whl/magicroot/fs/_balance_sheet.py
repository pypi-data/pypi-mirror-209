import pandas as pd
from dataclasses import dataclass
from .. import df as mr
import regex as re
from ..time import function as time_function

@dataclass
class BalanceSheet:
    period: pd.Timestamp
    accounts: pd.Series
    balances: pd.Series
    others: pd.DataFrame = None
    descriptions: pd.DataFrame = None
    dimensions: pd.DataFrame = None
    name: str = None

    def __post_init__(self):
        self.accounts, self.balances = mr.gen.coupled_series(self.accounts.astype(str), self.balances)
        self.name = self.name if self.name is not None else self.period
        self.split_descriptions_from_dimentions()
        # self.group()
        self.balanced_on_acc()

    def split_descriptions_from_dimentions(self):
        bl = self.others.copy()
        bl['accounts'] = self.accounts
        df = bl.groupby('accounts').nunique()
        x = pd.DataFrame(df.max(), columns=['value'])
        self.descriptions = bl[x[x['value'] == 1].index.to_list()]
        self.dimensions = bl[[col for col in x.index if col not in x[x['value'] == 1].index.to_list()]]

    def balance(self):
        assert self.balances.sum() < 0.01

    def balanced_on_acc(self, acc='__control__'):
        self[acc] = -self.balances[self.accounts != acc].sum()

    def to_frame_agg(self):
        return pd.concat([
            self.accounts.to_frame('accounts'),
            self.descriptions,
            self.balances.to_frame(self.name)
        ], axis=1).groupby(['accounts'] + self.descriptions.columns.to_list(), dropna=False).sum()

    def to_frame_level(self, level=2):
        return self.to_frame_agg().reset_index()[['accounts', self.name]].assign(
            accounts=lambda x: x['accounts'].str[:level]).groupby('accounts').sum()

    def to_frame(self, pat=None):
        bl = pd.concat([
            self.accounts.to_frame('accounts'),
            self.descriptions,
            self.dimensions,
            self.balances.to_frame(self.name)
        ], axis=1)
        bl = bl[self.pattern_filter(pat)]

        return bl.set_index(['accounts'] + self.descriptions.columns.to_list() + self.dimensions.columns.to_list())

    def pattern_filter(self, pat=None):
        if pat is None:
            return self.accounts.apply(lambda x: True)
        return self.accounts.apply(lambda x: bool(re.fullmatch(pat, x)))

    def add_descriptions_by_patterns(self, patterns, descriptions):
        self.descriptions['pat'] = ''
        for pat in patterns.drop_duplicates().astype(str):
            self.descriptions = self.descriptions.assign(
                pat=self.descriptions['pat'].mask(self.accounts.astype(str).apply(lambda x: bool(re.fullmatch(pat, x))), pat)
            )
        self.descriptions = self.descriptions.merge(
            pd.concat([descriptions, patterns.to_frame('pat')], axis=1).groupby('pat', dropna=False).first().reset_index(),
            how='left', validate='m:1'
        ).drop(columns='pat')

    @property
    def frame(self):
        return pd.DataFrame({'accounts': self.accounts, self.period: self.balances})

    def from_frame(self, df):
        self.accounts = df.accounts
        self.balances = df[self.period]

    def agg(self, accounts_level=2):
        return self.frame.assign(
            accounts=lambda x: x['accounts'].str[:accounts_level]
        ).groupby('accounts').sum().reset_index()

    def group(self):
        df = self.frame.groupby(['accounts']).sum().reset_index()
        self.accounts = df['accounts']
        self.balances = df[self.period]

    def __getitem__(self, item):
        bl = self.to_frame(pat=item).reset_index()
        return BalanceSheet(
            period=self.period, accounts=bl.accounts, name=self.name,
            balances=bl[self.name], others=bl[mr.cols.without(bl, [self.name, 'accounts'])]
        )

    def __setitem__(self, key, value):
        fltr = self.pattern_filter(key)
        self.balances.loc[fltr] = value
        print(f'len of {key} is {len(self.balances.loc[fltr])}')
        if len(self.balances.loc[fltr]) == 0:
            self.accounts.loc[len(self.accounts)] = key
            self.balances.loc[len(self.balances)] = value

    def __sub__(self, other):
        joined = self.to_frame().reset_index().merge(other.to_frame().reset_index(), how='outer').assign(
                balance=lambda x: x[self.name].fillna(0) - x[other.name].fillna(0)
            )
        return BalanceSheet(
            period=self.period, accounts=joined.accounts,
            balances=joined['balance'], name=str(self.name) + ' - ' + str(other.name),
            others=joined[mr.cols.without(joined, [self.name, 'accounts'])]
        )

    def copy(self, name=None):
        return BalanceSheet(
            period=self.period, accounts=self.accounts, balances=self.balances, others=self.others,
            name=name or self.name
        )

    def open(self, account, name):
        bl = self.copy()
        bl[account] = 0
        return bl

    def close(self, account, beneficiary, name):
        bl = self.copy()
        value = bl[account].sum()
        return bl.post(bl[account], credit=account, debit=beneficiary)

    def post(self, value, credit, debit):
        if len(self.accounts[self.accounts == credit]) != 1 and len(self.accounts[self.accounts == debit]) != 1:
            raise ValueError(f'\'credit\' and \'dedit\' filter has not produced single account')

        self.balances.loc[self.accounts == credit] -= value
        self.balances.loc[self.accounts == debit] += value

        self.check_balanced()

# Use pandas pivot_table
