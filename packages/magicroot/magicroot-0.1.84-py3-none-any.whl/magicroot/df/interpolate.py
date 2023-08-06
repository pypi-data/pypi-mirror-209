import pandas as pd


def series(s, in_index=None, method=None):
    """

    .. deprecated:: v0.0.2
                    to be moved to :py:func:`magicroot.df.tec.interpolate`.

    """
    idx = pd.concat([s.index.to_series(), in_index]).drop_duplicates()
    s = s.reindex(idx).sort_index()
    s = s.interpolate(method) if method else s.fillna(method='bfill')
    return s.reindex(in_index)



