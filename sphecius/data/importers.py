# -*- coding: utf-8 -*-
"""
importers.py

    File with Functions to Import Data for Cryptanalysis

@author: Douglas Daly
@date: 4/7/2017
"""

#
#   Functions
#

def load_text_from_file(filename, section_divider='\n', line_ender='\n',
                        skip_lines_starting_with=None):
    """ Load text from File

    :param str filename: Path to the File to import
    :param str section_divider: Character used to denote page/section dividers
                                (default is '\n')
    :param str line_ender: Character used to denote line endings (if None lines
                           are concatenated, default is '\n')
    :param list skip_lines_starting_with: Skip any lines starting with a
                                          character in the given list (default
                                          is None)

    :return: Dictionary of Dictionaries, Page->Line->Text
    :rtype: dict

    """
    if skip_lines_starting_with is None:
        skip_lines_starting_with = list()

    dict_ret = dict()
    curr_section_idx = 0
    curr_line_idx = 0
    dict_ret[curr_section_idx] = dict()
    dict_ret[curr_section_idx][curr_line_idx] = ''

    with open(filename, 'r') as fin:
        for line in fin:
            if line[0] in skip_lines_starting_with:
                continue

            if line[0] == section_divider:
                curr_section_idx += 1
                curr_line_idx = 0
                dict_ret[curr_section_idx] = dict()
                dict_ret[curr_section_idx][curr_line_idx] = ''
                continue

            if line_ender == '\n' or len(line) == 1:
                t_line_ender = line[:-1]
                end_clip = 1
            else:
                t_line_ender = line[-2]
                end_clip = 2

            if t_line_ender == line_ender:
                t_line = line[:-end_clip]
            else:
                t_line = line

            dict_ret[curr_section_idx][curr_line_idx] += t_line

            if t_line_ender == line_ender:
                curr_line_idx += 1
                dict_ret[curr_section_idx][curr_line_idx] = ''

    return dict_ret
