

def without(df, columns):
    """
    Get list of columns of Dataframe except from a given list

    :Parameters:
        df : pandas.Dataframe
            Dataframe to operate on
        to_columns : list
            Columns to exclude

    :Returns:
        list, tuple or iterable
            list of columns of the Dataframe except those specified 'columns' parameter

    Examples
    ----------

    This has an alias of ``code-block``.


    .. code-block:: python
        :linenos:

        from typing import Iterator

        # This is an example
        class Math:
            @staticmethod
            def fib(n: int) -> Iterator[int]:
                "Fibonacci series up to n"
                a, b = 0, 1
                while a < n:
                    yield a
                    a, b = b, a + b


        result = sum(Math.fib(42))
        print("The answer is {}".format(result))

    """
    return [col for col in df.columns if col not in columns]


def pull(df, columns, to_the_begin=True):
    """
    Pull columns to the begin or the end of the Dataframe

    :Parameters:
        df : pandas.Dataframe
            Dataframe to operate on
        columns : list
            Columns to pull forward or backwards
        to_the_begin: Bool, default True

    :Returns:
        pandas.Dataframe
            'df' with the columns reordered
    """
    if to_the_begin:
        return df[columns + without(df, columns)]
    return df[without(df, columns) + columns]


def common(df, df_other):
    """
    Get list of common columns between two Dataframes

    :param df: *pandas.Dataframe* Dataframe to operate on
    :param df_other: *pandas.Dataframe* Dataframe to operate on
    :return: *list* list of columns of the Dataframe except those specified 'columns' parameter
    """
    return [col for col in df.columns if col in df_other.columns]


def split(df, all_except, value_name='value', sep='_', **kwargs):
    """
    Split columns based on filter

    :param df: *pandas.Dataframe* Dataframe to operate on
    :param all_except: *pandas.Dataframe* Dataframe to operate on
    :param value_name: *pandas.Dataframe* Dataframe to operate on
    :param sep: *pandas.Dataframe* Dataframe to operate on
    :param kwargs: *dict of {str: callable or Series}* Dataframe to operate on
    :return: *list* list of columns of the Dataframe except those specified 'columns' parameter
    """
    return df.melt(
        id_vars=all_except, value_name=value_name, var_name='col_names'
    ).assign(**kwargs).drop(columns=value_name).melt(
        id_vars=all_except + ['col_names'], value_name='split', var_name='variable'
    ).assign(col_names=lambda x: x['col_names'] + sep + x['variable']).pivot(
        index=all_except,
        columns='col_names',
        values='split'
    ).reset_index()


