# -*- coding: utf-8 -*-
"""
liber_primus_to_reverse_liber_primus.py

    Translator Class for LP Anglo Saxon Runic to Reversed LP

@author: Douglas Daly
@date: 4/9/2017
"""
#
#   Imports
#
from .base import Translator


#
#   Class Definition
#

class LiberPrimusToReverseLiberPrimus(Translator):
    """
    Converts LP Runes to Reversed LP Runes
    """

    def _generate_translation_dict(self):
        """ Generates the Translation Dictionary Needed

        :return: Translation Dictionary
        :rtype: dict

        """
        runes = ['ᚠ', 'ᚢ', 'ᚦ', 'ᚩ', 'ᚱ', 'ᚳ', 'ᚷ', 'ᚹ', 'ᚻ', 'ᚾ', 'ᛁ', 'ᛄ',
                 'ᛇ', 'ᛈ', 'ᛉ', 'ᛋ', 'ᛏ', 'ᛒ', 'ᛖ', 'ᛗ', 'ᛚ', 'ᛝ', 'ᛟ', 'ᛞ',
                 'ᚪ', 'ᚫ', 'ᚣ', 'ᛡ', 'ᛠ']
        rev_runes = ['ᚠ', 'ᚢ', 'ᚦ', 'ᚩ', 'ᚱ', 'ᚳ', 'ᚷ', 'ᚹ', 'ᚻ', 'ᚾ', 'ᛁ',
                     'ᛄ', 'ᛇ', 'ᛈ', 'ᛉ', 'ᛋ', 'ᛏ', 'ᛒ', 'ᛖ', 'ᛗ', 'ᛚ', 'ᛝ',
                     'ᛟ', 'ᛞ', 'ᚪ', 'ᚫ', 'ᚣ', 'ᛡ', 'ᛠ']
        rev_runes.reverse()
        ret_dict = dict(zip(runes, rev_runes))

        return ret_dict
