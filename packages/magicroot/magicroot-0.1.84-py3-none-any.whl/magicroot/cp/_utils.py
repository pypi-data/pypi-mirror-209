from ._component import Component


class _PullForward(Component):
    def __call__(self, df, cols, *args, **kwargs):
        return df[cols + [col for col in df.columns if col not in cols]]


df_cols_pull_forward = _PullForward()

