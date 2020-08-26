import random
import pygame
#
from background import Background
import game_logic as gl
import algorithms as alg
from settings import Settings


# MAIN --------------------------------------------------------------------- #
if __name__ == '__main__':
    # INITIALIZATION ------------------------------------------------------- #

    # settings - all the parameters
    settings = Settings()

    # window
    pygame.init()
    window = pygame.display.set_mode(settings.window_dim)
    pygame.display.set_caption('Sorting Algorithms Visualization')

    # background texture
    background = Background(settings)

    # lines that will be sorted
    lines = gl.create_lines(settings)
    alg.mix_lines(lines)
    alg.selection_sort(lines)

    # MAIN LOOP ------------------------------------------------------------ #
    while True:
        # checking all game events
        for event in pygame.event.get():
            gl.check_events(event)

            # refreshing window 
            gl.update_window(window, settings, background, lines)