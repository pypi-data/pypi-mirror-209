from openpyxl import load_workbook
import pandas as pd
# from .. import pd
from .parcer_base import Parser, JSON
import logging
import shutil

log = logging.getLogger('MagicRoot.databranch.os.parcers')


class CSV(Parser):
    extension = 'csv'

    def read(self, *args, **kwargs):
        return pd.read_csv(filepath_or_buffer=self.path, *args, **self.read_settings(**kwargs))

    def save(self, obj, *args, **kwargs):
        obj.to_csv(path_or_buf=self.path, *args, **self.save_settings(**kwargs))

    def peak(self, *args, **kwargs):
        return self.read(nrows=5, *args, **kwargs).__repr__()


class Zip(Parser):
    extension = 'zip'

    def read(self, *args, **kwargs):
        return pd.read_csv(filepath_or_buffer=self.path, *args, **self.read_settings(**kwargs))

    def save(self, obj, *args, **kwargs):
        obj.to_csv(path_or_buf=self.path, *args, **self.save_settings(**kwargs))

    def peak(self, *args, **kwargs):
        return self.read(nrows=5, *args, **kwargs).__repr__()


class Feather(Parser):
    extension = 'ftr'

    def read(self, *args, **kwargs):
        return pd.read_feather(path=self.path, *args, **self.read_settings(**kwargs))

    def save(self, obj, *args, **kwargs):
        obj.reset_index(drop=True).to_feather(path=self.path, *args, **self.save_settings(**kwargs))

    def peak(self, *args, **kwargs):
        return self.read(nrows=5, *args, **kwargs).__repr__()


class SAS(Parser):
    extension = 'sas7bdat'

    def read(self, *args, **kwargs):
        return pd.read_sas(filepath_or_buffer=self.path, *args, **self.read_settings(**kwargs))

    def save(self, obj, *args, **kwargs):
        raise NotImplementedError('It is not possible to save sas files')

    def peak(self, *args, **kwargs):
        return self.read(encoding='latin-1', *args, **kwargs).__repr__()


class Excel(Parser):
    extension = 'xlsx'

    def read(self, *args, **kwargs):
        return pd.read_excel(io=self.path, *args, **self.read_settings(**kwargs))

    def save(self, obj, *args, **kwargs):
        """
        book = load_workbook(self.path)
        writer = pd.ExcelWriter(self.path, engine='openpyxl')
        writer.book = book

        ## ExcelWriter for some reason uses writer.sheets to access the sheet.
        ## If you leave it empty it will not know that sheet Main is already there
        ## and will create a new sheet.

        writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

        obj.to_excel(writer, *args, **kwargs)

        writer.save()
        """
        if isinstance(obj, dict):
            with pd.ExcelWriter(self.path) as writer:
                for sheet_name, df in obj.items():
                   df.to_excel(writer, sheet_name=sheet_name, index=False, freeze_panes=(1, 1), *args, **self.save_settings(**kwargs))
        else:
            obj.to_excel(excel_writer=self.path, index=False, freeze_panes=(1, 1), *args, **self.save_settings(**kwargs))
        # raise NotImplementedError('It is not possible to save excel files')

    def peak(self, *args, **kwargs):
        return self.read(encoding='latin-1', *args, **kwargs).__repr__()


class Text(Parser):
    extension = 'txt'

    def read(self, *args, **kwargs):
        return open(self.path, *args, **kwargs)

    def save(self, obj, *args, **kwargs):
        """
        if obj is not None:
            self.read().write(obj)
        """
        try:
            shutil.copyfile(obj.path, self.path)
        except shutil.SameFileError:
            pass
        # raise NotImplementedError('To save to text files read with \'w\'')

    def peak(self, *args, **kwargs):
        return self.read(encoding='latin-1', *args, **kwargs).__repr__()


class ParquetHDFS(Parser):
    extension = 'h5'

    def read(self, *args, **kwargs):
        return pd.read_hdf(filepath_or_buffer=self.path, *args, **self.read_settings(**kwargs))

    def save(self, obj, *args, **kwargs):
        raise NotImplementedError('It is not possible to save parquet HDFS files at this stage')

    def peak(self, *args, **kwargs):
        return self.read(nrows=5, *args, **kwargs).__repr__()


class Parquet(Parser):
    extension = 'parquet'

    def read(self, *args, **kwargs):
        return pd.read_parquet(path=self.path, *args, **self.read_settings(**kwargs))

    def save(self, obj, *args, **kwargs):
        obj.reset_index(drop=True).to_parquet(path=self.path, *args, **self.save_settings(**kwargs))

    def peak(self, *args, **kwargs):
        return self.read(nrows=5, *args, **kwargs).__repr__()


DEFINED_PARCERS = [CSV, Zip, Feather, SAS, Excel, Text, ParquetHDFS, Parquet]
