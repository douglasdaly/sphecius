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

    @property
    def alphabet(self):
        """ Alphabet Property
        """
        return self._alphabet

    def get_alphabet_list(self):
        """ Gets the Alphabet in List format
        """
        return list(self._alphabet)

    def __getitem__(self, item):
        """ Gets the Letter at the given index or the index at the given letter

        :param item: Either the Letter to get the index of or the index of the letter to get

        :return: Either the Letter at the given Index or Index of the given Letter
        :rtype: str or int

        """
        if type(item) == str:
            return self.a2i(item)
        else:
            return self.i2a(item)

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
        """ Base get Index of Letter Method

        :param str letter: Letter to get the index of

        :return: Index of the letter given (1-based indexing)
        :rtype: int

        """
        return self._alphabet.find(letter.upper()) + 1

    def size(self):
        """ Length of the alphabet

        :return: Length of this alphabet
        :rtype: int

        """
        return len(self._alphabet)
