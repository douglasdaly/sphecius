"""
rail_fence.py

    Rail-Fence Cipher Class

@author: Douglas Daly
@date: 4/10/2017
"""
#
#   Imports
#
from .base import Cipher
from .. import string_helpers


#
#   Class Definition
#

class RailFence(Cipher):
    """
    Rail Fence Cipher
    """

    def __init__(self, num_rails):
        """
        Default Constructor
        """
        self.set_key(num_rails)

    def set_key(self, key):
        """Sets the Key for this Cipher

        :param int key: Number of Rails to Use

        """
        self._key = key

    def encrypt(self, plaintext, strip_punctuation=False):
        """Encryption Method

        :param str plaintext: Plain text to encrypt
        :param bool strip_punctuation: Whether or not to strip the punctuation

        :return: Encrypted Text
        :rtype: str

        """
        if strip_punctuation:
            plaintext = string_helpers.remove_punctuation(plaintext)

        return ''.join(self.__fence(plaintext, self._key))

    def decrypt(self, ciphertext):
        """Decryption Method

        :param str ciphertext: Cipher text to Decrypt

        :return: Decrypted Text
        :rtype: str

        """
        rng = range(len(ciphertext))
        pos = self.__fence(rng, self._key)

        return ''.join(ciphertext[pos.index(self._key)] for n in rng)

    @staticmethod
    def __fence(text, n_rails):
        """Fence Algorithm Main Helper Method

        :param str text: Text to Encrypt/Decrypt
        :param int n_rails: Number of Rails to Use

        :return: Encrypted/Decrypted Text
        :rtype: str

        """
        fence = [[None] * len(text) for n in range(n_rails)]
        rails = list(range(n_rails - 1)) + list(range(n_rails - 1, 0, -1))

        for n, x in enumerate(text):
            fence[rails[n % len(rails)]][n] = x

        return [c for rail in fence for c in rail if c is not None]
