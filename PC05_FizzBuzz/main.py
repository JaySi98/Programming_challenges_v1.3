import argparse
import sys

# MAIN --------------------------------------------------------------------- #
if __name__ == '__main__':
     # parsing arguments
    parser = argparse.ArgumentParser(description='FizzBuzz game.')
    parser.add_argument('-n','--num', type=int,help='number of numbers')
    args = parser.parse_args()

    for i in range(1,args.num + 1):
        if i%3==0 and i%5==0:
            print('FizzBuzz')
        elif i%3==0:
            print('Fizz')
        elif i%5==0:
            print('Buzz')
        else:
            print(i)