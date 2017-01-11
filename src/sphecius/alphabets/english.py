# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 18:45:33 2017

@author: doug
"""

#
#   Imports
#
from sphecius.alphabets.base import Alphabet

#
#   Class
#

class English(Alphabet):
    """Plain English Letter Class"""
    
    def __init__(self):
        """Default Constructor"""
        self._alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"