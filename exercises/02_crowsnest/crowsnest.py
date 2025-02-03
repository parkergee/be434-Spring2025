#!/usr/bin/env python3
"""
Author : Parker Geffre
Date   : 2025-02-02
Purpose: Crowsnest exercise
"""

import argparse
import os
import sys


def get_args():
    """get command line args"""
    parser = argparse.ArgumentParser(description='Announce the animal!')
    parser.add_argument('word', metavar = "word", help='Thing we see.')
    return parser.parse_args()


def main(): 
    """main"""
    args = get_args()
    word = args.word
    article = 'a'
    
    if word[0].lower() in 'aeiou':
        article = 'an'
    
    print(f"Ahoy, Captain, {article} {word.upper()} off the larboard bow!")


if __name__ == '__main__':
    main()