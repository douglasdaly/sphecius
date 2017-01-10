# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 18:45:33 2017

@author: doug
"""

#
#   Imports
#


#
#   Class
#

class English(object):
    """Plain English Letter Class"""
    
    def __init__(self):
        """Default Constructor"""
        self.__alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    
    def get_alphabet(self):
        """Gets this Translators alphabet"""
        return self.__alphabet