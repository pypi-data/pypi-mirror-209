import numpy as np


def _base(columns, by, func, *args, **kwargs):
    return lambda x: x[by].merge(
            x[by + [col for col in columns if col not in by]].groupby(by, *args, **kwargs).agg(func).reset_index(),
            how='left', on=by, validate='many_to_one'
        )[columns].set_index(x.index)


def withfunc(columns, by, func, *args, **kwargs):
    return _base(columns, by, func, *args, **kwargs)


def cumsum(columns, by, order, ascending=None, *args, **kwargs):
    return lambda x: x.sort_values(by + order, ascending=ascending)[by + columns].groupby(by, *args, **kwargs).cumsum()


def sum(columns, by, *args, **kwargs):
    return _base(columns, by, func=np.sum, *args, **kwargs)


def diff(columns, by, *args, **kwargs):
    return _base(columns, by, func=np.diff, *args, **kwargs)


def max(columns, by):
    return lambda x: x[by + columns].groupby(by).max().reset_index().merge(
        x.reset_index()[by], how='right', validate='one_to_many'
    )[columns]


def min(columns, by):
    return lambda x: x[by + columns].groupby(by).min().reset_index().merge(
        x.reset_index()[by], how='right', validate='one_to_many'
    )[columns]


def count(columns, by, *args, **kwargs):
    return _base(columns, by, func='count', *args, **kwargs)


def apply(columns, by, func, *args, **kwargs):
    """
    Create column based on Dataframe shape with the result of a groupby apply

    :Parameters:
        columns : list
            Columns to return, result of apply
        by : list
            Columns to use for grouping
        func: callable
            Function to pass to the ''apply''

    :Returns:
        callable(pandas.Dataframe)
            A function that can be applied to a Dataframe
    """
    return lambda x: x[by + columns].groupby(by, group_keys=False, *args, **kwargs).apply(func)[columns]


def pattern(columns, by, *args, **kwargs):
    return apply(columns, by, func=lambda x: x/x.sum(numeric_only=True), *args, **kwargs)
