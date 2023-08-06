from functools import cached_property
import itertools
import pprint
from ... import cp
import pandas as pd
from ...attach import attachment
from ..utils import TableAttachmentProtocol, TableImplementationError
from ...df import format
from .utils import Format


@attachment
class Formatter(TableAttachmentProtocol):

    def run(self, on, *args, **kwargs):
        self.formatter_inputs = on
        self.output = on
        self.output = self.format_inputs(on, *args, **kwargs)
        return self.output

    columns_formats = {}

    @property
    def _column_formats(self):
        relevant_column_formats = {}
        items = cp.AttributeSelector()('column_formats', 'f', instance=self._instance)
        if self.column_formats:
            relevant_column_formats = {
                arg: {
                    ty: [
                        col for col in cols if col in self.formatter_inputs[arg].columns
                    ] for ty, cols in format_dic.items()
                }
                for arg, format_dic in items.items()
            }
        print('--------------------------------------')
        print(relevant_column_formats)
        return relevant_column_formats

    def format_inputs(self, on, *args, **kwargs):
        inputs = self.utils.rename_columns_inputs(on, self.rename_columns)
        try:  # tries to run overwritten format inputs
            self.output = self._format_based_format_input(inputs)
            print('\t\tFormated with \'format_input\'')
        except (TableImplementationError, AttributeError):
            try:  # if not defined tries to it own format inputs
                self.output = self._format_based_on_dic(inputs)
                print('\t\tFormatted with \'Format dic\'')
            except (TableImplementationError, AttributeError):  # if not possible it does nothing
                self.output = inputs
        return self.output

    def _format_based_format_input(self, inputs):
        return {
            k: (v if k in self._instance.formatted_inputs else self._instance.format_input(v))
            for k, v in inputs.items()
        }

    def _format_based_on_dic(self, inputs):
        self.output = {
            # arg: self.utils.format.table(table, self._column_formats[arg]) for arg, table in inputs.items()
            arg: self.utils.format.table(table, cp.AttributeSelector()('column_formats', 'f', instance=self._instance)) for arg, table in inputs.items()
        }
        return self.output

    def _format_formats_warn(self, formatted_cols):
        seen = set()
        dupes = [col for col in formatted_cols if col in seen or seen.add(col)]
        if len(dupes):
            msg = f'\t\tThe following columns were formatted twice: {dupes}, ' \
                  f'change \'column_formats\' to increase performance'
            print(msg)
            self.log.debug(msg)

    @staticmethod
    def _add_args_to_dic(dic, args):
        return {arg: dic for arg in args}


    # @property
    # def column_formats(self):
    #     msg = \
    #         """
    #             \'columns_formats\' not defined, should be defined as a dictionary of the form
    #             >>> column_formats = {\'format\': ['columns_a', 'columns_b']}
    #         """
    #     raise TableImplementationError(msg)


@attachment
class FormatterLegacy(TableAttachmentProtocol):

    def rename_columns_inputs(self, inputs, rename_dic):
        if len(rename_dic) > 0:
            self._instance.log.debug(f'Renaming columns according to {rename_dic}')
        for arg_name, table in inputs.items():
            renme_dic = {}
            for new_name, old_names in self._instance.rename_columns.items():
                old_names = old_names if isinstance(old_names, list) else [old_names]
                for old_name in old_names:
                    if old_name in table.columns:
                        renme_dic[old_name] = new_name

            inputs[arg_name] = table.rename(columns=renme_dic)
        return inputs

    def format_inputs(self, on, *args, **kwargs):
        try:
            return self._instance.data_dictionary_module.format_with_data_dicionary()
        except TableImplementationError:
            self._instance.log.debug('Unable to use Datadictionary found running with \'schema\' and \'format input\' variables')
            inputs = self.rename_columns_inputs(on, self._instance.rename_columns)
            return {k: (v if k in self._instance.formatted_inputs else self._instance.format_input(v)) for k, v in inputs.items()}

    def run(self, on, *args, **kwargs):
        self.output = self.format_inputs(on, *args, **kwargs)
        return self.output
        # format input
        # formated inputs
        # data dic


@attachment
class DataDictionary:
    data_dictionary_schema = None

    def fill_data_dictionary(self, df, *args, **kwargs):
        self._instance.log.debug('defined data dictionary but not in data dictionary')
        df_prop_dd = pd.DataFrame(df.dtypes).reset_index().reset_index()
        df_prop_dd.columns = ['ORDER', 'COLUMN', 'FORMAT_AS']
        df_prop_dd = df_prop_dd.assign(ORDER=lambda x: x['ORDER'] + 1, TABLE=self._instance.name)[[
            'TABLE', 'ORDER', 'COLUMN', 'FORMAT_AS'
        ]]
        df_prop_dd['FORMAT_AS'] = df_prop_dd['FORMAT_AS'].replace({
            'datetime64[ns]': 'DATE', 'object': 'STR', 'float64': 'FLOAT', 'int64': 'INT'
        })
        data_dic = self.data_dictionary_df
        try:
            data_dic = data_dic.drop(columns='ARG')
        except KeyError:
            pass
        data_dic = pd.concat([data_dic, df_prop_dd])
        self._instance.config.new(file=self._instance.data_dictionary, with_obj=data_dic, index=False, *args, **kwargs)
        print(data_dic)

    @cached_property
    def data_dictionary_df(self):
        return self._instance.config.get(self._instance.data_dictionary)

    @cached_property
    def format_dictionary(self):
        self.table_inputs = self._instance.load.table_inputs

        df = self.data_dictionary_df
        df['ARG'] = df['TABLE'].replace({table: arg for arg, table in self .table_inputs.items()})
        df = df[df['ARG'].isin(list(self.table_inputs.keys()) + [self._instance.name])]

        inputs = list(self.table_inputs.values()) + [self._instance.name]

        df = df.sort_values(['TABLE', 'ORDER'])

        self.data_dictionary_schema = df.loc[df['TABLE'] == self._instance.name, 'COLUMN'].to_list()

        format_dic = {}
        for table in inputs:
            table_format_dic = {}
            df_inputs = df.loc[df['TABLE'] == table, :]

            # floats
            floats = df_inputs.loc[df_inputs['FORMAT_AS'] == 'FLOAT', 'COLUMN'].to_list()
            table_format_dic['FLOAT'] = floats

            # strings
            strings = df_inputs.loc[df_inputs['FORMAT_AS'] == 'STR', 'COLUMN'].to_list()
            table_format_dic['STR'] = strings

            # Dates
            table_dates_format_dic = {}
            df_dates = df_inputs[df_inputs['FORMAT_AS'] == 'DATE']
            date_formats = df_dates['FORMAT_WITH'].drop_duplicates().to_list()
            for date_format in date_formats:
                dates = df_dates.loc[df_dates['FORMAT_WITH'] == date_format, 'COLUMN'].to_list()
                table_dates_format_dic[date_format] = dates

            table_format_dic['DATE'] = table_dates_format_dic

            # Codes
            codes = df_inputs.loc[df_inputs['FORMAT_AS'] == 'CODE', ['COLUMN', 'FORMAT_WITH']].to_dict('split')
            codes = {record[0]: int(record[1]) for record in codes['data']}
            table_format_dic['CODE'] = codes
            format_dic[table] = table_format_dic

        return format_dic

    @cached_property
    def format_dictionary_input(self):
        return {
            arg: type_format_dic
            for table, type_format_dic in self.format_dictionary.items()
            for arg, table_name in self.table_inputs.items()
            if table == table_name
        }

    def format_based_on_datadictionary(self, df, dic):
        table = format.as_float(df, dic['FLOAT'])
        table = format.as_string(table, dic['STR'])
        table = format.as_set_len_code(table, dic['CODE'])
        for date_format, columns in dic['DATE'].items():
            table = format.as_date(table, columns, format=date_format)
        return table

    def format_inputs(self, on, *args, **kwargs):
        try:
            if self._instance.data_dictionary and self._instance.table_inputs:
                last_inputs = {}
                for arg, table in self._instance.last_inputs.items():
                    table = self.format_based_on_datadictionary(table, self.format_dictionary_input[arg])
                    df = self.data_dictionary_df
                    df_rename = {name[0]: name[1] for name in df.loc[
                        (df['ARG'] == arg) & (df['RENAME_TO'].notnull()), ['COLUMN', 'RENAME_TO']
                    ].to_dict('split')['data']}

                    table = table.rename(columns=df_rename)
                    last_inputs[arg] = table

                self.load_inputs = lambda: last_inputs
                self._instance.log.debug('Used Datadictionary')

                return last_inputs

        except TableImplementationError:
            self._instance.log.debug('Unable to use Datadictionary found running with \'schema\' and \'format input\' variables')
            inputs = self.rename_columns_inputs(on, self._instance.rename_columns)
            return {k: (v if k in self._instance.formatted_inputs else self._instance.format_input(v)) for k, v in inputs.items()}

    def format_with_data_dicionary(self):
        if self._instance.data_dictionary and self._instance.table_inputs:
            last_inputs = {}
            for arg, table in self._instance.last_inputs.items():
                table = self.format_based_on_datadictionary(table, self.format_dictionary_input[arg])
                df = self.data_dictionary_df
                df_rename = {name[0]: name[1] for name in df.loc[
                    (df['ARG'] == arg) & (df['RENAME_TO'].notnull()), ['COLUMN', 'RENAME_TO']
                ].to_dict('split')['data']}

                table = table.rename(columns=df_rename)
                last_inputs[arg] = table

            self.load_inputs = lambda: last_inputs
            self._instance.log.debug('Used Datadictionary')

            return last_inputs






