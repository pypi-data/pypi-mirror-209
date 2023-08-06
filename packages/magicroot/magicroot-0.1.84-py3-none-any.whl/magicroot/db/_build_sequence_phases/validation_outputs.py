from warnings import warn
from functools import cached_property

import pandas as pd
import warnings
from ...attach import attachment
from ..utils import TableAttachmentProtocol, TableImplementationError
import datetime


@attachment
class ValidateOutputs(TableAttachmentProtocol):

    def run(self, on, release_to=None, *args, **kwargs):
        try:
            try:
                self.basic_validation(on)
            except AttributeError:
                pass
            self.validate(on, *args, **kwargs)
        except AssertionError:
            self.log.exception('Got an exception')
            warnings.warn(f"Table {self.__class__.__name__} failed validation please check the .log for "
                          f"more details")
        return {'_saved': on}

    def basic_validation(self, df):
        self.test_nulls(df)

        empty = df.count() == 0
        self.define_test(
            df=df,
            pass_test=~empty,
            description=f'that table is not empty',
            fail_msg='Output table is empty'
        )

        self.define_test(
            df=df,
            pass_test=empty | (len(df) == len(df.drop_duplicates())),
            description=f'that table does not have repeated rows',
            fail_msg=f'Output table has duplicated rows (total rows: {len(df)}, unique rows: {len(df.drop_duplicates())})'
        )

