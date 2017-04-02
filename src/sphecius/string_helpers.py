# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 19:07:09 2017

@author: doug
"""

#
#   Imports
#
import string
import numpy as np

#
#   Variables
#


#
#   Functions
#

def string_to_list(text, seperator=' '):
    """Converts a string to a list of 'letters' using the (optional) seperator"""

    return text.split(seperator)


def list_to_string(text):
    """Converts a list of 'letters' to a contiguous String"""
    
    output = ''
    for letter in text:
        output += letter
    
    return output


def shift_forward(text, spaces):
    """Shifts the given string or list the given number of spaces forward"""
    
    output = text[-spaces::]
    if type(text) == str:
        output += text[:len(text)-spaces:]
    elif type(text) == list:
        output.extend(text[:len(text)-spaces:])
    else:
        output = text
    
    return output


def shift_backward(text, spaces):
    """Shifts the given string or list the given number of spaces backward"""
    
    output = text[spaces::]
    if type(text) == str:
        output += text[:spaces:]
    elif type(text) == list:
        output.extend(text[:spaces:])
    else:
        output = text
    
    return output


def remove_punctuation(text):
    """Removes all punctuation from the given string"""

    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def convert_text_to_matrix_2d(text, axis_size, axis=0, padding=None):
    """Converts the given Text to a Matrix

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
