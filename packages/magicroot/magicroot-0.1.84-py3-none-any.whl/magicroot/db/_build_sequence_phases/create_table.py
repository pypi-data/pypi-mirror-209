from ...attach import attachment
from ..utils import TableAttachmentProtocol
from .. import df
from ... import errors
import pandas


@attachment
class FreestyleCreate(TableAttachmentProtocol):

    def run(self, on, *args, **kwargs):
        df = self.create_error_handling(on, *args, **kwargs)
        if self._instance.constant_columns:
            df = self._instance.add_constant_columns(df)
        self.output = df
        return {'create_table_result': df}

    def create_error_handling(self, on, *args, **kwargs):
        try:
            rv = self._instance.create(*args, **kwargs, **on)
            if isinstance(rv, pandas.DataFrame) or isinstance(rv, dict):
                return rv
            raise errors.TableImplementationError(
                f'\'create\' function in \'{self._instance.__class__.__name__}\''
                f' should return a pandas.Dataframe or a dict'
            )
        except ValueError as e:
            if 'If you wish to proceed you should use pd.concat' in str(e):
                msg = f'You are trying to join columns of different types, ' \
                      f'Check if you are performing a join based on the columns below: ' \
                      f'\n {df.types.different(**on)}'
                raise ValueError(msg)
            elif 'cannot reindex on an axis with duplicate labels' in str(e):
                msg = f'Probably one of the columns in the process ends with more than one column with the same name'
                raise ValueError(msg)
            elif 'Index contains duplicate entries, cannot reshape' in str(e):
                msg = f'Probably tried to use \'pd.Dataframe.pivot\' with index with duplicate entries'
                raise ValueError(msg)
            else:
                raise e





