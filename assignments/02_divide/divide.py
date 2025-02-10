#!/usr/bin/env python3
"""
Author : Parker Geffre <parkergeffre@arizona.edu>
Date   : 2025-02-09
Purpose: To successfully divide two numbers.
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Divisor',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-i',
                        '--int',
                        help='A named integer argument',
                        metavar='int',
                        nargs='+',
                        type=int,
                        default=0)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Divide the integers"""

    args = get_args()
    int_arg = args.int
    
    if len(int_arg) > 2: #ensure no more than two args.
        print("usage : too many arguments.")
        quit(1) #set to 1 to output an error, 0 means success.
        
    num = int_arg[0]
    den = int_arg[1]
    
    if den == 0:
        print("Cannot divide by zero, dum-dum!")
        quit(1) #set to 1 to output an error, 0 means success.
        
    res = num / den 
    
    print(f"{num} / {den} = {res}")
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
