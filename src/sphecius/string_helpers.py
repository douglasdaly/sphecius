# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 19:07:09 2017

@author: doug
"""

#
#   Imports
#


#
#   Functions
#

def string_to_list(string, seperator=' '):
    """Converts a string to a list of 'letters' using the (optional) seperator"""

    return string.split(seperator)


def list_to_string(string):
    """Converts a list of 'letters' to a contiguous String"""
    
    output = ''
    for letter in string:
        output += letter
    
    return output


def shift_forward(string, spaces):
    """Shifts the given string or list the given number of spaces forward"""
    
    output = string[-spaces::]
    if type(string) == str:        
        output += string[:len(string)-spaces:]
    elif type(string) == list:
        output.extend(string[:len(string)-spaces:])
    else:
        output = string
    
    return output


def shift_backward(string, spaces):
    """Shifts the given string or list the given number of spaces backward"""
    
    output = string[spaces::]
    if type(string) == str:
        output += string[:spaces:]
    elif type(string) == list:
        output.extend(string[:spaces:])
    else:
        output = string
    
    return output