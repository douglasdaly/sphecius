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

        dict_tup = self.__generate_morse_code_dictionaries()
        self.__dict_to_morse = dict_tup[0]
        self.__dict_from_morse = dict_tup[1]
    
    
    def __generate_morse_code_dictionaries(self):
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
        
        dict_morse['.-.-.-'] = '.'
        dict_morse['--..--'] = ','
        dict_morse['..--..'] = '?'
        dict_morse['-.-.--'] = '!'
        
        dict_letters = dict()
        for key in dict_morse.keys():
            dict_letters[dict_morse[key]] = key
        
        return (dict_letters, dict_morse)
    
    
    def convert_to(self, to_convert):
        """Converts the given letter string to morse code"""
        
        to_convert = to_convert.lower()
        output = '|'
        for l in range(len(to_convert)):
            letter = to_convert[l]
            if letter == ' ':
                output += ' '
            elif letter in self.__dict_to_morse.keys():
                output += self.__dict_to_morse[letter]
            else:
                output += '*'
            output += '|'
        
        return output.strip()
                
    
    def convert_from(self, to_convert):
        """Converts a morse string with spaces to the english letters"""
        
        # - Divy it up
        if to_convert.find('|') > -1:
            arr = to_convert.strip('|').split('|')
        else:
            arr = to_convert.strip().split(' ')
        
        output = ''
        for word in arr:
            output += self.convert_from_no_spaces(word, len(word))
        
        return output
    
    
    def convert_from_no_spaces(self, to_convert, min_letters=1):
        """Converts a string of . and -'s to Letters with no spaces/breaks in it"""
        
        cStr = ''
        outStr = ''
        
        for i in range(len(to_convert)):
            cStr += to_convert[i]
            if len(cStr) == min_letters:
                if cStr in self.__dict_from_morse.keys():
                    outStr += self.__dict_from_morse[cStr]
                else:
                    outStr += ' '
                cStr = ''
        
        return outStr