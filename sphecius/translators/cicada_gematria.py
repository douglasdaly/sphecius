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

class CicadaGematria(object):
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
        
        self.__runes = runes
        
        runes_to_eng = dict(zip(runes, english))
        runes_to_num = dict(zip(runes, numbers))
        eng_to_runes = dict(zip(english, runes))
        eng_to_num = dict(zip(english, numbers))
        num_to_runes = dict(zip(runes, numbers))
        num_to_eng = dict(zip(numbers, english))
        
        # - C/K
        eng_to_runes['C'] = eng_to_runes['C/K']
        eng_to_runes['K'] = eng_to_runes['C/K']        
                
        eng_to_num['C'] = eng_to_num['C/K']
        eng_to_num['K'] = eng_to_num['C/K']
                
        # - S/Z
        eng_to_runes['S'] = eng_to_runes['S/Z']
        eng_to_runes['Z'] = eng_to_runes['S/Z']
                
        eng_to_num['S'] = eng_to_num['S/Z']
        eng_to_num['Z'] = eng_to_num['S/Z']
                
        # - Additions
        #runes_to_eng['•'] = ' '
        #eng_to_runes[' '] = '•'
        
        return (runes_to_eng, runes_to_num, eng_to_runes, eng_to_num, num_to_runes, num_to_eng)
    
    
    def __conversion_helper(self, str_to_convert, dict_to_use):
        """Helper function for doing conversions"""
        output = list()
        for letter in str_to_convert:
            if letter in dict_to_use.keys():
                output.append(dict_to_use[letter])
            else:
                output.append(letter)
        
        return output

    
    def convert_to_runes(self, english=None, numbers=None):
        """Converts the given English or Numbers to Runes"""
        
        if english is not None:
            return self.__conversion_helper(english, self.__dict_eng_to_rune)
        else:
            return self.__conversion_helper(numbers, self.__dict_num_to_rune)


    def convert_to_english(self, runes=None, numbers=None):
        """Converts the given Runes or Numbers to English"""
        
        if runes is not None:
            return self.__conversion_helper(runes, self.__dict_rune_to_eng)
        else:
            return self.__conversion_helper(numbers, self.__dict_num_to_eng)
    
    
    def convert_to_numbers(self, runes=None, english=None):
        """Converts the given Runes or English to Numbers"""
        
        if runes is not None:
            return self.__conversion_helper(runes, self.__dict_rune_to_num)
        else:
            return self.__conversion_helper(english, self.__dict_eng_to_num)
    
    
    def get_alphabet(self):
        """Gets the ordered alphabet for this translator object"""
        
        return self.__runes
