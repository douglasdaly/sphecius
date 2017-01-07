# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 17:43:25 2017

@author: doug
"""

#
#   Imports
#


def convert_from_morse(ToConvert, MinLetters=1):
    """Converts a string of . and -'s to Letters"""
    
    DictMorse = dict()
    DictMorse['.-'] = 'A'
    DictMorse['-...'] = 'B'
    DictMorse['-.-.'] = 'C'
    DictMorse['-..'] = 'D'
    DictMorse['.'] = 'E'
    DictMorse['..-.'] = 'F'
    DictMorse['--.'] = 'G'
    DictMorse['....'] = 'H'
    DictMorse['..'] = 'I'
    DictMorse['.---'] = 'J'
    DictMorse['-.-'] = 'K'
    DictMorse['.-..'] = 'L'
    DictMorse['--'] = 'M'
    DictMorse['-.'] = 'N'
    DictMorse['---'] = 'O'
    DictMorse['.--.'] = 'P'
    DictMorse['--.-'] = 'Q'
    DictMorse['.-.'] = 'R'
    DictMorse['...'] = 'S'
    DictMorse['-'] = 'T'
    DictMorse['..-'] = 'U'
    DictMorse['...-'] = 'V'
    DictMorse['.--'] = 'W'
    DictMorse['-..-'] = 'X'
    DictMorse['-.--'] = 'Y'
    DictMorse['--..'] = 'Z'
    
    DictMorse['-----'] = '0'
    DictMorse['.----'] = '1'
    DictMorse['..---'] = '2'
    DictMorse['...--'] = '3'
    DictMorse['....-'] = '4'
    DictMorse['.....'] = '5'
    DictMorse['-....'] = '6'
    DictMorse['--...'] = '7'
    DictMorse['---..'] = '8'
    DictMorse['----.'] = '9'
        
    cStr = ''
    outStr = ''
    
    for i in range(len(ToConvert)):
        cStr += ToConvert[i]
        if len(cStr) == MinLetters:
            if cStr in DictMorse.keys():
                outStr += DictMorse[cStr]
            else:
                outStr += ' '
            cStr = ''
                
    
    return outStr