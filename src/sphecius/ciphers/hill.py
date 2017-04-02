# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 22:19:59 2017

@author: doug
"""

#
#   Imports
#
from .. import string_helpers as sh
from .base import Cipher

import numpy as np

#
#   Class
#

class Hill(Cipher):
    """Hill Cipher Class"""

    def __init__(self, alphabet, key_matrix):
        """Default Constructor"""
        super(Hill, self).__init__(alphabet=alphabet)
        self.set_key(key=key_matrix)

    def set_key(self, key):
        """Sets the Key Matrix for this Cipher"""
        if self.__valid_hill_key(key):
            self._key = key
        else:
            raise Exception('Invalid (non-invertible) Key given!')

    def encrypt(self, plaintext):
        """Hill Cipher Encryption"""

    def decrypt(self, ciphertext):
        """Hill Cipher Decryption"""
        decrypt_key = np.linalg.inv(self._key)

    def __run_algorithm(self, text, key, padding=None):
        """

        :param str text:
        :param numpy.matrix key:

        :return: Resulting Text from Hill Algorithm
        :rtype: str

        """
        # - Clean the Text
        text = sh.remove_punctuation(text)

        # - Get Parameters Needed
        text_mat = sh.convert_text_to_matrix_2d(text, axis_size=key.shape[0], axis=1, padding=padding)
        v_a2i = np.vectorize(self._alphabet.a2i)
        num_mat = v_a2i(text_mat)

        mod_z = self._alphabet.size



    def __valid_hill_key(self, key):
        """Checks if the given Key Matrix is valid

        :param numpy.matrix key: Key Matrix to Check

        :return: Whether or not the key matrix given is valid for decryption
        :rtype: bool

        """
        sz_tup = key.shape
        if len(sz_tup) != 2:
            return False
        else:
            if sz_tup[0] != sz_tup[1]:
                return False

        try:
            np.linalg.inv(key)
            return True
        except np.linalg.LinAlgError:
            return False
