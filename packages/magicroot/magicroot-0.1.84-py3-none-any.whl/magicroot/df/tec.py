from . import format
from . import cols, add
import tabulate
import pandas as pd


def propagate(on, by, inplace=False, validate=None, **kwargs):
    """
    Extends Dataframe with computation
    """
    df = on.merge(by, validate=validate)

    value_vars = [col for col in df.columns if col not in on.columns]
    df = df.melt(id_vars=on.columns, value_vars=value_vars, var_name='variable', value_name='value')

    df = df.assign(**{col: func(df, df['value'], df['variable']) for col, func in kwargs.items()})[
        list(set(list(on.columns) + list(kwargs.keys())))
    ]

    if inplace:
        return df
    return pd.concat([on, df])


def complete(target, with_cols_from, target_name='target', with_cols_from_name='with_cols_from'):
    common_cols = cols.common(target.columns, with_cols_from.columns)
    return target.merge(with_cols_from[common_cols].drop_duplicates(), how='outer', indicator=True).replace({
        'right_only': 'Not in ' + target_name, 'left_only': 'Not in ' + with_cols_from_name})


def melt_by_dates(
        df, begin_dt_column, end_dt_column,
        freq='M',
        period_column='period',
        begin_period_column='begin_period',
        end_period_column='end_period',
        *args, **kwargs):
    """
    Melts Dataframe based on to dates and a frequency

    """
    df = df.reset_index(drop=True)
    offset = pd.offsets.MonthEnd() if freq == 'M' else pd.offsets.YearEnd()
    return format.as_date(df[[begin_dt_column, end_dt_column]], columns=None, *args, **kwargs).apply(
        lambda x: pd.Series(
            pd.date_range(
                start=x[begin_dt_column],
                end=(x[end_dt_column] - pd.to_timedelta(1, unit='day')) + offset,
                freq=freq
            )
        ), axis=1
    ).stack().reset_index(level=-1, name=begin_period_column).rename(columns={'level_1': period_column}).assign(
        **{
            begin_period_column: lambda x: x[begin_period_column].to_numpy().astype('datetime64[M]'),
            end_period_column: lambda x: x[begin_period_column] + pd.offsets.MonthEnd()
        }
    ).join(df)


def interpolate(s, in_index=None, method=None):
    """
    Interpolates series
    """
    idx = pd.concat([s.index.to_series().reset_index(drop=True), in_index]).drop_duplicates()
    s = s.reindex(idx).sort_index()
    s = s.interpolate(method) if method else s.fillna(method='bfill')
    return s.reindex(in_index)


def common_lines(left, right, names=('left', 'right'), col_name='In_Table'):
    """
    From the common columns in both Dataframes find the common lines
    """
    common_cols = cols.common(left, right)
    df = left[common_cols].drop_duplicates().merge(
        right[common_cols].drop_duplicates(), how='outer', indicator=col_name)
    df[col_name] = df[col_name].str.replace('left', names[0]).str.replace('right', names[1])
    return df


def unique_lines(df, index, values=None, prefix='', *args, **kwargs):
    """
    From the common columns in both Dataframes find the common lines
    """
    values = values if values else cols.without(df, index)
    df = df[
        index + values
    ].drop_duplicates().groupby(index, dropna=False).count().sort_values(values, ascending=False).reset_index()
    return add.column_name(df, to_columns=values, prefix=prefix, *args, **kwargs)


def fancy_print(df):
    print(tabulate.tabulate(df, headers='keys', tablefmt='grid'))
