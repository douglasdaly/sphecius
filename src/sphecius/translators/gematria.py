# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 20:49:03 2017

@author: doug
"""

#
#   Imports
#


#
#   Class
#

class Gematria(object):
    """
    Rune Translator Class
    """
    
    def __init__(self):
        """Default Constructor"""
        dicts = self.__generate_dictionaries()
        self.__dict_rune_to_eng = dicts[0]
        self.__dict_rune_to_num = dicts[1]
        self.__dict_eng_to_rune = dicts[2]
        self.__dict_eng_to_num = dicts[3]
        self.__dict_num_to_rune = dicts[4]
        self.__dict_num_to_eng = dicts[5]
    
    
    def __generate_dictionaries(self):
        """Generates the Dictionaries needed to use this Gematria"""
        
        runes =     ['ᚠ', 'ᚢ', 'ᚦ', 'ᚩ', 'ᚱ', 'ᚳ', 'ᚷ', 'ᚹ', 'ᚻ', 'ᚾ', 'ᛁ', 'ᛄ', 'ᛇ', 'ᛈ', 'ᛉ', 'ᛋ', 'ᛏ', 'ᛒ', 'ᛖ', 'ᛗ', 'ᛚ', 'ᛝ', 'ᛟ', 'ᛞ', 'ᚪ', 'ᚫ', 'ᚣ', 'ᛡ', 'ᛠ']
        english =   ['F', 'U', 'TH', 'O', 'R', 'C/K', 'G', 'W', 'H', 'N', 'I', 'J', 'EO', 'P', 'X', 'S/Z', 'T', 'B', 'E', 'M', 'L', 'NG/ING', 'OE', 'D', 'A', 'AE', 'Y', 'IA/IO', 'EA'] 
        numbers =   [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109]
        
        runes_to_eng = dict(zip(runes, english))
        runes_to_num = dict(zip(runes, numbers))
        eng_to_runes = dict(zip(english, runes))
        eng_to_num = dict(zip(english, numbers))
        num_to_runes = dict(zip(runes, numbers))
        num_to_eng = dict(zip(numbers, english))
        
        # - Additions
        runes_to_eng['•'] = ' '
        eng_to_runes[' '] = '•'
        
        return (runes_to_eng, runes_to_num, eng_to_runes, eng_to_num, num_to_runes, num_to_eng)