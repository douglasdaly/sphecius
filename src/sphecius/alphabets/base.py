# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 17:39:41 2017

@author: doug
"""

#
#   Imports
#


#
#   Class
#

class Alphabet(object):
    """Base Alphabet Class"""
    
    def __init__(self):
        """Base Default Constructor"""
        self._alphabet = None
    
    
    def get_alphabet(self):
        """Abstract get Alphabet Method"""
        return self._alphabet

    
    def i2a(self, index):
        """Base get Letter at Index Method"""
        return self._alphabet[index]
    
    
    def a2i(self, letter):
        """Base get Index of Letter Method"""
        return self._alphabet.find(letter.upper())