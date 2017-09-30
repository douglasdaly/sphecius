# -*- coding: utf-8 -*-
"""
ngram.py

    Class for NGram Analysis

@author: Douglas Daly
@date: 1/11/2017
"""
#
#   Imports
#
import os.path
from collections import Counter

from .. import string_helpers

#
#   Variables
#
_ngram_base_dir = "../resources/ngrams/"


#
#   Class
#

class NGram(object):
    """
    N-Gram class for Text Analysis
    """

    def __init__(self, n, language='english'):
        """ Default Constructor
        """
        filename = language + "_" + str(n) + "grams.txt"

        # - Throw Exception if no resource file for this
        if not os.path.isfile(_ngram_base_dir + filename):
            raise Exception("No N-Gram Resource File for N=" + str(n) + " and lang=" + language + " exists.")

        self.__n = n
        self.__gram_dict = self.__load_grams_from_file(_ngram_base_dir + filename)

    @staticmethod
    def __load_grams_from_file(filepath):
        """ Loads the N-Gram Dict from File

        :param str filepath: Filepath to load the N-Gram Dict from

        """
        occurrences = dict()
        run_tot = 0.0

        # - Load from File
        with open(filepath, 'r') as f:
            for line in f:
                splat = line.split(' ')
                tnum = float(splat[1])
                occurrences[splat[0].upper()] = tnum
                run_tot += tnum

        # - Convert to Probabilities/Rates
        output = dict()
        for (k, v) in occurrences.iteritems():
            output[k] = v / run_tot

        return output

    def get_single_word_occurrences(self, word):
        """ Gets occurrences of this N-Gram from the given Word

        :param str word: Word to get N-Gram occurrences for

        :return: Dictionary of N-Gram to Count
        :rtype: dict

        """
        if len(word) < self.__n:
            return dict()

        output = dict()
        for c in range(len(word)-self.__n+1):
            tw = word[c:c+self.__n]

            if tw in self.__gram_dict.keys():
                if tw not in output.keys():
                    output[tw] = 1
                else:
                    output[tw] += 1

        return output

    def get_text_occurrences(self, text, remove_spaces=False):
        """ Gets occurrences of this N-Gram from the given Text

        :param str text: Text to get N-Gram analysis for

        :return: Dictionary of N-Gram to occurrence count
        :rtype: dict

        """
        # - First strip punctuation
        text = string_helpers.remove_punctuation(text).upper()

        if remove_spaces:
            text = text.replace(' ', '')

        splat = text.split(' ')

        rc = Counter()
        for word in splat:
            tc = Counter(self.get_single_word_occurrences(word))
            rc.update(tc)

        return dict(rc)

    def convert_occurrences_to_sum_probabilities(self, occurrences):
        """ Converts the given Occurrence dictionary to the sum of the NGram probabilities

        :param dict occurrences: N-Gram Occurrences count dictionary

        :returns: Dictionary of N-Gram to sum of probability of N-Gram occurring
        :rtype: dict

        """
        output = dict()
        for (k, v) in occurrences.iteritems():
            output[k] = v * self.__gram_dict[k]

        return output

    def get_text_occurrence_rates(self, text, remove_spaces=False):
        """ Gets the occurrence rates for the given text

        :param str text: Text to get occurrence rates for
        :param bool remove_spaces: [Optional] Whether or not to remove spaces during the N-Gram analysis

        :return: Dictionary of N-Gram to percentage occurrence
        :rtype: dict

        """
        occurrences = self.get_text_occurrences(text, remove_spaces=remove_spaces)

        run_tot = 0.0
        for val in occurrences.values():
            run_tot += val

        output = dict()
        for (k, v) in occurrences.iteritems():
            output[k] = v / run_tot

        return output

    def get_relative_occurrence_rates(self, occurrence_rates):
        """ Gets the relative occurrence rates given a Dictionary of Occurrence Rates

        :param dict occurrence_rates: Occurrence rates to get relative values for

        :return: Dictionary of given occurrence rates normalized to 100 percent
        :rtype: dict

        """
        output = dict()

        run_tot = 0.0
        for k in occurrence_rates.keys():
            t = self.__gram_dict[k]
            run_tot += t
            output[k] = t

        for k in output.keys():
            output[k] /= run_tot

        return output
