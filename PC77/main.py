import pygame
import sys
import multiprocessing as mp 
#
import game_logic as gl
import algorithms as alg
from settings import Settings

'''
CO MOZNA POPRAWIC 
- sortowanie po wielkosci ale kolorowe słupki
- wiecej agrumentow(ilosc linii)
- wiecej algorytmow
'''

# MAIN --------------------------------------------------------------------- #
if __name__ == '__main__':
    # INITIALIZATION ------------------------------------------------------- #
    # settings
    settings = Settings()

    # parsing arguments to get the name of the algorithm
    name = gl.get_argument(sys.argv, settings)
    algorithm = getattr(alg, name)

    # window
    pygame.init()
    window = pygame.display.set_mode(settings.window_dim)
    pygame.display.set_caption(settings.window_caption)
    window.fill(pygame.Color("black"))
    
    # arrary to be sorted
    arr = gl.create_array(settings)


    # ANIMATION ------------------------------------------------------------ #
    call = algorithm(window, settings, arr)


    # MAIN LOOP ------------------------------------------------------------ #
    while True:
        # checking game events
        for event in pygame.event.get():
            gl.check_events(event)
        
        # refreshing window 
        gl.update_window(window, settings, arr)