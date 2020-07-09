from datetime import date
import getopt
import sys


def get_arg(argv):
    day = 0
    month = 0
    year = 0

    try:
      opts, args = getopt.getopt(argv,'d:m:y:')
    except getopt.GetoptError:
      print('invalid arguments')
      sys.exit()
    else:
        for opt, arg in opts:
            if opt == '-d':
                day = arg
            elif opt == '-m':
                month = arg
            elif opt == '-y':
                year = arg
            else:
                print('invalid arguments')
                sys.exit()
        return int(day), int(month), int(year)


def check_input(day, month, year):
    if not (0 > day >= 31):
        print('e')


if __name__ == '__main__':
    day, month, year = get_arg(sys.argv[1:])
    check_input(day, month, year)

    now = date.today()

    print(day, month, year)