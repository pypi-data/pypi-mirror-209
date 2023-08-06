import pandas as pd
from ...db import TableImplementationError
from ..build_sequence import Table as CompleteTable
from ...df import discount


class Addlines(CompleteTable):
    """
    Adds lines based on config table
    """

    def create(
            self, target, config, how='inner', validate='many_to_one', test={}, var_name='variable', value_name='value',
            *args, **kwargs
    ):
        join_cols = [col for col in config.columns if col in target.columns]
        value_vars = [col for col in config.columns if col not in target.columns]
        id_vars = [col for col in target.columns if col not in [var_name, value_name]]
        if var_name not in target.columns:
            raise TableImplementationError(f'var_name:\'{var_name}\' not in target table, '
                                           f'should be column that diferentiates the new values, '
                                           f'add \'var_name\' parameter to \'build\' function')
        if value_name not in target.columns:
            raise TableImplementationError(f'value_name:\'{value_name}\' not in target table, '
                                           f'should be column that holds the new values, '
                                           f'add \'value_name\' parameter to \'build\' function')

        msg = f'\t\t Addlines: {how} join will be performed on {join_cols} and validated with {validate}'
        self.log.debug(msg)
        print(msg)
        df_new_lines = target.merge(
            config, how=how, validate=validate
        )
        df_new_lines = self.addlines_after_join(
            df_new_lines, var_name=var_name, value_name=value_name, *args, **kwargs
        ).drop(columns=[var_name, value_name])

        msg = f'\t\t Addlines: Table will be melted on {value_vars} and ' \
              f'new columns will be \'{var_name}\' and \'{value_name}\''
        self.log.debug(msg)
        print(msg)
        df_new_lines = df_new_lines.melt(
            id_vars=id_vars, value_vars=value_vars, var_name=var_name, value_name=value_name
        )
        print(df_new_lines.head())
        return pd.concat([target, df_new_lines])[target.columns]

    def addlines_after_join(self, df_new_lines, *args, **kwargs):
        """
        Redefine to be able to do a transformation to the joined value before the append
        :param df_new_lines:
        :return:
        """
        return df_new_lines


class NewAddlines(CompleteTable):
    """
    Adds lines based on config table

    config table should have two types of columns,
        merge columns: used to merge with target table (should have exactly same format and names)
        newlines columns: used to create the new sets of lines based on the operation in 'addlines_after_join'

    >>> class AddlinesTest(mr.db.NewAddlines):
    >>>     name = 'ADDLINES_TEST'
    >>>
    >>>     addlines_value_name = 'VALUE'
    >>>
    >>>     inputs_dicionary = {
    >>>         'target': 'test_table.csv',
    >>>         'config': 'CONFIG_RISK_ADJUSTMENT.csv'
    >>>     }
    >>>
    >>>     def addlines_simple_operation(self, x, *args, **kwargs):
    >>>         return x['VALUE'] * x['RISK_ADJ_PCT']
    >>>
    >>>
    >>> AddlinesTest().build(input=downloads, output=downloads, release_to=downloads)

    """

    var_name = 'Addlines'
    unchanged = '_old'
    changed = 'new'
    join_validate = 'many_to_one'

    @property
    def value_name(self):
        return self.materiality

    def create(self, target, config, *args, **kwargs):
        value_name = self.value_name
        join_cols = [col for col in config.columns if col in target.columns]
        value_vars = [col for col in config.columns if col not in target.columns] + [value_name]

        msg = f'\t\t Addlines: inner join will be performed on {join_cols}'
        self.log.debug(msg)
        print(msg)

        df_new_lines = target.merge(
            config, validate=self.join_validate
        )

        df_new_lines = self.addlines_after_join(
            df_new_lines, value_name=value_name, *args, **kwargs
        )

        id_vars = [col for col in df_new_lines.columns if col not in [value_name, self.var_name]]
        df_new_lines = df_new_lines.melt(
            id_vars=id_vars, value_vars=value_vars, var_name=self.var_name, value_name='_' + value_name
        ).rename(columns={'_' + value_name: value_name})

        try:
            target = target.assign(**{self.var_name: lambda x: x[self.var_name].fillna(self.unchanged)})
        except KeyError:
            target = target.assign(**{self.var_name: self.unchanged})

        return pd.concat([
            target,
            df_new_lines.reset_index(drop=True).assign(**{self.var_name: self.changed})
        ])

    def addlines_after_join(self, df_new_lines, *args, **kwargs):
        """
        Redefine to be able to do a transformation to the joined value before the append
        :param df_new_lines:
        :return:
        """
        return df_new_lines.assign(
            **{self.value_name: self.addlines_simple_operation(df_new_lines, *args, **kwargs)}
        )

    def addlines_simple_operation(self, x, *args, **kwargs):
        return x[self.value_name]


class AddDiscount(NewAddlines):

    @property
    def cashflow(self): return self.value_name

    with_rate = ''
    from_date = ''
    to_date = ''

    def addlines_simple_operation(self, x, *args, **kwargs):
        return discount.component(
                cashflow=x[self.cashflow], with_rate=x[self.with_rate],
                from_date=x[self.from_date], to_date=x[self.to_date]
            )
