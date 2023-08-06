from ...attach import attachment
from ..utils import TableAttachmentProtocol, TableImplementationError
from .. import df


class CreateFunctionError(TableImplementationError):
    pass


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
            return self._instance.create(*args, **kwargs, **on)
        except ValueError as e:
            if 'If you wish to proceed you should use pd.concat' in str(e):
                msg = f'You are trying to join columns of different types, ' \
                      f'Check if you are performing a join based on the columns below: ' \
                      f'\n {df.types.different(**on)}'
                raise CreateFunctionError(msg)
            else:
                raise e





