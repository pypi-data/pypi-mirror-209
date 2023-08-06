from . import compare
from . import gen


def compared(**kwargs):
    return compare.types(*kwargs.values(), columns=kwargs.keys())


def different(*args, **kwargs):
    df_types = compared(*args, **kwargs)
    common_types = df_types.nunique(axis=1) == 1
    return df_types[~common_types]


def common(*args, **kwargs):
    df_types = compared(*args, **kwargs)
    common_types = df_types.nunique(axis=1) == 1
    not_in_all = df_types.isna().any(axis=1)
    return df_types[common_types & ~not_in_all]


def common_if_present(*args, **kwargs):
    df_types = compared(*args, **kwargs)
    common_types = df_types.nunique(axis=1) == 1
    not_in_all = df_types.isna().any(axis=1)
    return df_types[common_types & not_in_all]


