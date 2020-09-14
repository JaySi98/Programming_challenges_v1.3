import sys
import pygame
import random
import argparse
import math
#    
import settings
import algorithms as alg

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
        if (args.alg in settings.alg_list):
            return args.alg
        else:
            print('Error, incorrect argument')
            sys.exit()

# CREATE_ARRAY ---------------------------------------------------------- #
# fills the array with random colors(r,g,b)
def create_array(settings):
    arr = []
    step = round(settings.color_lenght / settings.lenght)
    red = 255
    green = 0
    blue = 0
    value = 0

    for i in range(0, settings.color_lenght+1, step):
        value += 1
        if i > 0 and i <= 255:
            blue += step
        elif i > 255 and i <= 255*2:
            red -= step
        elif i > 255*2 and i <= 255*3:
            green += step
        elif i > 255*3 and i <= 255*4:
            blue -= step
        elif i > 255*4 and i <= 255*5:
            red += step
        elif i > 255*5 and i <= 255*6:
            green -= step
        color = (red, green, blue)
        arr.append([value, color]) 
    return arr


# CALL_ALGORYTHM -------------------------------------------------------- #
def call_algorythm(window, settings, name, arr):
    algorithm = getattr(alg, name)
    if name in ['merge_sort', 'quick_sort']:
        call = algorithm(window, settings, arr, 0, len(arr)-1)
    else:
        call = algorithm(window, settings, arr)


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



    '''
    def create_array(settings, lenght):
    arr = []
    for i in range(lenght):
        color = settings.colors[i%len(settings.colors)]
        arr.append([i, color]) 
    return arr

    ########################################################

    def create_array(settings, lenght):
    arr = []
    specratio = 255*6 / lenght
    step = round(specratio)
    red = 255
    green = 0
    blue = 0

    for i in range(0, 255*6+1, step):
        if i > 0 and i <= 255:
            blue += step
        elif i > 255 and i <= 255*2:
            red -= step
        elif i > 255*2 and i <= 255*3:
            green += step
        elif i > 255*3 and i <= 255*4:
            blue -= step
        elif i > 255*4 and i <= 255*5:
            red += step
        elif i > 255*5 and i <= 255*6:
            green -= step
        color = (red, green, blue)
        arr.append([i, color]) 
    return arr
    '''