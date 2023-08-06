
# modules
from . import beta  # old and new code
from . import cp  # compoment structure (lib code)
from . import df  # operations on pandas Series and Dataframes
from . import fs  # useful functions for financial services
from . import os  # to deal with folders and files
from . import time  # time executions
from . import plan  # project management tools
from .db import CompleteTable
from .db import CompleteTable as Table  # Base class for building tables

from . import settings
from Modelo_de_Dados_Lusitania.src.modelo_de_dados.base._modules.magicroot.pd.dataframe import DataFrame

# global variables
import pandas
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

pandas.options.display.float_format = '{:,.2f}'.format
