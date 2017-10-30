"""
load_clean_liber_primus.py

    Example file showing how to load the Liber Primus data from a formatted
    text file into a dictionary and saved to be further analyzed in python.

@author: Douglas Daly
@date: 10/30/2017
"""
#
#   Imports
#
import pickle

from sphecius.data import load_text_from_file

#
#   Functions
#

def clean_line(line):
    """ Cleans a single line
    """
    ret = line.replace('-', ' ').replace('.', '. ').strip()
    return ret

def clean_file_input(raw_data):
    """ Cleans the bulk of the full file contents

    The result will be a dictionary with each page, and each page will be a
    dictionary of the full page contents in key 0, and then each line starting
    with 1, though some sections & lines will require additional cleaning.

    :param dict raw_data: Raw dictionary from file load

    :return: Clean(er) dictionary of file contents
    :rtype: dict

    """
    clean_lp_dict = dict()
    for section, text in raw_data.items():
        temp_full = "".join(text[0].split('\n'))
        temp_lines = temp_full.split('/')

        temp_dict = dict()
        temp_dict[0] = clean_line(temp_full).replace('/', '').strip()

        c_idx = 1
        for line in temp_lines:
            if line.strip():
                temp_dict[c_idx] = clean_line(line)
                c_idx += 1

        clean_lp_dict[section] = temp_dict

    return clean_lp_dict

#
#   Main
#

if __name__ == "__main__":
    # Load File Contents
    lp_dict = load_text_from_file("./liber_primus_transcription_full.txt",
                                  section_divider="%",
                                  skip_lines_starting_with=['&', '$', '*',
                                                            '/'])

    # Clean file contents
    clean_lp_dict = clean_file_input(lp_dict)

    # Pickle results
    with open("lp_full_clean.pkl", "wb") as fout:
        pickle.dump(clean_lp_dict, fout)
