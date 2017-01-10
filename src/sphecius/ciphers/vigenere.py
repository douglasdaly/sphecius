# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 22:17:38 2017

@author: doug
"""

#
#   Imports
#


#
#   Class
#

class Vigenere(object):
    """Vigenere Cipher Class"""
    
    def __init__(self, alphabet):
        """Default Constructor"""
        self.__encryptor = self._build_encryptor(alphabet)
        self.__decryptor = self._build_decryptor(alphabet)
    
    
    def _build_encryptor(self, alphabet):
        """Builds the Encryption Lookup Table"""
        lAlphabet = len(alphabet)
        
        for i in range(lAlphabet):
            
        