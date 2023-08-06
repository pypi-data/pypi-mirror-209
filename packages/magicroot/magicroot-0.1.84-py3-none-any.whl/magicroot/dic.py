from .cls import to_list
import inspect


def invert_explode(arg):
    mdic = {}
    for key, values in arg.items():
        values = to_list(values)
        for value in values:
            mdic[value] = key
    return mdic


def args(from_list, with_func):
    if not isinstance(from_list, dict):
        return {k: v for k, v in zip(inspect.getfullargspec(with_func)[0][1:], from_list)}
    return args
