import pandas as pd
from ...db import TableImplementationError
from ..complete_table import project_cls as CompleteTable


class FillFrom(CompleteTable):
    _fill_from_columns = []
    _fill_from_index_columns = []

    def create(self, target, fill_source, *args, **kwargs):
        df_columns_to_add = target[self._fill_from_columns].drop_duplicates().merge(
            fill_source[self._fill_from_columns].drop_duplicates(),
            how='outer',
            indicator='SOURCE'
        )[lambda x: x['SOURCE'] == 'right_only'][self._fill_from_columns]

        df_columns_to_keep = target[self._fill_from_index_columns].drop_duplicates()

        new_lines = df_columns_to_keep.merge(df_columns_to_add, how='cross')

        return pd.concat([
            target.assign(INTERPOLATED='N'),
            new_lines.assign(INTERPOLATED='Y')
        ]).sort_values(self._fill_from_index_columns + self._fill_from_columns)


class InterpolateFrom(FillFrom):
    _interpolate_with_time = []
    _interpolate_column = []

    def create(self, target, fill_source, *args, **kwargs):
        df = super().create(target, fill_source, *args, **kwargs)

        return self.interpolate(
            df=df,
            x_time=self._interpolate_with_time,
            y=self._interpolate_column,
            by=self._fill_from_index_columns
        )

    @staticmethod
    def interpolate(df, x_time, y, by):
        """
        :param df:
        :param x_time: time variable that indicates the time between observations
        :param y:
        :param by:
        :return:
        """
        return df.groupby(by, dropna=False).apply(
            lambda group: group.set_index(x_time).assign(
                **{
                    y: lambda x: x[y].interpolate(
                        method='time',
                        limit_area='inside'
                    ).fillna(0)
                }
            ).reset_index()
        ).reset_index(drop=True)
