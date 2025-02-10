#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-02-09
Purpose: Add Your Purpose
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Add Your Purpose',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs = '+',#number of args needs to be more
                        help='Items we are bringing')
    
    parser.add_argument('-s', #when its absent, its false
                        '--sorted',
                        help='Whether to sort the items',
                        action = 'store_true') #when its not present, the default value is false
    
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    print(args.items) #get it from there, makes a list.


# --------------------------------------------------
if __name__ == '__main__':
    main()
