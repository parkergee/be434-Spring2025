#!/usr/bin/env python3
"""
Author : Parker Geffre <parkergeffre@arizona.edu>
Date   : 2025-02-25
Purpose: Jump the five.
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text.')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Encrypt a phone number"""

    args = get_args()
    text = args.text
    jumper = {'1':'9', '2':'8'} #dictionary here, go on and on.
    # if you have a character, need to use jumper.get, use default.
    
    new_text = ''
    
    for char in text: #take that text and turn it into a list of strings.
        #a string is iterable!!! 
        #want to print what's in the jumper table, if it doesnt exist - print what's in the string.
        new_text == jumper.get(char, char)
print(new_text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
