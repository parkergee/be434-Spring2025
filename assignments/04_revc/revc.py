#!/usr/bin/env python3
"""
Author : Parker Geffre <parkergeffre@arizona.edu>
Date   : 2025-02-25
Purpose: Will accept a string of DNA either or a filename containing the DNA and will print the reverse complement.
"""

import argparse
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print the reverse complement of DNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('DNA',
                        metavar='DNA',
                        help='Input sequence or file.')
    
    args = parser.parse_args()

    if os.path.isfile(args.DNA):
        args.DNA = open(args.DNA).read().rstrip()

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Reverse complement"""

    args = get_args()
    DNA = args.DNA
    dnapol = {'A':'T', 'C':'G', 'a':'t', 'c':'g', 'T':'A', 'G':'C', 't':'a', 'g':'c'} #dictionary here, go on and on.
    # Cannot assume T will be made into A if define A:T
    forward = '' #make forward seq
    reversed = '' #make reverse seq
    for char in DNA:
        forward += dnapol.get(char, char)
    reversed += forward[::-1] #have to use +-?????
    print(reversed)

# --------------------------------------------------
if __name__ == '__main__':
    main()
