import inspect


class SM:
    def start(self):
        self.state = self.startState

    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        return o

    def transduce(self, inputs):
        self.start()
        return [self.step(inp) for inp in inputs]


class Component:
    """
    All Components have a __call__ that receives only *args and returns only *args so order of args is relevant

    The __init__ of components may be use **kwargs for internal use of each Component, *args are used for defining
    default
    """
    def __init__(self, *args, parent=None, **kwargs):
        self.parent = parent

    def __call__(self, *args):
        return args

    def __mul__(self, other):
        if isinstance(other, list):
            return [self(inp) for inp in other]
        raise NotImplemented

    def __rmul__(self, other):
        a = self

        class NewComp(Component):
            def __call__(self, *args):
                return [a(arg) for arg in other(*args)]
        return NewComp()

    def __rshift__(self, other):
        a = self

        class NewComp(Component):
            def __call__(self, *args):
                return other(a(*args))
        return NewComp()

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

    def set_defaults(self, *args):
        print(inspect.getfullargspec(self.__call__))

        pass


class Consecutive(Component):
    def __init__(self, components, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.components = components
        for component in components:
            component.parent = self

    def __call__(self, *args):
        args = args if len(args) > 1 else args[0]
        for component in self.components:
            args = component(args)
        return args


class X(Component):
    i = {}
    a = 0
    h = 'did it work?'

    def __call__(self, a):
        self.a += a
        print(f'testing af: {self.a}')
        return self.a


class CheckAttribute(Component):
    def __call__(self, component, *attrs):
        for attr in attrs:
            try:
                return getattr(component, attr)
            except AttributeError:
                pass


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


class CoaValidation:
    i = {

    }

    __call__ = (((CheckAttribute() >> LoadDic()) & LoadDic()) >> LoadFromDic()).__call__




# LoadInputs = (CheckAttribute() >> LoadDic()) & CoA & ''

# print(LoadInputs(CoaValidation, 'table_inputs', 'inputs_dicionary', 'inputs_dictionary', 'i', 'h'))


class NoDefault:
    pass


class LoadFromDic(LoadFromDic):
    def __call__(self, arg1, arg2=CoA, arg3=''):
        return super().__call__(arg1, arg2, arg3)


loadinputs = CheckAttribute() >> LoadDic() >> LoadFromDic().set_defaults(None, CoA, '')
# 0 >> arg, certo >> lista passas para dic >>
print(loadinputs(CoaValidation, 'table_inputs', 'inputs_dicionary', 'inputs_dictionary', 'i', 'h'))

x = X()

x(1)
print('--------------')
y = x >> x
y(1)
print('--------------')
y = CheckAttribute()
print(y(x, 'table_inputs', 'inputs_dicionary', 'inputs_dictionary', 'i', 'h'))
