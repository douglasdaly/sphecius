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
        self._translate_dict = self._generate_translation_dict()

    def translate(self, text):
        """Function which does the Translation

        :param str text: Text to Translate

        :return: Translated String
        :rtype: str

        """
        ret = ''
        for ch in text:
            if ch in self._translate_dict.keys():
                ret += self._translate_dict[ch]
            else:
                ret += ch

        return ret

    def _generate_translation_dict(self):
        """Generates the Translation Dictionary

        :return: Dictionary of Character to Character Translation
        :rtype: dict

        """
        raise NotImplementedError()
