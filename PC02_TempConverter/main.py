import getopt
import sys


def get_arg(argv):
    temperature = 0
    
    try:
      opts, args = getopt.getopt(argv,'f:c:k:')
    except getopt.GetoptError:
      print('invalid arguments')
      sys.exit()
    except len(argv) != 3:
        print('invalid number of arguments')
        sys.exit()
    else:
        for opt, arg in opts:
            if opt in ('-f', '-c', '-k'):
                temperature = arg
                return str(opt)[1:], int(temperature)
        else:
            print('invalid arguments')
            sys.exit()


def convert(scale, temp):
    kelvin = 0 
    far = 0
    celc = 0

    if scale == 'f':
        far = temp
        celc = (temp - 32) * (5/9)
        kelvin = celc + 273.15 
    elif scale == 'c':
        celc = temp
        kelvin = temp + 273.15
        far = (temp + 32) * (9/5)
    elif scale == 'k':
        celc = temp - 273.15
        kelvin = temp 
        far = (celc - 32) * (5/9)
    
    print('Kelvin: ', kelvin)
    print('Celsius: ', celc)
    print('Fahrenheit: ', far)


if __name__ == '__main__':
    scale, temp = get_arg(sys.argv[1:])
    convert(scale, temp)