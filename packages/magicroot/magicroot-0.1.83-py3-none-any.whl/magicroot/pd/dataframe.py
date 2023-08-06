import pandas as pd


class FormatMethods:

    def __init__(self, df):
        self._df = df

    def with_func(self, columns, func):
        """
        Tranforms the given columns based on the given function
        :param df: Table to be transformed
        :param columns: columns to be transformed
        :param func: function that receives the dataframe and the name of the column to be formated
        :return:
        """
        columns = columns if columns is not None else self._df.columns
        for column in columns:
            if column in self._df.columns:
                self._df = self._df.assign(**{column: func(self._df, column)})
        return self._df

    def as_code(self, columns=None, fillna='0'):
        """
        Tranforms the given columns into set lenght codes (ex. '001')
        :param df: Table to be transformed
        :param columns: dict
        columns to be transformed as keys, lenght of expected results as values
        :param lenght: columns to be transformed
        :return:
        columns = columns if columns is not None else self._df.columns
        for column, lenght in columns.items():
            self._df = self.with_func([column], lambda x, col: x[col].fillna(fillna).astype(str).str.zfill(lenght))
        return self._df
        """
        columns = columns if columns is not None else self._df.columns
        for column, lenght in columns.items():
            self._df = self.with_func([column], lambda x, col: x[col].fillna(fillna).astype(str).str.zfill(lenght))
        return self._df


class Formattable:
    def __get__(self, instance, owner):
        return FormatMethods(instance)


class BaseDataFrame:

    def __init__(self, *args, **kwargs):
        self._df = pd.DataFrame(*args, **kwargs)

    def __getattr__(self, attr):
        return getattr(self._df, attr)

    def __getitem__(self, *args, **kwargs):
        return BaseDataFrame(self._df.__getitem__(*args, **kwargs))

    format = Formattable()


class LoggedMethods(BaseDataFrame):
    def melt(self):
        # print('hello world')
        return self._df.melt()


class DataFrame(LoggedMethods):
    def prove_df(self):
        return 'this is an improved df'

"""

"""


