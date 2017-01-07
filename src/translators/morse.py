# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 17:43:25 2017

@author: doug
"""

#
#   Imports
#

class Morse(object):
    """
    Morse Code Translation Class
    """

    def __init__(self):
        """Default Constructor"""
        self.__dict_morse = self.__generate_morse_code_dictionary()
    
    
    def __generate_morse_code_dictionary(self):
        """Generates a dict() object of Morse Code"""
        
        dict_morse = dict()
        dict_morse['.-'] = 'a'
        dict_morse['-...'] = 'b'
        dict_morse['-.-.'] = 'c'
        dict_morse['-..'] = 'd'
        dict_morse['.'] = 'e'
        dict_morse['..-.'] = 'f'
        dict_morse['--.'] = 'g'
        dict_morse['....'] = 'h'
        dict_morse['..'] = 'i'
        dict_morse['.---'] = 'j'
        dict_morse['-.-'] = 'k'
        dict_morse['.-..'] = 'l'
        dict_morse['--'] = 'm'
        dict_morse['-.'] = 'n'
        dict_morse['---'] = 'o'
        dict_morse['.--.'] = 'p'
        dict_morse['--.-'] = 'q'
        dict_morse['.-.'] = 'r'
        dict_morse['...'] = 's'
        dict_morse['-'] = 't'
        dict_morse['..-'] = 'u'
        dict_morse['...-'] = 'v'
        dict_morse['.--'] = 'w'
        dict_morse['-..-'] = 'x'
        dict_morse['-.--'] = 'y'
        dict_morse['--..'] = 'z'
        
        dict_morse['-----'] = '0'
        dict_morse['.----'] = '1'
        dict_morse['..---'] = '2'
        dict_morse['...--'] = '3'
        dict_morse['....-'] = '4'
        dict_morse['.....'] = '5'
        dict_morse['-....'] = '6'
        dict_morse['--...'] = '7'
        dict_morse['---..'] = '8'
        dict_morse['----.'] = '9'
        
        return dict_morse
    
    
    def convert_from_morse(self, ToConvert, MinLetters=1):
        """Converts a string of . and -'s to Letters"""
        
        cStr = ''
        outStr = ''
        
        for i in range(len(ToConvert)):
            cStr += ToConvert[i]
            if len(cStr) == MinLetters:
                if cStr in self.__dict_morse.keys():
                    outStr += self.__dict_morse[cStr]
                else:
                    outStr += ' '
                cStr = ''
        
        return outStr