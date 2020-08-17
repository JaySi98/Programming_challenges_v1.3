import argparse
import sys


# MAIN -------------------------------------------------------------------- #
if __name__ == '__main__':
    # parsing arguments
    parser = argparse.ArgumentParser(
        description='Find triangular number')
    parser.add_argument('-n','--number', type=int,
        help='integer')
    args = parser.parse_args()
    
    # calcuating value of given number
    #T = (n)(n + 1) / 2.
    out = int(args.number *(args.number + 1) / 2)
    
    # printing output
    print('given number:', args.number)
    print('triangular number:', out)