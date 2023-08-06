import re

from .. import os as mros
from ..log import *
from .utils import TableImplementationError


class ConstructTable:
    pass


class IOTable(ConstructTable):
    pass


class BuildSequenceProperties(IOTable):
    pass


class BuildSequenceFunctions(BuildSequenceProperties):
    pass


class BuildSequenceTests(BuildSequenceFunctions):
    pass



