#!/usr/bin/env python3
"""
Author : Parker Geffre <parkergeffre@arizona.edu>
Date   : 2025-02-23
Purpose: Howler
"""

import argparse
import os
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler exercise',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')


    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')



    args = parser.parse_args()
    
    if os.path.isfile(args.text): #process input text from the user
        args.text = open(args.text().read().rstrip()) # we are going to overwrite
    
    return args
#upper()
#need to detect if args.out is made, then you need to open that as a file for writing text
#then put uppercase in there
#look into the sys module, STDOUD

#print('Hello', file = sys.stdout)

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    if args.out:
        print(args.text.upper(), file = open(args.out, 'wt')) #make uppercase
    else:
        print(args.text.upper())
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
