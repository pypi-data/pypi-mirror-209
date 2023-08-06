import pandas as pd
from dataclasses import dataclass


@dataclass
class BalanceSheet:
    period: pd.Timestamp
    accounts: pd.Series
    balances: pd.Series
    agregations: pd.Series = None

    def __post_init__(self):
        df = self.df.groupby(['accounts', 'agregations']).sum().reset_index()
        print(df.head())
        self.accounts = df['accounts']
        self.balances = df[self.period]
        self.agregations = df[self.agregations if self.agregations is not None else self.accounts]

        self.check_balanced()

    def check_balanced(self):
        assert self.balances.sum() < 0.01

    def post(self, value, credit, debit):
        if len(self.accounts[self.accounts == credit]) != 1:
            raise ValueError(f'\'credit\' filter has not produced single account, produced: {self.accounts[self.accounts == credit]}')

        if len(self.accounts[self.accounts == debit]) != 1:
            raise ValueError('\'dedit\' filter has not produced single account')

        self.balances.loc[self.accounts == credit] -= value
        self.balances.loc[self.accounts == debit] += value

        self.check_balanced()

    @property
    def df(self):
        return pd.DataFrame({'accounts': self.accounts, 'agregations': self.agregations, self.period: self.balances})

    def __sub__(self, other):
        return BalanceSheet(
            period=self.period, accounts=self.accounts,
            balances=self.df.merge(other.df, how='left').assign(balance=lambda x: x[self.period] - x[other.period])['balance']
        )

# Use pandas pivot_table
