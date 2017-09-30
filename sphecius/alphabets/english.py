# -*- coding: utf-8 -*-
"""
english.py

    English Alphabet Class

@author: Douglas Daly
@date: 1/9/2017
"""
#
#   Imports
#
import string

from .base import Alphabet


#
#   Class
#

class English(Alphabet):
    """Plain English Letter Class"""
    
    def __init__(self):
        """ Default Constructor
        """
        self._alphabet = string.ascii_uppercase
