import pandas as pd
import threading
from .tables import *
from ._build_sequence_phases import *
import traceback
import warnings
from .. import cp
from ..os import Folder
import os
from colorama import Fore



@logged(ref_folder='output')
class Table(BuildSequenceTests):

    sounds = 'matrix'
    sounds_started = False

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
    default_extension = '.parquet'
    release_extension = '.csv'

    def build(
            self, release_to=None, input=None, output=None, config=None, validation_output=None, logs=None,
            logs_backup=None, report_to=None,
            *args, **kwargs
    ):
        self.start_sounds()
        print(f'Creating {self.name} ({self.__class__.__name__})...')
        got_errors = False  # TODO delete
        error = None
        df = pd.DataFrame()  # TODO delete
        self.folder_definiton(
            input=input, output=output, config=config, validation_output=validation_output, logs=logs, release_to=release_to, logs_backup=logs_backup, report_to=report_to,
        )

        with self.log.section('Process of creating table'):

            self._phase('(01/08) Loading Inputs', self.load.run)

            try:

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

            except Exception as e:
                print(Fore.YELLOW)
                print('\t\t Error ocurred during excution,' 
                      'will create reports before printing it')  
                # warnings.warn(traceback.format_exc())
                print(Fore.WHITE)  
                self.log.error(traceback.format_exc())
                got_errors = True
                error = e
                    

            with self.log.section('Relevant reports'):
                try:
                    print(f'\t(08/08) Relevant reports...')
                    self.relevant_reports(df, *args, **self.format.output, **kwargs)
                except Exception as e:
                    warnings.warn(traceback.format_exc())
                    self.log.error(traceback.format_exc())
                self.save_reports()

            if got_errors:
                print(Fore.RED)
                raise error
                print(f'\tUnable to create {self.name} ({self.__class__.__name__}).')
                self.get_user_input()
                return df

            print(f'\tFinished creating {self.name} ({self.__class__.__name__}).')
        return df

    def get_user_input(self):

        print('Do you want to continue execution [y/n]:')
        x = input()
        if 'n' in x:
            raise SystemExit

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
                warnings.warn(traceback.format_exc())
                self.log.error(traceback.format_exc())
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

    def folder_definiton(self, input=None, output=None, config=None, validation_output=None, 
                         logs=None, release_to=None, logs_backup=None, report_to=None,):
        try:
            self.report_to = report_to
            self.release_to = release_to
            self.output = output if output else self.release_to
            self.input = input if input else self.output
            self.config = config or self.config or self.output
            self.output.new(folder='.dbReports')
        except AttributeError:
            print('Error accessing folder possible passed a None paramenter for input or output or'
                  'typed incorrectly \'input\' or \'output\'')
            

        if not isinstance(self.release_to, Folder) and self.release_to:
            raise TypeError('release_to is not a folder')
        if not isinstance(self.input, Folder):
            raise TypeError('input is not a folder')
        if not isinstance(self.output, Folder):
            raise TypeError('output is not a folder')
        

    def _phase(self, name, func, *args, **kwargs):
        with self.log.section(name):
            print(f'\t{name}...')
            rv = func(*args, **kwargs)
            try:
                self.update_excel_log(rv, name)
                self.log.report(*rv.values(), names=list(rv.keys()))
            except Exception as exc:
                warn('Unable to report')
                traceback.print_exception(type(exc), exc, exc.__traceback__)
            return rv

    def _phase_set_assumptions(self, *args, **kwargs):
        # df = self.set_assumptions(self._created_table, *args, **kwargs)
        df = self.set_assumptions(self.create_module.output, *args, **kwargs)
        self._assumptions_table = df
        return {'set_assumption_result': df}

    def new(self, report=None, description=None, name=None, with_tests=None):
        report = report.copy()
        if not name:
            name = ('Rep_' + str(len(self.generated_reports.keys()) + 1))[:31]
        if not description:
            description = name
        report.index.name = description
        self.generated_reports[name] = report

        # define testes associated with report
        if with_tests is not None:
            if not isinstance(with_tests, dict):
                with_tests = {name: test for test in with_tests}

            for desc, test in with_tests.items():
                self.define_test(df=name, pass_test=test, description=desc)

    def define_test(self, df, pass_test, description, fail_msg=None, sep='\n\n\t\t\t', *args, **kwargs):
        leng = 0
        mat = None
        df_str = None
        state = 'passed'

        if isinstance(df, str):
            df_str = df
            df = self.generated_reports[df]
        if not isinstance(pass_test, pd.Series):
            pass_test = pass_test(df)
        try:
            assert pass_test.all()
            self.log.debug(sep + f'Testing \'{description}\' passed for all rows')
        except AssertionError:
            state = 'failed'
            if len(pass_test) == len(df):
                leng = len(df[~pass_test])
                try:
                    if self.materiality:
                        mat = df.loc[~pass_test, self.materiality].astype(float).abs().sum() if self.materiality else 0
                        mat_all = max(df.loc[:, self.materiality].astype(float).abs().sum(), 1) if self.materiality else 1
                        mat_msg = f'\t{mat :,.2f} absolute monetary units or {mat/mat_all :.2%}\n'
                except KeyError:
                    pass
                self.new(report=df[~pass_test].sample(min(leng, 10000)), name='Auto_test_' + str(len(self.test_log) + 1))

        self._update_test_log(df, description, leng, id=str(len(self.test_log) + 1), mat=mat, table=df_str, state=state)

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
        except (AttributeError, ValueError):
            pass

    def _update_test_log(self, on, description, leng, id=None, mat=None, table=None, state=None):
        try:
            df_new_lines = pd.DataFrame({
                'excution_dt': [cp.Component.exec_dt],
                'user': [self.output.user],
                'class': [self.__class__.__name__],
                'table': [table if table else self.name],
                'id': id,
                'test_description': [description],
                'state': [state],
                'n_rows_that_failed': [leng],
                'materiality_that_failed': [mat],
                'materilaty_column_used': [self.materiality],
                'Total_rows': [len(on)],
                'Total_columns': [len(on.columns)]
            })
            # print(self.test_log.head())
            self.test_log = pd.concat([self.test_log, df_new_lines])
        except AttributeError:
            pass

    def save_reports(self):
        try:
            if len(self.test_log) > 0:
                df = self.test_log[self.test_log['state'] == 'failed']
                if len(df) > 0:
                    warn(f'The tests below have failed:\n {df}')
            self.new(report=self.excel_log, name='Auto_phase_log')
            self.new(report=self.test_log, name='Auto_test_log')
            self.output['.dbReports'].new(file=self.name + '.xlsx', with_obj=self.generated_reports)
        except PermissionError:
            print('Unable to save reports, please check that the file is closed')

    @staticmethod
    def basic_describe(*args, names, include="all", datetime_is_numeric=True, **kwargs):
        df = pd.DataFrame()
        for i, table in enumerate(args):
            d = table.describe(include=include, **kwargs).T
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

    # def relevant_reports(self, df, *args, **kwargs):
    #     self.log.debug('No Relevant reports were set, redefine function \'relevant_reports\' to set')
    #     return df

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

    def create(self, df, *args, **kwargs):
        return df

    def validate(self, *args, **kwargs):
        pass

    def construct(self, *args, **kwargs):
        pass

    def __init__(self, input: mros.Folder = None, output: mros.Folder = None, validation_output: mros.Folder = None, sounds=None):
        self.input = input
        self.output = output
        self.validation_output = validation_output if validation_output is not None else output
        self.data_dictionary_schema = None
        self.config = None
        self.excel_log = pd.DataFrame()
        self.test_log = pd.DataFrame()
        self.generated_reports = {}
        if sounds is not None:
            Table.sounds = sounds
        if sounds == 'off':
            Table.sounds_started = True

    def format_date_range(self, begin_dt, end_dt):
        begin_dt = pd.to_datetime(begin_dt, format='%d-%m-%Y')
        self.log.debug(f'Loaded begin_dt {begin_dt}')

        end_dt = pd.to_datetime(end_dt, format='%d-%m-%Y')
        self.log.debug(f'Loaded end_dt {end_dt}')

        return begin_dt, end_dt

    @classmethod
    def start_sounds(cls):
        if not Table.sounds_started:
            Table.sounds_started = True
            try:
                def loopSound():
                    while True:
                        from playsound import playsound
                        playsound(str(cp._settings.path) + '\\sounds\\' + Table.sounds + '.mp3', block=True)

                # providing a name for the thread improves usefulness of error messages.
                loopThread = threading.Thread(target=loopSound, name='backgroundMusicThread')
                loopThread.daemon = True  # shut down music thread when the rest of the program exits
                loopThread.start()
            except ModuleNotFoundError:
                warnings.warn('please install \'playsound\' package for full experience ;)')
            except Exception as e:
                print('unable to play sounds')

    def relevant_reports(self, *args, **kwargs):
        pass

    def __contains__(self, item):
        return dir(self).__contains__(item)
