from warnings import warn
from functools import cached_property
import inspect

import pandas as pd

from ...attach import attachment
from ..utils import TableAttachmentProtocol, TableImplementationError
from ... import cp
from ... import df
from ... import cls
from ... import dic


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
        accepted_attrs = ['inputs_dicionary', 'inputs_dictionary', 'table_inputs', 'load_inputs', 'i']
        defined_attrs = cls.defined(accepted_attrs, self._instance)
        print(f"\t\tDefined the following input attributes: {defined_attrs}")

        if len(defined_attrs) == 0:
            warn("\nDid not find a input method please define at least one of the following: "
                 "['load_inputs', 'table_inputs', 'inputs_dicionary', 'inputs_dictionary', 'i'] \n"
                 "Continuing assuming: i = ['input_file.xlsx']")
            return self.build_load_dic(['input_file.xlsx'])

        attrs = [getattr(self._instance, attr) for attr in defined_attrs]

        for i, a in enumerate(attrs):
            if callable(a):
                attrs[i] = a()
            if isinstance(a, str):
                attrs[i] = [a]

        inputs_dic = {k: self.treat_input_command(v) for d in attrs if isinstance(d, dict) for k, v in d.items()}
        inputs_list = [self.treat_input_command(v) for l in attrs if isinstance(l, list) for v in l]

        inputs = {}
        expected_inputs = cls.get_args('create', self._instance)
        for inp in expected_inputs:
            try:
                inputs[inp] = inputs_dic[inp]
            except (KeyError, TypeError):
                try:
                    inputs[inp] = inputs_list.pop(0)
                except IndexError:
                    pass

        x = {**{k: v for k, v in inputs.items() if isinstance(v, dict)}, **{k: 'loaded with mapping' for k, v in inputs.items() if isinstance(v, pd.DataFrame)}}
        print(f"\t\tLoading with the following dic: {x}")
        return inputs

    def treat_input_command(self, val):
        try:
            val = str(val.save_name)
        except AttributeError:
            pass
        if isinstance(val, str):
            val = {'file_name': val}
        return val

    def load_inputs(self, *args, **kwargs):
        dic, subsequent_arg, msg = {}, False, ''

        for arg, obj in self._transformed.items():
            if isinstance(obj, dict):
                dic[arg], result = cp.load_file(obj, self.input)

                if subsequent_arg:
                    msg = msg + f'\n'
                try:
                    cols = list(dic[arg].columns)
                except AttributeError:
                    cols = 'Unable to show cols'
                msg = msg + f'\t\tLoaded \'{arg}\' from {result.path}\n\t\t\t with columns: {cols}'
                subsequent_arg = True
            else:
                dic[arg] = obj

        self._instance.log.debug(msg)
        print(msg)
        return dic

    def run(self, *args, **kwargs):
        self.output = self.load_inputs()
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







