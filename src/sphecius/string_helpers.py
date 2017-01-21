# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 19:07:09 2017

@author: doug
"""

#
#   Imports
#
import regex


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

    return regex.sub(ur"\p{P}+", "", text)
