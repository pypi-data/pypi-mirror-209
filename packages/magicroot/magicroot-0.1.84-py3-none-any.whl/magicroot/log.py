import logging
from .time import Timer
from contextlib import contextmanager
import pandas as pd
import datetime
import os
from ._tools import df


class Log(logging.Logger):
    line = '/*********************************************************************************************************/'
    half_line_space = '                                                    '

    def __init__(self, *args, **kwargs):
        self.timers = {}
        super().__init__(*args, **kwargs)

    def some_random_method(self):
        print('hello world')

    @contextmanager
    def section(self, name):
        self.debug(f'{self.line} \n{self.half_line_space} {name}\n{self.line}')
        self.timers[name] = Timer()
        yield
        time_taken = self.timers[name].lap()
        self.debug(f'Section \'{name}\' took {time_taken} to run \n\n')
        time_taken_str = str(time_taken).split(".")[0]
        if time_taken_str != '0:00:00':
            print(f'\t\t(took {time_taken_str})')

    @contextmanager
    def timer(self, name='root'):
        self.timers[name] = Timer()
        self.debug(f'Started timer \'{name}\'')
        yield
        self.debug(f'Stopped timer \'{name}\' at: {self.timers[name].lap()}')

    def time(self, name='root'):
        try:
            self.debug(f'Stopped timer \'{name}\' at: {self.timers[name].lap()}')
        except KeyError:
            self.timers[name] = Timer()
            self.debug(f'Started timer \'{name}\'')

    def left_join(self, left, joinned):
        self.debug(f'After left join the table has {len(left)} increased lines by '
                   f'{(len(left) / len(joinned) - 1):.0%}')

    def df_filter(self, pre_filter, pos_filter):
        if len(pre_filter) > 0:
            self.debug(f'After the filter the table has {len(pos_filter)} rows, decreased lines by '
                       f'{len(pre_filter) - len(pos_filter)} or {1 - (len(pos_filter) / len(pre_filter)):.0%}')
        return pos_filter

    def types(self, *args, **kwargs):
        try:
            df_types = df.compare.types(*args, **kwargs)
            df_types.columns = [f'\'{col}\'' for col in df_types.columns]
            common_types = df_types.nunique(axis=1) == 1
            not_in_all = df_types.isna().any(axis=1)
            mgn = '\nThe given tables have the following'
            self.debug(
                f'{mgn} different types\n{df_types[~common_types]}\n'
                f'{mgn} common types in the tables they are present \n{df_types[common_types & not_in_all]}\n'
                f'{mgn} common types in all tables \n{df_types[common_types & ~not_in_all]}\n'

            )
        except (AttributeError, ValueError):
            pass

    def describe(self, *args, names, include="all", datetime_is_numeric=True, **kwargs):
        desc = pd.DataFrame()
        for i, table in enumerate(args):
            d = table.describe(include=include, **kwargs).T
            d = d.assign(Table=names[i], Column=d.index).set_index(['Table', 'Column'])
            desc = pd.concat([desc, d])
        self.debug(f'Describe is shown a below \n {desc}')

    def sum(self, *args, names, **kwargs):
        msg = 'Sums of given tables are showned below'
        for i, table in enumerate(args):
            msg = msg + f'\n\nSum of \'{names[i]}\' is shown a below \n{table.sum(numeric_only=True, **kwargs)}'
        self.debug(msg)

    def sample(self, *args, names, n=5, log=True, **kwargs):
        n = min([len(arg) for arg in args] + [5])
        msg = 'Samples of given tables are showned below'
        for i, table in enumerate(args):
            msg = msg + f'\n\nSample \'{names[i]}\' is shown a below \n{table.sample(n=n, **kwargs)}'
        if log:
            self.debug(msg)
        else:
            return msg

    def _log_args(self, func, intro='', *args):
        msg = intro
        for i, table in enumerate(args):
            msg = msg + func(i, table)
        self.debug(msg)

    def report(self, *args, names, n=5, include="all", datetime_is_numeric=True, **kwargs):
        try:
            self.types(*args, columns=names)
            self.describe(*args, names=names, include=include, datetime_is_numeric=datetime_is_numeric)
            self.sum(*args, names=names)
            self.sample(*args, names=names, n=n, **kwargs)
        except AttributeError:
            pass

    def groupby(self, ungrouped, grouped):
        self.debug(f'After grouping the table has {len(grouped)} reduced lines by '
                   f'{(1 - len(grouped)/len(ungrouped)):.0%}')


logging.setLoggerClass(Log)


def logged(ref_folder, folder_name='.dbLogs', separate_old=True, base_name=None):
    def some_decorator(cls):
        class NewCls(cls):
            logger = None

            @property
            def log(self):
                if self.__class__.logger is None:
                    name = base_name or self.name or self.__class__.__name__
                    # name = sel1f.__class__.__name__ if base_name is None else base_name
                    logger_reference = __name__ + '.' + name
                    log_folder = self.__getattribute__(ref_folder).new(folder_name)
                    # log_folder = self.output.new(folder_name)
                    logger = logging.getLogger(logger_reference)
                    date_str = str(datetime.datetime.now()).replace('.', '').replace(':', '-')
                    log_file = os.path.join(log_folder.path,
                                            name + ' - ' + date_str + '.log')
                    hand = logging.FileHandler(log_file)
                    hand.setLevel(logging.DEBUG)
                    formatter = logging.Formatter(f'%(asctime)s\t%(name)s\t%(levelname)s\t\n%(message)s\n')
                    hand.setFormatter(formatter)

                    class NoParsingFilter(logging.Filter):
                        def filter(self, record):
                            return record.name == logger_reference

                    hand.addFilter(NoParsingFilter())
                    logger.setLevel(logging.DEBUG)
                    # print to file
                    logger.addHandler(hand)
                    # print to console
                    # logger.addHandler(logging.StreamHandler())
                    self.__class__.logger = logger

                    if separate_old:
                        old = log_folder.new('.Z_Rascunhos')
                        for log in log_folder.files:
                            if name + ' - ' in log or self.name + ' - ' in log:
                                try:
                                    log_folder.move(old, objs=log)
                                except PermissionError:
                                    pass

                return self.__class__.logger
        return NewCls
    return some_decorator


