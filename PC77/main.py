import pygame
import sys
import argparse
#
import game_logic as gl
import algorithms as alg
from settings import Settings


# MAIN --------------------------------------------------------------------- #
if __name__ == '__main__':
    # PARSING ARGUMENTS ---------------------------------------------------- #
    if len(sys.argv) < 2:
        print('Error, no algorithm was selected')
        sys.exit()
    else:
        parser = argparse.ArgumentParser(description='Sorting Algorithms Visualization')
        parser.add_argument('-a','--alg', type=str, help='algorithms name')
        args = parser.parse_args()
        al = algorithms[args.alg]
