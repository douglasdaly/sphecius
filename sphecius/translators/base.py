# -*- coding: utf-8 -*-
"""
base.py

    Base classes for the Translators.

@author: Douglas Daly
@date: 4/8/2017
"""
#
#   Imports
#
from abc import ABCMeta, abstractmethod


#
#   Class
#

class Translator(object, metaclass=ABCMeta):
    """
    Base Translator Object
    """

    def __init__(self):
        """ Default Constructor
        """
        self._translate_dict = self._generate_translation_dict()

    def translate(self, text):
        """ Function which does the Translation

        :param str text: Text to Translate

        :return: Translated String
        :rtype: str

        """
        ret = ''
        for ch in text:
            if ch in self._translate_dict.keys():
                ret += self._translate_dict[ch]
            else:
                ret += str(ch)

        return ret

    def translate_single(self, character):
        """ Function to translate a Single character

        :param str character: Character to Translate

        :return: Translated Character
        :rtype: str

        """
        if character in self._translate_dict.keys():
            return self._translate_dict[character]
        else:
            return None

    @abstractmethod
    def _generate_translation_dict(self):
        """ Generates the Translation Dictionary

        :return: Dictionary of Character to Character Translation
        :rtype: dict

        """
        pass
