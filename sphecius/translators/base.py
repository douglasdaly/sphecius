"""
Base.py

    Base classes for the Translators.

@author: Doug Daly

"""

#
#   Imports
#
from ..alphabets import Alphabet


#
#   Class
#

class Translator(object):
    """
    Base Translator Object
    """

    def __init__(self, alphabet_from, alphabet_to):
        """Default Constructor

        :param Alphabet alphabet_from: The Alphabet we're translating from
        :param Alphabet alphabet_to: The Alphabet we're translating to

        """
        self._alphabet_from = alphabet_from
        self._alphabet_to = alphabet_to

    def translate(self, text):
        """Translates the given Text

        Translates the given text, in the 'From' Alphabet to the 'To' Alphabet.

        :param str text: Text to translate

        :return: Translated text
        :rtype: str

        """
        raise NotImplementedError()
