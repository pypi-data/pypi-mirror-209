
from .tables import *
from ._build_sequence_phases import *
import traceback
import warnings
from .. import cp
from ..os import home


@logged(ref_folder='output')
class BuildSequenceTable(BuildSequenceTests):

    load = AggInputs()
    format = Formatter()
    create_module = FreestyleCreate()
    save_module = SavingOutputs()
    validate_module = ValidateOutputs()
    folders = FoldersStorage()
    utils = Utils()

    data_dictionary_module = DataDictionary()

    formatted_inputs = []
    drop_duplicates = False
    materiality = None
    data_dictionary = None
    config = None
    rename_columns = {}
    schema = []
    default_extension = '.ftr'
    release_extension = '.csv'

    def build(
            self, release_to=None, input=None, output=None, config=None, validation_output=None, logs=None,
            logs_backup=None, report_to=None,
            *args, **kwargs
    ):

        print(f'Creating {self.name} ({self.__class__.__name__})...')

        self.folder_definiton(
            input=input, output=output, config=config, validation_output=validation_output, logs=logs, release_to=release_to, logs_backup=logs_backup, report_to=report_to,
        )

        with self.log.section('Process of creating table'):

            self._phase('(01/08) Loading Inputs', self.load.run)

            self._phase('(02/08) Formating Inputs', self.format.run, self.load.output)

            self._phase('(03/08) Creating Table', self.create_module.run, self.format.output, *args, **kwargs)

            df = self._phase('(04/08) Applying Assumptions', self._phase_set_assumptions, *args, **kwargs)
            df = df['set_assumption_result']

            with self.log.section('Selecting appropriate schema'):
                print(f'\t(05/08) Selecting appropriate schema...')
                if self.schema:
                    df = self.fill_schema(self._assumptions_table, schema=self.schema)
                    df = df[self.schema]
                if self.data_dictionary_module.data_dictionary_schema:
                    pass
                else:
                    try:
                        self.data_dictionary_module.fill_data_dictionary(df)
                    except (TableImplementationError, ValueError, AttributeError):
                        pass
                if self.drop_duplicates:
                    df = df.drop_duplicates()
                else:
                    self.log.info('No schema was provided for this table')

            self._phase('(06/08) Saving Outputs', self.save_module.run, df, release_to=release_to)

            self._phase('(07/08) Validate Outputs', self.validate_module.run, df, *args, **kwargs)

            with self.log.section('Relevant reports'):
                try:
                    print(f'\t(08/08) Relevant reports...')
                    self.relevant_reports(df, *args, **kwargs)
                except Exception as e:
                    warnings.warn('Unable to produce reports, see log for error')
                    self.log.error(traceback.format_exc())
                self.save_excel_log()
                self.save_reports()

            print(f'\tFinished creating {self.name} ({self.__class__.__name__}).')

        return df

    def valid(self, output=None, release_to=None, validate=True, *args, **kwargs):
        print(f'Validating {self.name} ({self.__class__.__name__})...')

        self.folder_definiton(output=output, release_to=release_to)
        df = self.output.get(self.save_name)

        if validate:
            self._phase('Validate Outputs', self.validate_module.run, df, *args, **kwargs)

        with self.log.section('Relevant reports'):
            try:
                print(f'\tRelevant reports...')
                self.relevant_reports(df, *args, **kwargs)
            except Exception as e:
                warnings.warn('Unable to produce reports, see log for error')
                self.log.error(traceback.format_exc())
            self.save_excel_log()
            self.save_reports()

    def report(self, output=None, release_to=None, *args, **kwargs):
        print(f'Reporting {self.name} ({self.__class__.__name__})...')
        self.output = output
        self.release_to = release_to
        df = output.get(self.save_name)

        with self.log.section('Relevant reports'):
            try:
                print(f'\tRelevant reports...')
                self.relevant_reports(df, *args, **kwargs)
            except Exception as e:
                warnings.warn('Unable to produce reports, see log for error')
                self.log.error(traceback.format_exc())

    def folder_definiton(self, input=None, output=None, config=None, validation_output=None, logs=None, release_to=None, logs_backup=None, report_to=None,):
        self.report_to = report_to
        self.release_to = release_to
        self.output = output if output else self.release_to
        self.input = input if input else self.output
        self.config = config or self.config or self.output
        self.output.new(folder='.dbReports')

    def _phase(self, name, func, *args, **kwargs):
        with self.log.section(name):
            print(f'\t{name}...')
            rv = func(*args, **kwargs)
            self.update_excel_log(rv, name)
            self.log.report(*rv.values(), names=list(rv.keys()))
            return rv

    def _phase_set_assumptions(self, *args, **kwargs):
        # df = self.set_assumptions(self._created_table, *args, **kwargs)
        df = self.set_assumptions(self.create_module.output, *args, **kwargs)
        self._assumptions_table = df
        return {'set_assumption_result': df}

    def new(self, report=None, description=None, name=None):
        if not name:
            name = 'Rep_' + str(len(self.generated_reports.keys()) + 1)
        if not description:
            description = name
        report.index.name = description
        self.generated_reports[name[:31]] = report

    def define_test(self, df, pass_test, description, fail_msg=None, sep='\n\n\t\t\t', *args, **kwargs):
        leng = 0
        mat = None
        try:
            assert pass_test.all()
            self.log.debug(sep + f'Testing \'{description}\' passed for all rows')
        except AssertionError:
            if fail_msg:
                msg = sep + fail_msg + sep
            else:
                len_msg = ''
                mat_msg = ''
                sample = ''
                if len(pass_test) == len(df):
                    leng = len(df[~pass_test])
                    leng_all = max(len(df), 1)
                    len_msg = f'\t{leng} rows or {leng/leng_all :.2%}\n'
                    if self.materiality:
                        mat = df.loc[~pass_test, self.materiality].astype(float).abs().sum() if self.materiality else 0
                        mat_all = max(df.loc[:, self.materiality].astype(float).abs().sum(), 1) if self.materiality else 1
                        mat_msg = f'\t{mat :,.2f} absolute monetary units or {mat/mat_all :.2%}\n' \

                        sample = self.log.sample(df[~pass_test], names=['Test'], log=False)
                msg = sep + \
                      f'Testing \'{description}\' failed \n' + \
                      sep + len_msg + sep + mat_msg + sep + f'{sample}' + sep

            self.log.info(msg)
            warnings.warn(msg)
        self._update_test_log(df, description, leng, mat=mat)

    def test_nulls(self, df, columns=None):
        columns = columns if columns else df.columns
        for column in columns:
            self.log.debug(f'Assering that {column} is not null')
            if column in df.columns:
                self.define_test(
                    df=df,
                    pass_test=df[column].notnull(),
                    description=f'that {column} is not null'
                )

    def update_excel_log(self, rv, phase):
        try:
            df_new_lines = self.basic_describe(*rv.values(), names=list(rv.keys())).assign(
                dt=cp.Component.exec_dt,
                Class=self.__class__.__name__,
                Phase=phase
            )
            self.excel_log = pd.concat([self.excel_log, cp.df_cols_pull_forward(df_new_lines, ['dt', 'Class', 'Phase'])])
        except AttributeError:
            pass

    def save_excel_log(self):
        try:
            # home[cp.Settings('cp', 'settings_config')['path']].append_to('phase_log.xlsx',
            #                                                              with_obj=self.excel_log)
            self.output['.dbReports'].append_to('phase_log.xlsx', with_obj=self.excel_log)
        except (PermissionError, pd._config.config.OptionError):
            print('Unable to save phase log')

    def save_reports(self):
        if len(self.generated_reports.keys()) > 0:
            try:
                self.output['.dbReports'].new(file=self.name + '.xlsx', with_obj=self.generated_reports)
            except PermissionError:
                print('Unable to save phase log')

    @staticmethod
    def basic_describe(*args, names, include="all", datetime_is_numeric=True, **kwargs):
        df = pd.DataFrame()
        for i, table in enumerate(args):
            d = table.describe(include=include, datetime_is_numeric=datetime_is_numeric, **kwargs).T
            d = d.assign(Table=names[i], Column=d.index)

            n = min([len(table), 5])
            samples = table.sample(n=n, **kwargs).T.reset_index(names='Column').assign(Table=names[i])
            samples.columns = ['sample_' + str(i) if col not in ['Column', 'Table'] else col for i, col in
                               enumerate(samples.columns)]

            d = d.merge(
                pd.DataFrame({'sum': table.sum(numeric_only=True, **kwargs)}).reset_index(names='Column').assign(
                    Table=names[i]),
                how='outer'
            ).merge(
                pd.DataFrame({'Type': table.dtypes}).reset_index(names='Column').assign(Table=names[i]),
                how='outer'
            ).merge(
                samples,
                how='outer'
            )
            df = pd.concat([df, d])
        df = df[['Table', 'Column'] + [col for col in df.columns if col not in ['Column', 'Table']]]
        return df

    def _update_test_log(self, on, description, leng, mat=None):
        # folder = home[cp.Settings('cp', 'settings_config')['path']]
        pass
        # folder = self.output['.dbReports']
        # try:
        #     df = folder.get('test_log.csv', exact_match=True, encoding='latin-1')
        # except FileNotFoundError:
        #     df = pd.DataFrame()
        # df_new_line = pd.DataFrame({
        #     'datetime': [cp.Component.exec_dt],
        #     'user': [self.output.user],
        #     'table': [self.name],
        #     'class': [self.__class__.__name__],
        #     'test': [description],
        #     'rows_for_fail': [leng],
        #     'materiality_of_fail': [mat],
        #     'materilaty_column': [self.materiality],
        #     'rows': [len(on)],
        #     'columns': [len(on.columns)]
        # })
        # folder.new(file='test_log.csv', with_obj=pd.concat([df, df_new_line]), index=False)

    @staticmethod
    def format_input(df):
        raise TableImplementationError()

    def add_constant_columns(self, df):
        self.log.debug(f'Creating constant columns')
        return df.assign(
            **self.constant_columns
        )

    @property
    def constant_columns(self):
        return {}

    def fill_schema(self, df, cons='', schema=None):
        for column in schema:
            if column not in df.columns:
                df[column] = cons
        return df

    def save(self, df):
        self.output.new(file=self.save_name, with_obj=df)
        path = os.path.join(self.output.path, self.save_name)
        print(f'\t\tSaved results to {path}')

    def release(self, df, release_folder, *args, **kwargs):
        release_folder.new(file=self.save_release_name, with_obj=df, index=False, *args, **kwargs)
        path = os.path.join(release_folder.path, self.save_release_name)
        print(f'\t\tReleased results to {path}')

    def relevant_reports(self, df, *args, **kwargs):
        self.log.debug('No Relevant reports were set, redefine function \'relevant_reports\' to set')
        return df

    def set_assumptions(self, df,  *args, **kwargs):
        self.log.debug('No Assumptions were set')
        return df

    @property
    def data_dictionary(self):
        raise TableImplementationError(
            'Property data_dictionary not defined, '
            )

    @property
    def name(self):
        # Split the string into words
        words = re.findall('[A-Z][^A-Z]*', self.__class__.__name__)

        # Capitalize each word and join them with an underscore
        return '_'.join([word.upper() for word in words])

    @property
    def release_name(self):
        return self.name

    @property
    def save_name(self):
        return self.name + self.default_extension

    @property
    def save_release_name(self):
        return self.release_name + self.release_extension

    @property
    def applicable_data_dictionary_df(self):
        df = self.data_dictionary_df
        df['ARG'] = df['TABLE'].replace({table: arg for arg, table in self.table_inputs.items()})
        return df[df['ARG'].isin(list(self.table_inputs.keys()) + [self.name])]

    def create(self, *args, **kwargs):
        return *args, *kwargs

    def validate(self, *args, **kwargs):
        pass

    def construct(self, *args, **kwargs):
        pass

    def __init__(self, input: mros.Folder = None, output: mros.Folder = None, validation_output: mros.Folder = None):
        self.input = input
        self.output = output
        self.validation_output = validation_output if validation_output is not None else output
        self.data_dictionary_schema = None
        self.config = None
        self.excel_log = pd.DataFrame()
        self.generated_reports = {}

    def format_date_range(self, begin_dt, end_dt):
        begin_dt = pd.to_datetime(begin_dt, format='%d-%m-%Y')
        self.log.debug(f'Loaded begin_dt {begin_dt}')

        end_dt = pd.to_datetime(end_dt, format='%d-%m-%Y')
        self.log.debug(f'Loaded end_dt {end_dt}')

        return begin_dt, end_dt
