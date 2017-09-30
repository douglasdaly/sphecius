# -*- coding: utf-8 -*-
"""
lexical.py

    Lexical Cryptanalysis Functions

@author: Douglas Daly
@date: 1/21/2017
"""
#
#   Imports
#
from .. import string_helpers
from ..alphabets import Alphabet


#
#   Functions
#

def index_of_coincidence(text):
    """ Gets the IoC of the given Text

    :param str text: Text to get IoC for

    :return: Index of Coincidence of the given text
    :rtype: float

    """
    return ngram_index_of_coincidence(text, 1)


def index_of_coincidence_normalized(text, alphabet):
    """Gets the Normalized IoC of the given Text

    :param str text: Text to get IoC for
    :param Alphabet alphabet: Alphabet to normalize to

    :return: Normalized IoC Value
    :rtype: float

    """
    return index_of_coincidence(text) * alphabet.size()


def ngram_index_of_coincidence(text, gram_length):
    """ Gets the IoC of NGrams of the given Text

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
    """ Gets a Dictionary of N-Gram to Count from a given Text

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
    """ Gets a Dictionary of N-Gram to Count from a given Text

    :param str text: Text to get NGram Frequencies from
    :param int gram_length: Length of the NGram to get
    :param bool strip_punctuation: Strip punctuation from the text first (default is True)

    :return: Dictionary of NGram to Occurrence Frequency
    :rtype: dict

    """
    d_freqs = get_ngram_frequencies(text, gram_length, strip_punctuation=strip_punctuation)
    return __convert_frequency_dict_to_rates(d_freqs)


def get_character_frequencies(text, strip_punctuation=True):
    """ Gets a Dictionary of Character and Count from the given Text

    :param str text: Text to Count Character occurrences in
    :param bool strip_punctuation: [Optional] Strips punctuation from text (default is True)

    :return: Dictionary of Character to Count
    :rtype: dict

    """
    return get_ngram_frequencies(text, 1, strip_punctuation=strip_punctuation)


def get_character_probabilities(text, strip_punctuation=True):
    """ Gets a Dictionary of Character and Probability from the given Text

    :param str text: Text to Count Character occurrences in
    :param bool strip_punctuation: [Optional] Strips punctuation from text (default is True)

    :return: Dictionary of Character to Probability
    :rtype: dict

    """
    d_freqs = get_character_frequencies(text, strip_punctuation)
    return __convert_frequency_dict_to_rates(d_freqs)


def __convert_frequency_dict_to_rates(freq_dict):
    """ Converts a Frequency Dictionary to a Probability Dictionary

    :param dict freq_dict: Dictionary of Frequencies of Occurrence

    :return: Dictionary of Probabilities/Rates of Occurrence
    :rtype: dict

    """
    n_tot = sum(freq_dict.values())
    for k in freq_dict.keys():
        freq_dict[k] /= n_tot

    return freq_dict


def measure_of_roughness(text, alphabet):
    """ Gets the Measure of Roughness for the given Text and Alphabet Length

    :param str text: Text to get MR for
    :param Alphabet alphabet: Alphabet to calculate MR for

    :return: Measure of Roughness for  the given Text and Alphabet Length
    :rtype: float

    """
    d_probs = get_character_probabilities(text, True)
    mr = 0.
    for letter in alphabet.get_alphabet_list():
        if letter in d_probs.keys():
            mr += (d_probs[letter] - (1/alphabet.size()))**2
        else:
            mr += (-(1/alphabet.size()))**2

    return mr


def chi_squared_statistic(text, dict_expected_probabilities):
    """ Gets the Chi-Squared Statistic for the Given Text and Expected Probability Distribution

    :param str text: Text to get Chi-Squared Statistic for
    :param dict dict_expected_probabilities: Dictionary of Letter to Expected Probability

    :return: Chi-Squared Statistic for the given Text
    :rtype: float

    """
    text = string_helpers.remove_punctuation(text)
    d_freqs = get_ngram_frequencies(text, False)
    n_text = len(text)
    cs = 0.
    for ch in dict_expected_probabilities.keys():
        exp_cnt = dict_expected_probabilities[ch] * n_text
        if ch in d_freqs.keys():
            num = (d_freqs[ch] - exp_cnt)**2
        else:
            num = (-exp_cnt)**2

        cs += num / exp_cnt

    return cs
