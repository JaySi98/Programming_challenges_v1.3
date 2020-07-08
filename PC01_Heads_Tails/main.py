import getopt
import sys
import random


def get_arg(argv):
    num = 1
    
    try:
      opts, args = getopt.getopt(argv,'n:')
    except getopt.GetoptError:
      print('invalid arguments')
      sys.exit()
    else:
        for opt, arg in opts:
            if opt == '-n':
                num = arg
                return num
        return num


if __name__ == '__main__':
    num = int(get_arg(sys.argv[1:]))
    heads, tails = 0, 0

    for i in range(num):
        r = random.randint(0,1)
        if r:
            heads += 1
        else:
            tails += 1

    print('Number of coin flips: ', num)
    print('Number of heads: ', heads)
    print('Number of tails: ', tails)
