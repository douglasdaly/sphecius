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

def index_of_coincidence(text):
    """Gets the IoC of the given Text

    :param str text: Text to get IoC for

    :return: Index of Coincidence of the given text
    :rtype: float

    """
    return ngram_index_of_coincidence(text, 1)


def ngram_index_of_coincidence(text, gram_length):
    """Gets the IoC of NGrams of the given Text

    :param str text: Text to get NGram IoC for
    :param int gram_length: Length of NGram to get IoC for

    :return: Index of Coincidence of NGrams of the given text
    :rtype: float
    """
    text = string_helpers.remove_punctuation(text).replace(' ', '')
    dict_freqs = get_ngram_frequencies(text=text, gram_length=gram_length, strip_punctuation=False)

    denom = len(text) * (len(text) - 1)
    num = 0.
    for ch in dict_freqs.keys():
        num += dict_freqs[ch] * (dict_freqs[ch]-1)

    return num / denom

def get_ngram_frequencies(text, gram_length, strip_punctuation=True):
    """Gets a Dictionary of N-Gram to Count from a given Text

    :param str text: Text to get NGram Frequencies from
    :param int gram_length: Length of the NGram to get
    :param bool strip_punctuation: Strip punctuation from the text first (default is True)

    :return: Dictionary of NGram to Occurrence Frequency
    :rtype: dict

    """
    if strip_punctuation:
        text = string_helpers.remove_punctuation(text).replace(' ', '')

    d_ret = dict()
    for i in range(len(text)-gram_length+1):
        ngram = text[i:i+gram_length]
        if ngram not in d_ret.keys():
            d_ret[ngram] = 0
        d_ret[ngram] += 1

    return d_ret


def get_ngram_probabilities(text, gram_length, strip_punctuation=True):
    """Gets a Dictionary of N-Gram to Count from a given Text

    :param str text: Text to get NGram Frequencies from
    :param int gram_length: Length of the NGram to get
    :param bool strip_punctuation: Strip punctuation from the text first (default is True)

    :return: Dictionary of NGram to Occurrence Frequency
    :rtype: dict

    """
    d_freqs = get_ngram_frequencies(text, gram_length, strip_punctuation=strip_punctuation)
    return __convert_frequency_dict_to_rates(d_freqs)


def get_character_frequencies(text, strip_punctuation=True):
    """Gets a Dictionary of Character and Count from the given Text

    :param str text: Text to Count Character occurrences in
    :param bool strip_punctuation: [Optional] Strips punctuation from text (default is True)

    :return: Dictionary of Character to Count
    :rtype: dict

    """
    return get_ngram_frequencies(text, 1, strip_punctuation=strip_punctuation)


def get_character_probabilities(text, strip_punctuation=True):
    """Gets a Dictionary of Character and Probability from the given Text

    :param str text: Text to Count Character occurrences in
    :param bool strip_punctuation: [Optional] Strips punctuation from text (default is True)

    :return: Dictionary of Character to Probability
    :rtype: dict

    """
    d_freqs = get_character_frequencies(text, strip_punctuation)
    return __convert_frequency_dict_to_rates(d_freqs)


def __convert_frequency_dict_to_rates(freq_dict):
    """Converts a Frequency Dictionary to a Probability Dictionary

    :param dict freq_dict: Dictionary of Frequencies of Occurrence

    :return: Dictionary of Probabilities/Rates of Occurrence
    :rtype: dict

    """
    n_tot = sum(freq_dict.values())
    for k in freq_dict.keys():
        freq_dict[k] /= n_tot

    return freq_dict
