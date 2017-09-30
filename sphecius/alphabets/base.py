# -*- coding: utf-8 -*-
"""
base.py

    Base Alphabet class

@author: Douglas Daly
@date: 1/11/2017
"""
#
#   Imports
#
from abc import ABCMeta, abstractmethod


#
#   Class
#

class Alphabet(object, metaclass=ABCMeta):
    """
    Base Alphabet Class
    """

    @abstractmethod
    def __init__(self):
        """ Abstract Constructor
        """
        pass

    def get_alphabet(self):
        """ Abstract get Alphabet Method
        """
        return self._alphabet

    def get_alphabet_list(self):
        """ Gets the Alphabet in List format
        """
        return list(self.get_alphabet())

    def i2a(self, index):
        """ Gets the Letter at the given Index

        :param int index: Index to get letter at

        :return: Letter at the given position in the alphabet
        :rtype: str

        """
        if index < 1 or index > self.size():
            return None
        return self._alphabet[index-1]

    def a2i(self, letter):
        """Base get Index of Letter Method"""
        return self._alphabet.find(letter.upper()) + 1

    def size(self):
        """Length of the alphabet"""
        return len(self._alphabet)
