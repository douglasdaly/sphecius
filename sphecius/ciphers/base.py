# -*- coding: utf-8 -*-
"""
base.py

    Base Cipher Object class

@author: Douglas Daly
@date: 1/12/2017
"""
#
#   Imports
#
from abc import ABCMeta, abstractmethod

from ..alphabets import English


#
#   Classes
#

class Cipher(object, metaclass=ABCMeta):
    """
    Base Cipher Class
    """

    def __init__(self, alphabet=English):
        """ Default Constructor
        """
        self._alphabet = alphabet
        self._key = None

    def set_key(self, key):
        """ Sets the Key for this Cipher object

        :param str key: Key for this Cipher object

        """
        self._key = key.upper()

    @abstractmethod
    def encrypt(self, plaintext):
        """ Abstract Encrypt Method

        :param str plaintext: Text to encrypt

        :returns: Encrypted text
        :rtype: str

        """
        pass

    @abstractmethod
    def decrypt(self, ciphertext):
        """ Abstract Decrypt Method

        :param str ciphertext: Text to decrypt

        :returns: Decrypted text
        :rtype: str

        """
        pass
