import pandas as pd
from .dataframe import DataFrame


def read_csv(*args, **kwargs):
    return DataFrame(pd.read_csv(*args, **kwargs))


def read_sas(*args, **kwargs):
    return DataFrame(pd.read_sas(*args, **kwargs))


def read_excel(*args, **kwargs):
    return DataFrame(pd.read_excel(*args, **kwargs))


def read_feather(*args, **kwargs):
    return DataFrame(pd.read_feather(*args, **kwargs))


def concat(*args, **kwargs):
    return DataFrame(pd.concat(*args, **kwargs))


