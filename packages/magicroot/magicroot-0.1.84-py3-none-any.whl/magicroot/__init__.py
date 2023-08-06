"""
Jack of all trades... you know the rest
"""
# modules
from . import os  # to deal with folders and files
from . import df  # operations on pandas Series and Dataframes
from . import fs  # useful functions for financial services
from . import plan  # project management _tools
from . import time  # time function executions
from . import cls  # to deal with attributes of classes
from . import telegram

from . import cp  # compoment structure (lib code)
from . import _beta  # non production code, tests

from .db import Table
from .db import Table as CompleteTable  # Base class for building tables

from . import settings

# global variables
import pandas
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

pandas.options.display.float_format = '{:,.2f}'.format
# pandas.options.display.date_format = '%Y-%m-%d'
