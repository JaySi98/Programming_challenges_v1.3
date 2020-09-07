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
        parser.add_argument('-n','--num', type=int, help='lenght of the array')
        args = parser.parse_args()
        if (args.alg in settings.alg_list 
        and (settings.lenght_bounds[0] <= args.num <= settings.lenght_bounds[1])):
            return args.alg, args.num
        else:
            print('Error, incorect arguments')
            sys.exit()

# CREATE_ARRAY ---------------------------------------------------------- #
# fills the array with random colors(r,g,b)
def create_array(settings, lenght):
    arr = []
    for i in range(lenght):
        color = settings.colors[i%len(settings.colors)]
        arr.append([i, color])
    #random.shuffle(arr) 
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
        x = settings.line_width * i
        y1 = dimensions[1] 
        y2 = dimensions[1] - arr[i][0]
        pygame.draw.line(window, arr[i][1], (x,y1), (x,y2), settings.line_width)

    # flipping the window
    pygame.display.flip()