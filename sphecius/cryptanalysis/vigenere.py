# -*- coding: utf-8 -*-
"""
vigenere.py

    Cryptanalysis Functions for Vigenere Ciphers

@author: Douglas Daly
@date: 4/13/2017
"""
#
#   Imports
#
import operator

from .. import string_helpers
from . import lexical


#
#   Functions
#

def get_coset_length_to_ioc(text, max_coset_length=20):
    """ Gets a dictionary of Coset-Length to Ic Value

    :param str text: Text to Analyze
    :param int max_coset_length: Max Coset Length to Analyze (default 20)

    :return: Dictionary of Coset-Length to Ic Value
    :rtype: dict

    """
    d_ret = dict()
    for coset_length in range(1, max_coset_length+1):
        text_cosets = string_helpers.get_coset_strings(text, coset_length)

        avg_ioc = 0.
        for coset in text_cosets:
            avg_ioc += lexical.index_of_coincidence(coset)
        avg_ioc /= len(text_cosets)

        d_ret[coset_length] = avg_ioc

    return d_ret


def get_most_likely_key_length_ioc(text, max_coset_length=20):
    """ Returns the most likely Key-Length based on the Coset Analysis

    :param str text: Text to Analyze
    :param int max_coset_length: Max Coset Length to Analyze (default 20)

    :return: Most Likely Vigenere Key Length
    :rtype: int

    """
    d_coset_to_iocs = get_coset_length_to_ioc(text, max_coset_length)

    return max(d_coset_to_iocs.items(), key=operator.itemgetter(1))[0]
