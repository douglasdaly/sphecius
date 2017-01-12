# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 22:19:59 2017

@author: doug
"""

#
#   Imports
#
from .. import string_helpers as sh
from . import Cipher

#
#   Class
#


class Caesar(Cipher):
    """Caesar Cipher Class"""
    
    def __init__(self, alphabet, shift):
        """Default Constructor"""
        super(Caesar, self).__init__(alphabet=alphabet)
        self._set_shift(shift)

    def _set_shift(self, shift):
        """Sets the shift for this Caesar cipher"""
        self._shift = shift

        if shift > 0:
            self.__shifted = sh.shift_forward(self._alphabet, shift)
        else:
            self.__shifted = sh.shift_backward(self._alphabet, -shift)

        self.__encryptor = dict(zip(self._alphabet, self.__shifted))
        self.__decryptor = dict(zip(self.__shifted, self._alphabet))

    def encrypt(self, plaintext):
        """Encrypts the given plaintext based on the set parameters of this class"""
        plaintext = plaintext.upper()
        
        output = list()
        for letter in plaintext:
            if letter in self.__encryptor.keys():
                output.append(self.__encryptor[letter])
            else:
                output.append(letter)
        
        return output

    def decrypt(self, ciphertext):
        """Decrypts the given Ciphertext based on the set parameters of this class"""
        ciphertext = ciphertext.upper()
        
        output = list()
        for letter in ciphertext:
            if letter in self.__decryptor.keys():
                output.append(self.__decryptor[letter])
            else:
                output.append(letter)
        
        return output
