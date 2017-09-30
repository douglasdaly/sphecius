# -*- coding: utf-8 -*-
"""
anglo_saxon_runic.py

    Anglo-Saxon Runic Alphabet

@author: Douglas Daly
@date: 1/11/2017
"""

#
#   Imports
#
from .base import Alphabet

#
#   Class
#


class AngloSaxonRunic(Alphabet):
    """Anglo-Saxon Rune Letters Class"""
    
    def __init__(self):
        """Default Constructor"""
        self._alphabet = "ᚠᚢᚦᚩᚱᚳᚷᚹᚻᚾᛁᛄᛇᛈᛉᛋᛏᛒᛖᛗᛚᛝᛟᛞᚪᚫᚣᛡᛠ"
