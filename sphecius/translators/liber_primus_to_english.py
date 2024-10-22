"""
liber_primus_to_english.py

    Translator Class for LP Anglo Saxon Runic to English per the Cicada Gematria

@author: Douglas Daly
@date: 4/8/2017
"""

#
#   Imports
#
from .base import Translator


#
#   Class Definition
#

class LiberPrimusToEnglish(Translator):
    """
    Converts LP Runes to English
    """

    def _generate_translation_dict(self):
        """Generates the Translation Dictionary Needed

        :return: Translation Dictionary
        :rtype: dict

        """
        runes = ['ᚠ', 'ᚢ', 'ᚦ', 'ᚩ', 'ᚱ', 'ᚳ', 'ᚷ', 'ᚹ', 'ᚻ', 'ᚾ', 'ᛁ', 'ᛄ',
                 'ᛇ', 'ᛈ', 'ᛉ', 'ᛋ', 'ᛏ', 'ᛒ', 'ᛖ', 'ᛗ', 'ᛚ', 'ᛝ', 'ᛟ', 'ᛞ',
                 'ᚪ', 'ᚫ', 'ᚣ', 'ᛡ', 'ᛠ']
        english = ['F', 'U', 'TH', 'O', 'R', 'C', 'G', 'W', 'H', 'N', 'I', 'J',
                   'EO', 'P', 'X', 'S', 'T', 'B', 'E', 'M', 'L', 'ING', 'OE',
                   'D', 'A', 'AE', 'Y', 'IO', 'EA']
        ret_dict = dict(zip(runes, english))

        return ret_dict
