# -*- coding: utf-8 -*-
"""
columnar.py

    Columnar Transposition Cipher

@author: Doug Daly
@date: 4/8/2017
"""

#
#   Imports
#
from .base import Cipher
from .. import string_helpers


#
#   Class
#

class Columnar(Cipher):
    """
    Columnar Transposition Cipher Class
    """

    def __init__(self, transpose_width, axis=1):
        """Default Constructor

        :param int transpose_width: Width to restrict rows/columns to
        :param int axis: Axis to build along (0 for Rows, 1 for Columns; Default is 1)

        """
        self._transpose_width = transpose_width
        self._axis = axis

