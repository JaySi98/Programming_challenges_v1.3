import argparse
import datetime as dt
import sys

# MAIN --------------------------------------------------------------------- #
if __name__ == '__main__':
    # parsing arguments
    parser = argparse.ArgumentParser(
        description='Calculate your age in seconds')
    parser.add_argument('-d','--date', type=dt.date.fromisoformat,
        help='date of your birthday YYYY-MM-DD')
    args = parser.parse_args()
    
    # getting todays date
    today = dt.date.today()
    
    # calcuating difference in seconds
    diff = (today - args.date).days * 86400

    # printing the result 
    print('You are over ', diff ,' seconds old.')