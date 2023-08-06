from ._component import Component
import pandas as pd


class Propagate(Component):
    def run(self, target, config, inplace=False, validate=None, **kwargs):

        df = target.merge(config, validate=validate)

        value_vars = [col for col in df.columns if col not in target.columns]
        df = df.melt(id_vars=target.columns, value_vars=value_vars, var_name='variable', value_name='value')

        df = df.assign(**{col: func(df, df['value'], df['variable']) for col, func in kwargs.items()})[target.columns]

        if inplace:
            return df
        return pd.concat([target, df])



