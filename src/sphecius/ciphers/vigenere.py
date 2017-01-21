# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 22:17:38 2017

@author: doug
"""

#
#   Imports
#
from .. import string_helpers as sh
from base import Cipher

#
#   Class
#

class Vigenere(Cipher):
    """Vigenere Cipher Class"""
    
    def __init__(self, alphabet, initial_shift=0):
        """Default Constructor"""
        super(Vigenere, self).__init__(alphabet=alphabet)
        cryptors = self.__build_cryptors(alphabet, initial_shift)
        self.__encryptor = cryptors[0]
        self.__decryptor = cryptors[1]
    
    def __build_cryptors(self, alphabet, initial_shift=0):
        """Builds the Encryption Lookup Table"""
        len_alphabet = len(alphabet)
        
        cipher_table = dict()
        decipher_table = dict()
        for i in range(len_alphabet):
            c_letter = alphabet[i]
            c_alphabet = sh.shift_backward(alphabet, (i+initial_shift) % len_alphabet)

            cipher_table[c_letter] = dict()
            cipher_table[c_letter] = dict()
            for j in range(len_alphabet):
                cipher_table[c_letter][alphabet[j]] = c_alphabet[j]
                decipher_table[c_letter][c_alphabet[j]] = alphabet[j]
            
        return cipher_table, decipher_table

    def encrypt(self, plaintext, key):
        """Encrypts the given string using the given key and the set alphabet"""
        if type(plaintext) == list:
            plaintext = sh.list_to_string(plaintext)

        plaintext = plaintext.upper()
        key = self._key
        
        len_key = len(key)
        output = list()
        for i in range(len(plaintext)):
            s_let = plaintext[i]
            k_let = key[i % len_key]
            c_let = self.__encryptor[s_let][k_let]
            output.append(c_let)
        
        return sh.list_to_string(output)
    
    def decrypt(self, ciphertext):
        """Decrypts the given Cipher Text with the given Key"""
        if type(ciphertext) == list:
            ciphertext = sh.list_to_string(ciphertext)
        
        ciphertext = ciphertext.upper()
        key = self._key
        
        len_key = len(key)
        output = list()
        for i in range(len(ciphertext)):
            c_let = ciphertext[i]
            k_let = key[i % len_key]
            s_let = self.__decryptor[k_let][c_let]
            output.append(s_let)
        
        return sh.list_to_string(output)
