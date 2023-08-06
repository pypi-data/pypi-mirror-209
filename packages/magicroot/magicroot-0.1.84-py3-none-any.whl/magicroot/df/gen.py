import numpy as np
import pandas as pd


def counting_col():
    return lambda x: np.arange(x.shape[0])


def coupled_series(*args):
    max_size = {len(arg): arg for arg in args if isinstance(arg, pd.Series)}
    max_arg = max_size[max(max_size.keys())]

    df = max_arg.to_frame('other')
    for i, arg in enumerate(args):
        df['__L' + str(i)] = arg
    return [df[col] for col in df if col[:3] == '__L']


def dataframe_from_series(**kwargs):
    """
    Create Dataframe with series and constants elements
    """
    return pd.concat(coupled_series(*kwargs.values()), axis=1, keys=kwargs.keys())

