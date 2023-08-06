from ._component import Component
import inspect
import pandas as pd


class AttributeSelector(Component):
    def run(self, *attrs, instance, error=AttributeError):
        for attr in attrs:
            try:
                return getattr(instance, attr)
            except error:
                pass
        raise error


class ToDic(Component):
    def run(self, args, func):
        if not isinstance(args, dict):
            return {k: v for k, v in zip(inspect.getfullargspec(func)[0][1:], args)}
        return args


class ApplyBasedOnType(Component):
    def run(self, value, funcs):
        for cls, func in funcs.items():
            if isinstance(value, cls):
                value = func(value)
        return value


class LoadFile(Component):
    def run(self, instruc, folder, file_name='file_name', *args, **kwargs):
        fname = instruc[file_name]
        file_agrs = {key: value for key, value in instruc.items() if key != file_name}

        result = folder.search(fname)
        value = folder.get(result.path, *args, **kwargs, **file_agrs, exact_match=True)
        return value, result


load_file = LoadFile()


class Tolist(Component):
    def run(self, arg):
        return arg if isinstance(arg, list) else [arg]


to_list = Tolist()


class DicInvertExplode(Component):
    def run(self, arg):
        mdic = {}
        for key, values in arg.items():
            values = to_list(values)
            for value in values:
                mdic[value] = key
        return mdic


dic_invert_explode = DicInvertExplode()


class DicInvert(Component):
    def run(self, arg):
        return {value: key for key, value in arg.items()}


dic_invert = DicInvert()


class DicFilter(Component):
    def run(self, dic, keys):
        return {key: dic[key] for key in set(keys).intersection(set(dic.keys()))}


dic_filter = DicFilter()


class RenameCols(Component):
    def run(self, dic, df):
        return df.rename(columns=dic_filter(dic_invert_explode(dic), df.columns))


rename_cols = RenameCols()


class LoadDic(Component):
    def __call__(self, dic_input):
        dic = {}
        for key, value in dic_input.items():
            if isinstance(value, Component):
                value = str(value.save_name)
            if isinstance(value, str):
                value = {'file_name': value}
            dic[key] = value
        return dic


class LoadFromDic(Component):
    def __call__(self, dic_input, input_folder, log):
        dic, subsequent_arg, msg = {}, False, ''

        for arg, obj in dic_input.items():
            file_name = obj['file_name']
            file_agrs = {key: value for key, value in obj.items() if key != 'file_name'}
            dic[arg] = input_folder.get(file_name, **file_agrs)
            result = input_folder.search(file_name)
            if subsequent_arg:
                msg = msg + f'\n'
            msg = msg + f'\t\tLoaded \'{arg}\' from {result.path}\n\t\t\t with columns: {list(dic[arg].columns)}'
            subsequent_arg = True

        # log.debug(msg)
        print(msg)
        return dic


class InPlaceGroup(Component):
    def __init__(self, func, *args, **kwargs):
        super(InPlaceGroup, self).__init__(self, *args, **kwargs)
        self.func = func

    def __call__(self, *args, **kwargs):
        return self._base(*args, func=self.func, **kwargs)

    @staticmethod
    def _base(columns, by, func, *args, **kwargs):
        return lambda x: x[by].merge(
            x[by + [col for col in columns if col not in by]].groupby(by, *args, **kwargs).agg(func).reset_index(),
            how='left', on=by, validate='many_to_one'
        )[columns].set_index(x.index)


class IfsGroup(Component):
    def __init__(self, func, *args, **kwargs):
        super(IfsGroup, self).__init__(self, *args, **kwargs)
        self.func = func

    def __call__(self, *args, **kwargs):
        return self._base(*args, func=self.func, **kwargs)

    @staticmethod
    def _base(columns, by, func, *args, **kwargs):
        return lambda x: x[by].merge(
            x[by + [col for col in columns if col not in by]].groupby(by, *args, **kwargs).agg(func).reset_index(),
            how='left', on=by, validate='many_to_one'
        )[columns].set_index(x.index)


class Excel(Component):
    sumby = InPlaceGroup('sum').__call__
    countby = InPlaceGroup('count').__call__
    maxby = InPlaceGroup('max').__call__
    minby = InPlaceGroup('min').__call__

    vloookup = ''




