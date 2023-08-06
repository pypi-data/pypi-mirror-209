from datetime import datetime as dt


def function(func):
    """
    Decorator to time functions
    :param func: function to time execution
    :return: Decorated function
    """
    def wrapper(*args, **kwargs):
        t = Timer()
        rv = func(*args, **kwargs)
        print(f'\nMagicRoot - time_function: Function {func.__name__} took {t.lap()} to run')
        return rv

    return wrapper


class Timer:
    def __init__(self):
        self.begin_time = dt.now()
        self.end_time = None

    def restart(self):
        self.begin_time = dt.now()

    def lap(self):
        self.end_time = dt.now() - self.begin_time
        return self.end_time
