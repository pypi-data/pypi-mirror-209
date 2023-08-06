import inspect
import datetime
import inspect


class Component:
    """
    All Components have a __call__ that receives only *args and returns only *args so order of args is relevant

    The __init__ of components may be use **kwargs for internal use of each Component, *args are used for defining
    default
    """

    def __init__(self, *args, parent=None, **kwargs):
        self.parent = parent
        if kwargs:
            func = self.run
            self.run = lambda *args, **other: func(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        return self.run(*args, **kwargs)

    def __mul__(self, other):
        func = self.run
        self.run = lambda agrlist, *args, **kwargs: [func(arg, *args, **kwargs) for arg in agrlist]
        return self

    def __pow__(self, other):
        # newComp = self >> other
        func = (self >> other).run
        # self.run = lambda agrdic, *args, **kwargs: {key: func(arg, *args, **kwargs) for key, arg in agrdic.items()}
        print('test')

        def run(agrdic, *args):
            dic = {}
            for key, value in agrdic.items():
                dic[key] = func(value)
            return dic, *args

        self.run = run
        return self

    def __rmul__(self, other):
        func = self.run
        self.run = lambda agrlist, *args, **kwargs: [func(arg, *args, **kwargs) for arg in agrlist]
        return self

    def __rshift__(self, other):
        func = self.run
        self.run = lambda *args, **kwargs: other(func(*args, **kwargs))
        return self

    def __rrshift__(self, other):
        self.__call__ = lambda *args: self(*args, *[arg for arg in other if arg is not None])
        return self

    def __and__(self, other):
        a = self
        if isinstance(other, Component):
            class NewComp(Component):
                def __call__(self, *args):
                    rv_a = a(*args)
                    if isinstance(rv_a, tuple):
                        return *a(*args), other(*args)
                    return a(*args), other(*args)
        else:
            class NewComp(Component):
                def __call__(self, *args):
                    rv_a = a(*args)
                    if isinstance(rv_a, tuple):
                        return *a(*args), other
                    return a(*args), other
        return NewComp()

    def __rand__(self, other):
        a = self
        if isinstance(other, list):
            class NewComp(list):
                def __call__(self, *args):
                    return other + a(*args)

            return NewComp()

    def run(self, *args, **kwargs):
        return args

    def set_defaults(self, *args):
        print(inspect.getfullargspec(self.__call__))
        pass

    exec_dt = datetime.datetime.now()
