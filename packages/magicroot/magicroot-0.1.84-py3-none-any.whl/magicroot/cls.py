import inspect

def attribute_selector(*attrs, instance, errors=AttributeError):
    """
    Tries to access a list of attributes and returns the first that exists

    :Parameters:
        *attrs : str
            names of attributes passed as strings
        instance : type
            any instance to perform the check on
        errors : tuple(errors), default AttributeError
            errors to catch

    :Returns:
        attrs
            The first attribute that does not raise a error

    :Raises:
        AttributeError
            if non of the attributes exist

    """
    for attr in attrs:
        try:
            return getattr(instance, attr)
        except errors:
            pass
    raise errors[0] if isinstance(errors, tuple) else errors


def defined(attrs, instance):
    """
    Returns the list of defined attributes and methods in the expected ``attrs`` list.

    :Parameters:
        attrs : list
            list of expected attributes
        instance : type
            any instance to perform the check on


    :Returns:
        list
            subset of attrs that are defined
    """
    return [attr for attr in attrs if attr in dir(instance)]


def get_args(method, instance):
    """
    Returns the list of defined arguments of a method in ``instance``.

    :Parameters:
        method : str
            method to get the arguments of
        instance : type
            any instance to perform the check on

    :Returns:
        list
            list of arguements
    """
    return inspect.getfullargspec(getattr(instance, method))[0][1:]


def all_exist(*attrs, instance, errors=AttributeError):
    """
    Checks if a class as a list of attributes

    :Parameters:
        *attrs : str
            names of attributes passed as strings
        instance : type
            any instance to perform the check on
        errors : tuple(errors), default AttributeError
            errors to catch

    :Returns:
        bool
            True if all exist, False otherwise

    """
    all_ex = True
    for attr in attrs:
        try:
            _ = getattr(instance, attr)
        except errors:
            all_ex = False
    return all_ex


def to_list(*args):
    """
    Returns the elements as a list with a single element, if it already a list 
    returns without change

    :Parameters:
        agr : any
            argument to place in list

    :Returns:
        list
            arg if arg is a list, tuple or ``None``, [arg] otherwise
    """
    return tuple([
        arg if isinstance(arg, list) or isinstance(arg, tuple) or arg is None 
        else [arg] for arg in args
    ])


def from_list(arg):
    """
    Returns the first element of a list, if arg is not a list returns arg

    :Parameters:
        agr : list
            argument or list from which to take the first element

    :Returns:
        any
            arg[0] if arg is list or tuple, arg otherwise
    """
    return arg[0] if isinstance(arg, list) or isinstance(arg, tuple) else arg


