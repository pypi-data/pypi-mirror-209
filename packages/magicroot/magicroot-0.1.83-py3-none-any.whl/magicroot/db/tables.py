import re

from .. import os as mros
from ..log import *
from .utils import TableImplementationError


class ConstructTable:
    pass


class IOTable(ConstructTable):
    pass


class Table(IOTable):
    pass


class BuildSequenceProperties(Table):
    pass


class BuildSequenceFunctions(BuildSequenceProperties):
    pass


class BuildSequenceTests(BuildSequenceFunctions):
    pass



