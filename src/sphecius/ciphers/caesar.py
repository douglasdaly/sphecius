# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 22:19:59 2017

@author: doug
"""

#
#   Imports
#


#
#   Class
#

class Caesar(object):
    """Caesar Cipher Class"""
    
    def __init__(self, alphabet, shift):
        """Default Constructor"""
        self.__shift = shift
        self.__alphabet = alphabet
        self.__shifted = self._get_shifted_alphabet()
        self.__encryptor = dict(zip(self.__alphabet, self.__shifted))
        self.__decryptor = dict(zip(self.__shifted, self.__alphabet))
    
    
    def _get_shifted_alphabet(self):
        """Gets the Shifted Alphabet Sequence"""
        shifted = self.__alphabet[-self.__shift::]
        shifted.extend(self.__alphabet[:len(self.__alphabet)-self.__shift:])
        return shifted
    
    
    def encrypt(self, plaintext):
        """Encrypts the given plaintext based on the set parameters of this class"""
        plaintext = plaintext.upper()
        
        output = list()
        for letter in plaintext:
            if letter in self.__encryptor.keys():
                output.append(self.__encryptor[letter])
            else:
                output.append(letter)
        
        return output
    
    
    def decrypt(self, ciphertext):
        """Decrypts the given Ciphertext based on the set parameters of this class"""
        ciphertext = ciphertext.upper()
        
        output = list()
        for letter in ciphertext:
            if letter in self.__decryptor.keys():
                output.append(self.__decryptor[letter])
            else:
                output.append(letter)
        
        return output