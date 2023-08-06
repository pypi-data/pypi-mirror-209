from warnings import warn
from functools import cached_property
from ... import cp
from ...os import home
import pandas as pd

from ...attach import attachment
from ..utils import TableAttachmentProtocol, TableImplementationError
import datetime


@attachment
class SavingOutputs(TableAttachmentProtocol):

    def run(self, on, release_to=None, *args, **kwargs):
        self.save(on)
        if release_to:
            self.release(on, release_to, *args, **kwargs)
        self.update_run_log(on, release_to)
        return {'_saved': on}

    def update_run_log(self, on, release_to):
        pass
        # folder = home[cp.Settings('cp', 'settings_config')['path']]
        # try:
        #     df = folder.get('run_log.csv', exact_match=True)
        # except FileNotFoundError:
        #     df = pd.DataFrame()
        # release_path = release_to.path if release_to else ''
        # try:
        #     n_col = len(on.columns)
        # except AttributeError:
        #     n_col = 0
        # df_new_line = pd.DataFrame({
        #     'datetime': [cp.Settings.exec_dt],
        #     'user': [self.output.user],
        #     'table': [self.name],
        #     'class': [self._instance.__class__.__name__],
        #     'output_extension': [self.default_extension],
        #     'output': [self.output.without_user],
        #     'input': [self.input.without_user],
        #     'released_to': [release_path],
        #     'release_extension': [self.release_extension],
        #     'rows': [len(on)],
        #     'columns': [n_col]
        # })
        # folder.new(file='run_log.csv', with_obj=pd.concat([df, df_new_line]), index=False)




