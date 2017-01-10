# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 22:17:38 2017

@author: doug
"""

#
#   Imports
#
import sphecius.string_helpers as sh

#
#   Class
#

class Vigenere(object):
    """Vigenere Cipher Class"""
    
    def __init__(self, alphabet, initial_shift=0):
        """Default Constructor"""
        cryptors = self.__build_cryptors(alphabet, initial_shift)
        self.__encryptor = cryptors[0]
        self.__decryptor = cryptors[1]
    
    
    def __build_cryptors(self, alphabet, initial_shift=0):
        """Builds the Encryption Lookup Table"""
        lAlphabet = len(alphabet)
        
        cipherTable = dict()
        decipherTable = dict()
        for i in range(lAlphabet):
            cLetter = alphabet[i]
            cAlphabet = sh.shift_backward(alphabet, (i+initial_shift) % lAlphabet)
            
            cipherTable[cLetter] = dict()
            decipherTable[cLetter] = dict()
            for j in range(lAlphabet):
                cipherTable[cLetter][alphabet[j]] = cAlphabet[j]
                decipherTable[cLetter][cAlphabet[j]] = alphabet[j]
            
        return (cipherTable, decipherTable)
    
    
    def encrypt(self, string, key):
        """Encrypts the given string using the given key and the set alphabet"""
        
        if type(string) == list:
            string = sh.list_to_string(string)
        
        string = string.upper()
        key = key.upper()
        
        lKey = len(key)
        output = list()
        for i in range(len(string)):
            sLet = string[i]
            kLet = key[i % lKey]
            cLet = self.__encryptor[sLet][kLet]
            output.append(cLet)
        
        return sh.list_to_string(output)
    
    
    def decrypt(self, cipher, key):
        """Decrypts the given Cipher Text with the given Key"""
        
        if type(cipher) == list:
            cipher = sh.list_to_string(cipher)
        
        cipher = cipher.upper()
        key = key.upper()
        
        lKey = len(key)
        output = list()
        for i in range(len(cipher)):
            cLet = cipher[i]
            kLet = key[i % lKey]
            sLet = self.__decryptor[kLet][cLet]
            output.append(sLet)
        
        return sh.list_to_string(output)
    
