# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 17:49:00 2017

@author: doug
"""

#
#   Imports
#
from ..alphabets import English

#
#   Classes
#


class Cipher(object):
    """Base Cipher Class"""

    def __init__(self, alphabet=English):
        """Default/Abstract Constructor"""
        self._alphabet = alphabet
        self._key = None

    def set_key(self, key):
        """Sets the Key for this Cipher object"""
        self._key = key.upper()

    def encrypt(self, plaintext):
        """Abstract Encrypt Method"""
        pass

    def decrypt(self, ciphertext):
        """Abstract Decrypt Method"""
        pass

