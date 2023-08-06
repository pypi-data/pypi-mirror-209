"""
Advanced use, probably only useful for internal use
"""


def attachment(cls):
    """
    Class decorator that creates descriptors to attach to classes.

    Allows making classes modular

    :param cls: Class to make into an attachment
    :return: An attachment to a class (Descriptor)
    """
    class Attachment(object):
        def __set_name__(self, owner, name):
            self.public_name = name
            self.private_name = '_' + name

        def __get__(self, obj, objtype=None):
            try:
                return getattr(obj, self.private_name)
            except AttributeError:
                attach = self.Attach(obj)
                setattr(obj, self.private_name, attach)
                return attach

        class Attach(cls, object):
            def __init__(self, instance, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self._instance = instance

            def __getattr__(self, item):
                try:
                    return getattr(cls, item)
                except AttributeError:
                    return getattr(self._instance, item)

        Attach.__name__ = cls.__name__
    return Attachment
