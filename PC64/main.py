import argparse
import sys
import PIL

# PARSE ARGUMENT ------------------------------------------------------------- #
def parse_argument(argv):
    if len(argv) < 2:
        print('Error, not enough arguments')
        sys.exit()
    parser = argparse.ArgumentParser(description='Ulam Spiral')
    parser.add_argument('-n','--num', type=int, help='lenght of the spiral')
    args = parser.parse_args()
    if 1 <= args.num <= 600:
        return args.num
    else: 
        print('Error, incorrect argument')


# MAIN --------------------------------------------------------------------- #
if __name__ == '__main__':
    # parsing arguments to get the lenght of the spiral
    lenght = parse_argument(sys.argv)
    print('lenght:', lenght)
    
    # creating array 

    # creating image 

    '''        
    im = Image.new("RGB", (newwidth, height))
    im.putdata(colors)
    im.save("Picture", "PNG")
    '''


