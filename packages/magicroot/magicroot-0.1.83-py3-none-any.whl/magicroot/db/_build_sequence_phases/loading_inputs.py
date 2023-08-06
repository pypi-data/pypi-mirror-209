from warnings import warn
from functools import cached_property
import inspect
from ..tables import BuildSequenceProperties
from ...attach import attachment
from ..utils import TableAttachmentProtocol, TableImplementationError
from ... import cp


@attachment
class AggInputs(TableAttachmentProtocol):
    """
    Defined as a dictionary of the form
    >>> table_inputs = {\'alias\': {\'file_name\': \'some_file_name.csv\', \'config_name\':\'config\'}}
        or
    >>> table_inputs = {\'alias\': \'some_file_name.csv\'}
        or
    >>> table_inputs = {\'alias\': SomeOtherTable()}
    """
    @property
    def _transformed(self):
        intance_treatment = {
            BuildSequenceProperties: lambda v: str(v.save_name),
            str: lambda v: {'file_name': v}
        }

        input_dic = \
            cp.AttributeSelector() \
            >> cp.ToDic(func=self._instance.create) \
            # ** cp.ApplyBasedOnType(funcs=intance_treatment)
        agg = input_dic('table_inputs', 'inputs_dicionary', 'inputs_dictionary', 'i', instance=self._instance)
        x = cp.ApplyBasedOnType(funcs=intance_treatment)
        dic = {}
        for key, value in agg.items():
            dic[key] = x(value)
        return dic

    def load_inputs(self, *args, **kwargs):
        dic, subsequent_arg, msg = {}, False, ''

        for arg, obj in self._transformed.items():
            dic[arg], result = cp.load_file(obj, self.input)

            if subsequent_arg:
                msg = msg + f'\n'
            try:
                cols = list(dic[arg].columns)
            except AttributeError:
                cols = 'Unable to show cols'
            msg = msg + f'\t\tLoaded \'{arg}\' from {result.path}\n\t\t\t with columns: {cols}'
            subsequent_arg = True

        self._instance.log.debug(msg)
        print(msg)
        return dic

    def run(self, *args, **kwargs):
        try:  # tries to run overwritten load inputs
            self.output = self._instance.load_inputs()
            print('\t\tLoaded with \'load_inputs\'')
        except AttributeError:  # if not defined creates it own load inputs
            self.output = self.load_inputs()
            print('\t\tLoaded with \'Load dic\'')
        return self.output


@attachment
class SimplifiedInputs(TableAttachmentProtocol):
    """
    Defined as a dictionary of the form
    >>> table_inputs = {\'alias\': {\'file_name\': \'some_file_name.csv\', \'config_name\':\'config\'}}
        or
    >>> table_inputs = {\'alias\': \'some_file_name.csv\'}
        or
    >>> table_inputs = {\'alias\': SomeOtherTable()}
    """

    def run(self, *args, **kwargs):
        try:
            self.output = self._instance.load_inputs()
        except AttributeError:
            self.output = self.load_inputs()
        return self.output

    @property
    def _table_inputs(self):
        try:
            return self._instance.table_inputs
        except AttributeError:
            pass

        try:
            return self._instance.inputs_dicionary
        except AttributeError:
            pass

        try:
            return self._instance.i
        except AttributeError:
            pass


    @property
    def inputs_dic(self):
        dic = {}
        for key, value in self._table_inputs.items():
            if isinstance(value, BuildSequenceProperties):
                value = str(value.save_name)
            if isinstance(value, str):
                value = {'file_name': value}
            dic[key] = value
        return dic

    def load_inputs(self, *args, **kwargs):
        dic, subsequent_arg, msg = {}, False, ''

        for arg, obj in self.inputs_dic.items():
            file_name = obj['file_name']
            file_agrs = {key: value for key, value in obj.items() if key != 'file_name'}
            dic[arg] = self.input.get(file_name, *args, **kwargs, **file_agrs)
            result = self.input.search(file_name)
            if subsequent_arg:
                msg = msg + f'\n'
            msg = msg + f'\t\tLoaded \'{arg}\' from {result.path}\n\t\t\t with columns: {list(dic[arg].columns)}'
            subsequent_arg = True

        self._instance.log.debug(msg)
        print(msg)
        return dic







