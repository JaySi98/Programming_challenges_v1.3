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

    # checking if given nuber is positive
    if args.number <= 0:
        print('argument must be positive intiger')
        sys.exit()

    # calcuating value of given number
    #T = (n)(n + 1) / 2.
    out = int(args.number *(args.number + 1) / 2)
    
    # printing output
    print('given number:', args.number)
    print('triangular number:', out)