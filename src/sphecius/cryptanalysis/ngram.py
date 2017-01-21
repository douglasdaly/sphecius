# -*- coding: utf-8 -*-
"""
Created on Sat Jan  21 11:21:00 2017

@author: doug
"""

#
#   Imports
#
import os.path

#
#   Variables
#
ngram_base_dir = "../resources/ngrams/"

#
#   Class
#

class NGram(object):
    """N-Gram class for Text Analysis"""

    def __init__(self, n, language='english'):
        """Default Constructor"""
        filename = language + "_" + str(n) + "grams.txt"

        # - Throw Exception if no resource file for this
        if not os.path.isfile(ngram_base_dir + filename):
            raise Exception("No N-Gram Resource File for N=" + str(n) + " and lang=" + language + " exists.")

        self.__n = n
        self.__gram_dict = self.__load_grams_from_file(ngram_base_dir + filename)

    @staticmethod
    def __load_grams_from_file(filepath):
        """Loads the N-Gram Dict from File"""
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

    def get_occurrences(self, text, remove_spaces=False):
        """Gets occurrences of this N-Gram from the given Text"""
        