
class TableImplementationError(NotImplementedError):
    """
    Raised when subclasses of mr.db.Table are not correctly implemented
    """
    pass


class TableFormmatingValueError(ValueError):
    """
    Raised when errors in formmating are raised
    """
    pass


class DiscountValueError(ValueError):
    """
    Raised when subclasses of mr.db.Table are not correctly implemented
    """
    pass

class DiscountTypeError(TypeError):
    """
    Raised when arguments given to mr.fs.disc.Curve do not have the correct typing
    """
    pass


