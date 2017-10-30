# -*- coding: utf-8 -*-
"""
caesar.py

    Caesar cipher class

@author: Douglas Daly
@date: 1/7/2017
"""
#
#   Imports
#
from .. import string_helpers as sh
from .base import Cipher


#
#   Class
#

class Caesar(Cipher):
    """
    Caesar Cipher Class
    """
    
    def __init__(self, alphabet, shift=None):
        """ Default Constructor
        """
        super(Caesar, self).__init__(alphabet=alphabet)
        self.set_key(shift)

    def set_key(self, key):
        """ Sets the Key for this Caesar Cipher

        :param int key: Shift Amount for Caesar Cipher

        """
        if key is not None:
            self._set_shift(key)
        else:
            self._key = None

    def _set_shift(self, shift):
        """ Sets the shift for this Caesar cipher
        """
        self._key = shift

        if shift > 0:
            self.__shifted = sh.shift_forward(self._alphabet.get_alphabet(),
                                              shift)
        else:
            self.__shifted = sh.shift_backward(self._alphabet.get_alphabet(),
                                               -shift)

        self.__encryptor = dict(zip(self._alphabet.get_alphabet(),
                                    self.__shifted))
        self.__decryptor = dict(zip(self.__shifted,
                                    self._alphabet.get_alphabet()))

    def encrypt(self, plaintext):
        """
        Encrypts the given plaintext based on the set parameters of this
        class
        """
        if self._key is None:
            raise Exception("No valid key set!")

        plaintext = plaintext.upper()
        
        output = list()
        for letter in plaintext:
            if letter in self.__encryptor.keys():
                output.append(self.__encryptor[letter])
            else:
                output.append(letter)
        
        return output

    def decrypt(self, ciphertext):
        """
        Decrypts the given Ciphertext based on the set parameters of this
        class
        """
        if self._key is None:
            raise Exception("No valid key set!")

        ciphertext = ciphertext.upper()
        
        output = list()
        for letter in ciphertext:
            if letter in self.__decryptor.keys():
                output.append(self.__decryptor[letter])
            else:
                output.append(letter)
        
        return output
