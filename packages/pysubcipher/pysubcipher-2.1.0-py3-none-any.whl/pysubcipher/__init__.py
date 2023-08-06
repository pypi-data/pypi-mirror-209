"""
PySubCipher allows you to encode and decode strings of text using a substitution cipher algorithm.

:copyright: (c) 2023-present mxngo
:license: MIT, see LICENSE for more details.
"""

__title__ = "pysubcipher"
__author__ = "mxngo"
__copyright__ = ":copyright: (c) 2023-present mxngo"
__license__ = "MIT"

import string
from typing import Final

from .pysubcipher import *

BASE_2: Final[str] = "01"
HEXDIGITS: Final[str] = string.hexdigits
OCTDIGITS: Final[str] = string.octdigits
ALPHANUMERIC: Final[str] = string.printable