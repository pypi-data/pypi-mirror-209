import pandas as pd


def with_func(df, columns, func):
    """
    Tranforms the given columns based on the given function
    :param df: Table to be transformed
    :param columns: columns to be transformed
    :param func: function that receives the dataframe and the name of the column to be formated
    :return:
    """
    columns = columns if columns is not None else df.columns
    for column in columns:
        if column in df.columns:
            df = df.assign(**{column: func(df, column)})
    # return df.assign(**{column: lambda x: func(x, column) for column in columns if column in df.columns})
    return df


def as_date(df, columns=None, *args, **kwargs):
    """
    Tranforms the given columns into european dates in the given table
    :param df: Table to be transformed
    :param columns: columns to be transformed
    :return:
    """
    return with_func(df, columns, lambda x, column: pd.to_datetime(df[column], *args, **kwargs))


def as_set_len_code(df, columns=None, fillna='0'):
    """
    Tranforms the given columns into set lenght codes (ex. '001')
    :param df: Table to be transformed
    :param columns: dict
    columns to be transformed as keys, lenght of expected results as values
    :param lenght: columns to be transformed
    :return:
    """
    columns = columns if columns is not None else df.columns
    for column, lenght in columns.items():
        df = with_func(df, [column], lambda x, col: x[col].fillna(fillna).astype(str).str.zfill(lenght))
    return df


def dic_transpose(dic, method='values_to_keys'):
    return_dic = {}
    if method == 'values_to_keys':
        for key, val in dic.items():
            value_list = return_dic[val] if val in return_dic else []
            return_dic[val] = value_list + [key]

    if method == 'list_values_to_keys':
        for key, vals in dic.items():
            for val in vals:
                return_dic[val] = key

    return return_dic


def as_code(df, columns, lenght, fillna='0'):
    """
    Tranforms the given columns into set lenght codes (ex. '001')
    :param df: Table to be transformed
    :param columns: dict
    columns to be transformed as keys, lenght of expected results as values
    :param lenght: columns to be transformed
    :return:
    """
    columns = columns if isinstance(columns, list) else [columns]
    return with_func(df, columns, lambda x, col: x[col].fillna(fillna).astype(int).astype(str).str.zfill(lenght))


def as_code_for_series(s, lenght, fillna='0'):
    """
    Tranforms the given columns into set lenght codes (ex. '001')
    :param df: Table to be transformed
    :param columns: dict
    columns to be transformed as keys, lenght of expected results as values
    :param lenght: columns to be transformed
    :return:
    """
    return s.fillna(fillna).astype(str).str.zfill(lenght)


def as_float(df, columns=None, errors='coerce', fill=0.0):
    """
    Tranforms the given columns into floats
    :param df: Table to be transformed
    :param columns: dict
    columns to be transformed as keys, lenght of expected results as values
    :param lenght: columns to be transformed
    :return:
    """
    return with_func(df, columns, lambda x, column: pd.to_numeric(x[column], errors=errors).fillna(fill))


def as_int(df, columns=None, *args, **kwargs):
    """
    Tranforms the given columns into floats
    :param df: Table to be transformed
    :param columns: dict
    columns to be transformed as keys, lenght of expected results as values
    :param lenght: columns to be transformed
    :return:
    """
    return with_func(df, columns, lambda x, column: df[column].astype(int, *args, **kwargs))


def as_string(df, columns=None):
    """
    Tranforms the given columns into strings
    :param df: Table to be transformed
    :param columns: dict
    columns to be transformed as keys, lenght of expected results as values
    :param lenght: columns to be transformed
    :return:
    """
    return with_func(df, columns, lambda x, column: df[column].astype(str))


def all(df, as_strings=None, as_floats=None, as_set_len_codes=None, as_dates=None):
    if as_strings is not None:
        df = as_string(df, columns=as_strings)
    if as_floats is not None:
        df = as_float(df, columns=as_floats)
    if as_set_len_codes is not None:
        df = as_set_len_code(df, columns=as_set_len_codes)
    if as_dates is not None:
        df = as_date(df, columns=as_dates)

    return df
