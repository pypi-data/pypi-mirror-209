import os
import shutil
from ..beta import fileleaf as fl
import zipfile
import ntpath
import datetime
from .navigator import Navigator
from .file import File
import logging
from ..log import logged
import pandas as pd

log = logging.getLogger('MagicRoot.databranch.os.folder')


class Folder(Navigator):
    logger = None

    def __init__(self, path):
        super().__init__(path)

    def log(self, msg=None):
        if Folder.logger is None:
            self._new('.dbLogs')
            self._new(os.path.join('.dbLogs', '.controls'))
            logger = logging.getLogger('MagicRoot.databranch.os.folder.folder_manipulation')
            date_str = str(datetime.datetime.now()).replace('.', '').replace(':', '-')
            log_file = os.path.join(self.path, '.dbLogs', '.controls', date_str + ' - folder manipulation.log')
            hand = logging.FileHandler(log_file)
            hand.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s')
            hand.setFormatter(formatter)

            class NoParsingFilter(logging.Filter):
                def filter(self, record):
                    return record.name == 'MagicRoot.databranch.os.folder.folder_manipulation'

            hand.addFilter(NoParsingFilter())
            logger.setLevel(logging.DEBUG)
            logger.addHandler(hand)
            Folder.logger = logger

        Folder.logger.debug(msg)

    def new(self, folder=None, file=None, with_obj=None, *args, **kwargs):
        """
        Shorthand for new_file and new_folder
        :param folder:
        :param file:
        :param with_obj:
        :param args:
        :param kwargs:
        :return:
        """
        if folder is not None:
            self.new_folder(folder)
            return Folder(os.path.join(self.path, folder))
        if file is not None:
            self.new_file(file, with_obj, *args, **kwargs)

    def append_to(
            self, file=None, with_obj=None,
            drop_duplicates=False, exact_match=True, *args, **kwargs):
        """
        Appends object to file, or creates it if it does not exist
        by default uses exact match to avoid unexpected appends
        """
        try:
            df = self.get(file=file, exact_match=exact_match, *args, **kwargs)
        except FileNotFoundError:
            df = pd.DataFrame()
        if isinstance(with_obj, dict):
            with_obj = pd.DataFrame(with_obj)
        df = pd.concat([df, with_obj])
        if drop_duplicates:
            df = df.drop_duplicates()
        self.new(file=file, with_obj=df)

    def new_file(self, name, obj, *args, **kwargs):
        self.log(f'Creating new file \'{name}\'')
        new_file = os.path.join(self.path, name)
        File(new_file).save(obj, *args, **kwargs)
        self.log(f'Successfully created new file \'{name}\'')

    def new_folder(self, name):
        self.log(f'Creating new folder \'{name}\'')
        self._new(name)
        self.log(f'Successfully created new folder \'{name}\'')
        return Folder(os.path.join(self.path, name))

    def _new(self, name):
        new_folder = os.path.join(self.path, name)
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)

    def clear(self):
        for obj in self.contents:
            self.remove(obj)

    def remove(self, name):
        self.log(f'Removing \'{name}\'')
        folder = os.path.join(self.path, name)
        if os.path.isdir(folder):
            shutil.rmtree(folder)
        if os.path.isfile(folder):
            os.remove(folder)
        self.log(f'Successfully removed \'{name}\'')

    def search(self, *args, **kwargs):
        return Folder(super().search(*args, **kwargs).path)

    def get(self, file, exact_match=False, *args, **kwargs):
        log.debug(f'Retriving \'{file}\' from \'{self.path}\'')
        file_path = os.path.join(self.path, file) if exact_match else os.path.join(self.search(file).path)
        return File(file_path).read(*args, **kwargs)

    def get_items(self, dic, *args, **kwargs):
        """
        Reads the inputs with the names given as keys in the \'dic\' parameter and returns a dictionary
        with the same keys and the retrived objects as values
        """
        return {
            arg: self.get(file_name, *args, **kwargs)
            for arg, file_name in dic.items()
        }

    def copy(self, to, objs=None, with_new_extension=None):
        objs = objs if objs is not None else self.files
        objs = objs if isinstance(objs, list) else [objs]
        for obj in objs:
            obj = File(self.search(obj).path)
            file_name = obj.tail
            if with_new_extension:
                file_name = File(obj.path).change(extension=with_new_extension).tail
            to.new_file(file_name, obj)

    def move(self, to, objs=None, with_new_extension=None):
        objs = objs if objs is not None else self.files
        objs = objs if isinstance(objs, list) else [objs]
        for obj in objs:
            obj = File(self.search(obj).path)
            file_name = obj.tail
            file_name_new = file_name
            if with_new_extension:
                file_name_new = File(obj.path).change(extension=with_new_extension).tail
            to.new_file(file_name_new, obj)
            self.remove(file_name)

    def unzip(self, to=None, objs=None):
        """
        Unzips a file (.zip) to the given folder
        :param to: folder to which to unzip the files
        :param objs:
        :return: None
        """
        objs = objs if objs is not None else self.files_with(extension='.zip')
        print(objs)
        objs = objs if isinstance(objs, list) else [objs]
        to = to if to is not None else self

        for zip in objs:
            zip_path = os.path.join(self.path, zip)
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(to.path)

    def groupby(self, file_name=None):
        """
        Group files in subfolder using a mapping function
        :return:
        """
        grouping_func = file_name
        for file_name in self.files:
            groups = grouping_func(file_name)
            for group in groups:
                group_folder = self.new_folder(group)
                self.move(to=group_folder, objs=file_name)

    @property
    def folders(self):
        return [Folder(os.path.join(self.path, f)) for f in self.directories]


# @logged(ref_folder='ref_folder', base_name='folder_manipulation')
# class Folder(UnloggedFolder):
#     @property
#     def ref_folder(self):
#         return UnloggedFolder(self.path)
#     pass


home = Folder(os.path.expanduser('~'))
