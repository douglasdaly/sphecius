# -*- coding: utf-8 -*-
"""
Created on Sat Jan  21 11:21:00 2017

@author: Douglas James Daly Jr.
"""

#
#   Imports
#
from .. import string_helpers


#
#   Functions
#

def index_of_coincidence(text, strip_punctuation=True):
    """Gets the IoC of the given Text

    :param str text: Text to get IoC for
    :param bool strip_punctuation: Should punctuation be stripped from the given text

    :return: Index of Coincidence of the given text
    :rtype: float

    """
    if strip_punctuation:
        text = string_helpers.remove_punctuation(text).replace(' ', '')
    dict_freqs = Lexical.get_character_frequencies(text=text, strip_punctuation=False)

    denom = len(text) * (len(text) - 1)
    num = 0.
    for ch in dict_freqs.keys():
        num += dict_freqs[ch] * (dict_freqs[ch]-1)

    return num / denom

def get_character_frequencies(text, strip_punctuation=True):
    """Gets a Dictionary of Character and Count from the given Text

    :param str text: Text to Count Character occurrences in
    :param bool strip_punctuation: [Optional] Strips punctuation from text (default is True)

    :return: Dictionary of Character to Count
    :rtype: dict

    """
    if strip_punctuation:
        text = string_helpers.remove_punctuation(text).replace(' ', '')

    d_ret = dict()
    for i in range(len(text)):
        c_char = text[i]
        if c_char not in d_ret.keys():
            d_ret[c_char] = 0
        d_ret[c_char] += 1

    return d_ret

def get_character_probabilities(text, strip_punctuation=True):
    """Gets a Dictionary of Character and Probability from the given Text

    :param str text: Text to Count Character occurrences in
    :param bool strip_punctuation: [Optional] Strips punctuation from text (default is True)

    :return: Dictionary of Character to Probability
    :rtype: dict

    """
    d_freqs = Lexical.get_character_frequencies(text, strip_punctuation)
    n_tot = sum(d_freqs.values())
    for k in d_freqs.keys():
        d_freqs[k] /= n_tot

    return d_freqs
