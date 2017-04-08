# -*- coding: utf-8 -*-
"""
importers.py

    File with Functions to Import Data for Cryptanalysis

@author: Doug Daly
@date: 4/7/2017

"""

#
#   Imports
#


#
#   Functions
#

def load_text_from_file(Filename, section_divider='#', line_ender='\n', skip_lines_starting_with=None):
    """Load text from File

    :param str Filename: Path to the File to import
    :param str section_divider: Character used to denote page/section dividers (default is '#')
    :param str line_ender: Character used to denote line endings (if None lines are concatenated, default is '\n')
    :param list skip_lines_starting_with: Skip any lines starting with a character in the given list (default is None)

    :return: Dictionary of Dictionary, Page->Line->Text
    :rtype: dict

    """

    dict_ret = dict()
    curr_section_idx = 0
    curr_line_idx = 0
    dict_ret[curr_section_idx] = dict()

    with open(Filename, 'r') as fin:
        for line in fin:
            
