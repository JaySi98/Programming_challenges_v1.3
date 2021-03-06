import pygame
import sys
import time
#
import game_logic as gl
import algorithms as alg
from settings import Settings

# MAIN --------------------------------------------------------------------- #
if __name__ == '__main__':
    # INITIALIZATION ------------------------------------------------------- #
    # settings
    settings = Settings()

    # parsing arguments to get the name of the algorithm
    name = gl.get_argument(sys.argv, settings)

    # window
    pygame.init()
    window = pygame.display.set_mode(settings.window_dim)
    pygame.display.set_caption(settings.window_caption)
    window.fill(pygame.Color("black"))
    
    # arrary to be sorted
    arr = gl.create_array(settings)


    # ANIMATION ------------------------------------------------------------ #
    alg.mix(window, settings, arr)
    time.sleep(1.5)
    gl.call_algorythm(window, settings, name, arr)

    # MAIN LOOP ------------------------------------------------------------ #
    while True:
        # checking game events
        for event in pygame.event.get():
            gl.check_events(event)
        
        # refreshing window 
        gl.update_window(window, settings, arr)