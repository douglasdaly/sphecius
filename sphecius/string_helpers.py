# -*- coding: utf-8 -*-
"""
string_helpers.py

    Commonly used string manipulation functions

@author: Douglas Daly
@date: 1/9/2017
"""
#
#   Imports
#
import string
import numpy as np

from .alphabets import Alphabet


#
#   Functions
#

def string_to_list(text, separator=' '):
    """ Converts a string to a list of 'letters' using the (optional) separator

    :param str text: Text to split
    :param str seperator: [Optional] Separator to split string by (defaults to a space)

    :return: List of split string elements
    :rtype: list

    """
    return text.split(separator)


def list_to_string(text):
    """ Converts a list of 'letters' to a contiguous String

    :param list text: Text split into elements in a list

    :return: Single string of the concatenated given list
    :rtype: str

    """
    output = ''
    for letter in text:
        output += letter
    
    return output


def shift_forward(text, spaces):
    """ Shifts the given string or list the given number of spaces forward

    :param str text: Text to shift
    :param int spaces: Number of spaces to shift the text forward by

    :return: Forward-shifted string
    :rtype: str

    """
    output = text[-spaces::]
    if type(text) == str:
        output += text[:len(text)-spaces:]
    elif type(text) == list:
        output.extend(text[:len(text)-spaces:])
    else:
        output = text
    
    return output


def shift_backward(text, spaces):
    """ Shifts the given string or list the given number of spaces backward

    :param str text: Text to shift
    :param int spaces: Number of spaces to shift the text backwards by

    :return: Backward-shifted string
    :rtype: str

    """
    output = text[spaces::]
    if type(text) == str:
        output += text[:spaces:]
    elif type(text) == list:
        output.extend(text[:spaces:])
    else:
        output = text
    
    return output


def remove_punctuation(text):
    """ Removes all punctuation from the given string

    :param str text: Removes all punctuation from the given text

    :return: Punctuation-removed string
    :rtype: str

    """
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def replace_stripped_text(original_text, stripped_text, chars_stripped=string.punctuation):
    """ Inserts punctuation back into stripped string

    :param str original_text: Original text with punctuation
    :param str stripped_text: Text stripped of punctuation to put punctuation back in
    :param list chars_stripped: [Optional] List of Stripped Characters to put back in

    :return: String with stripped characters replaced
    :rtype: str

    """
    ret = ''
    i_s = 0
    for i_o in range(len(original_text)):
        if original_text[i_o] in chars_stripped:
            ret += original_text[i_o]
            if original_text[i_o] == '.':
                ret += ' '
        else:
            if i_s < len(stripped_text):
                ret += stripped_text[i_s]
                i_s += 1

    return ret


def convert_text_to_matrix_2d(text, axis_size, axis=0, padding=None):
    """ Converts the given Text to a Matrix

    Converts the given text a matrix with the given row length and optionally pads
    the last column with the given string.

    :param str text: Text to convert into matrix
    :param int axis_size: Fixed length of the axis to build across
    :param int axis: [Optional] Which axis to limit (0 for Column, 1 for Rows; defaults to 0)
    :param str padding: [Optional] Pad the text to fit with the given string (defaults to space)

    :return: Matrix created from the given text
    :rtype: numpy.matrix

    """
    last_i = 0
    li_cols = list()
    for i in range(axis_size, len(text), axis_size):
        subtext = list(text[last_i:i])

        subarr = np.array(subtext)
        if axis == 1:
            subarr = subarr.reshape(axis_size, 1)
        li_cols.append(subarr)

        last_i = i

    if last_i < len(text):
        sstr = text[last_i::]
        for j in range(axis_size-len(sstr)):
            if padding is not None:
                sstr += padding[j % len(padding)]
            else:
                sstr += ' '

        subarr = np.array(list(sstr))
        if axis == 1:
            subarr = subarr.reshape(axis_size, 1)
        li_cols.append(subarr)

    return np.concatenate(li_cols, axis=axis)


def convert_matrix_to_text_2d(matrix, axis=0):
    """ Converts a text Matrix back to String

    Given a text matrix, convert it back into a single string.

    :param numpy.matrix matrix: Matrix of text to convert back to string
    :param int axis: [Optional] Which axis to limit (0 for Column, 1 for Rows; defaults to 0)

    :return: String converted back from matrix
    :rtype: str

    """
    ret = ''
    for i in range(matrix.shape[axis]):
        if axis == 0:
            ret += ''.join(matrix[i, :].tolist()[0])
        else:
            ret += ''.join(matrix[:, i].transpose().tolist()[0])

    return ret


def strip_non_alphabet_characters(text, alphabet2use):
    """ Strips any Non-Alphabet Characters from the given Text

    :param str text: Text to strip
    :param Alphabet alphabet2use: Alphabet to use

    :return: Stripped String
    :rtype: str

    """
    alpha = alphabet2use.get_alphabet().upper()
    ret = ''
    text = text.upper()
    for ch in text:
        if ch in alpha:
            ret += ch

    return ret


def get_coset_strings(text, coset_length):
    """ Returns a list of Coset Strings using the length Given

    :param str text: Text to get cosets of
    :param int coset_length: Length of coset to use (every Nth letter)

    :return: List of sub-string cosets
    :rtype: list

    """
    ret = list()
    for i in range(coset_length):
        ret.append(text[i:len(text):coset_length])

    return ret
