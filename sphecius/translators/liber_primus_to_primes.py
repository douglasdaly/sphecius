# -*- coding: utf-8 -*-
"""
liber_primus_to_primes.py

    Translator Class for LP Anglo Saxon Runic to Primes per the Cicada Gematria

@author: Doug Daly
@date: 4/8/2017
"""

#
#   Imports
#
from .base import Translator


#
#   Class Definition
#

class LiberPrimusToPrimes(Translator):
    """
    Converts LP Runes to Their Prime Values
    """

    def _generate_translation_dict(self):
        """Generates the Translation Dictionary Needed

        :return: Translation Dictionary
        :rtype: dict

        """
        runes = ['ᚠ', 'ᚢ', 'ᚦ', 'ᚩ', 'ᚱ', 'ᚳ', 'ᚷ', 'ᚹ', 'ᚻ', 'ᚾ', 'ᛁ', 'ᛄ', 'ᛇ', 'ᛈ', 'ᛉ', 'ᛋ', 'ᛏ', 'ᛒ', 'ᛖ', 'ᛗ',
                 'ᛚ', 'ᛝ', 'ᛟ', 'ᛞ', 'ᚪ', 'ᚫ', 'ᚣ', 'ᛡ', 'ᛠ']
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                  103, 107, 109]
        ret_dict = dict(zip(runes, primes))

        return ret_dict
