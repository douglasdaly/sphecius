"""
Base.py

    Base classes for the Translators.

@author: Doug Daly
@date: 4/8/2017
"""

#
#   Imports
#


#
#   Class
#

class Translator(object):
    """
    Base Translator Object
    """

    def __init__(self):
        """Default Constructor"""
        self._to_dict = self._generate_to_dict()
        self._from_dict = self._generate_from_dict()

    def translate_to(self, text):
        """Translates the given Text

        Translates the given text, in the 'From' Alphabet to the 'To' Alphabet.

        :param str text: Text to translate

        :return: Translated text
        :rtype: str

        """
        return self.__translate(text, self._to_dict)

    def translate_from(self, text):
        """Translates the given Text

        Translates the given text, in the 'To' Alphabet to the 'From' Alphabet.

        :param str text: Text to translate

        :return: Translated text
        :rtype: str

        """
        return self.__translate(text, self._from_dict)

    def __translate(self, text, translation_dict):
        """Function which does the Translation

        :param str text: Text to Translate
        :param dict translation_dict: Dictionary to use for Translation

        :return: Translated String
        :rtype: str

        """
        ret = ''
        for ch in text:
            if ch in translation_dict.keys():
                ret += translation_dict[ch]
            else:
                ret += ch

        return ret

    def _generate_to_dict(self):
        """Generates the Translate To Dictionary

        :return: Dictionary of Character to Character Translation
        :rtype: dict

        """
        raise NotImplementedError()

    def _generate_from_dict(self):
        """Generates the Translate From Dictionary

        :return: Dictionary of Character to Character Translation
        :rtype: dict

        """
        raise NotImplementedError()
