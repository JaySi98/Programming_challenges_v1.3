import sys
import pygame
import random
import argparse
#    
import settings

# GET_ARGUMENT ---------------------------------------------------------- #
# chekcs given arguments and returns the name of the selected algorithm
def get_argument(argv, settings):
    if len(argv) < 2:
        print('Error, no algorithm was selected')
        sys.exit()
    else:
        parser = argparse.ArgumentParser(description='Sorting Algorithms Visualization')
        parser.add_argument('-a','--alg', type=str, help='algorithms name')
        args = parser.parse_args()
        if args.alg in settings.alg_list:
            return args.alg
        else:
            print('Error, incorect argument')
            sys.exit()

# CREATE_ARRAY ---------------------------------------------------------- #
# fills the array with random unique values
def create_array(settings):
    arr = [i for i in range(settings.arr_len)]
    random.shuffle(arr)
    return arr


# CHECK_EVENTS ---------------------------------------------------------- #
# checks game events such as closing the game
def check_events(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        

# UPDATE_WINDOW ----------------------------------------------------------------- #
# refreshes the window
def update_window(window, settings, arr):
    # black background
    window.fill(settings.black)

    # array values as white lines
    dimensions = settings.window_dim
    for i in range(len(arr)):
        x = i*2
        y1 = dimensions[1] 
        y2 = dimensions[1] - arr[i]
        pygame.draw.line(window, settings.white, (x,y1), (x,y2), 2)

    # flipping the window
    pygame.display.flip()