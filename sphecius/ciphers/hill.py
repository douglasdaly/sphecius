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
import sympy


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
            raise Exception('Invalid Key given!')

    def encrypt(self, plaintext, padding=None):
        """Hill Cipher Encryption"""
        return self.__run_algorithm(plaintext, self._key, padding=padding)

    def decrypt(self, ciphertext):
        """Hill Cipher Decryption"""
        decrypt_key = self.__get_finite_inverse(self._key)
        return self.__run_algorithm(ciphertext, decrypt_key)

    def __run_algorithm(self, text, key, padding=None):
        """Helper function to run Hill algorithm

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

        # - Encoding
        enc_mat = ((key * num_mat) % self._alphabet.size()) + 1

        # - Convert back to string
        v_i2a = np.vectorize(self._alphabet.i2a)
        text_mat = v_i2a(enc_mat)
        ret = sh.convert_matrix_to_text_2d(text_mat, axis=1)

        return sh.replace_stripped_text(text, ret)

    def __get_finite_inverse(self, key):
        """Gets the Inverse of the given Key over a Finite Set

        :param np.matrix key: Key Matrix to Invert

        :return: Inverse Matrix (if exists) otherwise None
        :rtype: np.matrix

        """
        try:
            inv_key = (np.matrix(sympy.Matrix(key).inv_mod(self._alphabet.size())) + 1).astype(int)
            return inv_key
        except sympy.NonSquareMatrixError:
            return None
        except sympy.ValueError:
            return None

    def __valid_hill_key(self, key):
        """Checks if the given Key Matrix is valid

        :param numpy.matrix key: Key Matrix to Check

        :return: Whether or not the key matrix given is valid for decryption
        :rtype: bool

        """
        # - Check the Shape
        sz_tup = key.shape
        if len(sz_tup) != 2:
            return False
        else:
            if sz_tup[0] != sz_tup[1]:
                return False

        # - Check Even/Odd Criteria
        for iAx in range(2):
            t = np.sum(key % 2, axis=iAx)
            if not((t > 0).all() and (t < sz_tup[iAx]).all()):
                return False

        # - Check that Inverse Exists
        if self.__get_finite_inverse(key) is not None:
            return True
        else:
            return False
