import random
import pygame
#
import GameLogic as gl
from Background import Background
from Settings import Settings


# MAIN --------------------------------------------------------------------- #
if __name__ == '__main__':
    #settings initialization
    settings = Settings()

    #screen initialization
    pygame.init()
    window = pygame.display.set_mode(settings.screen_dim)
    pygame.display.set_caption("Rock Paper Scissors")

    #loading background texture
    background = Background(settings)

    #loading gesture textures

    #loading button textures 

    # MAIN LOOP ------------------------------------------------------------ #
    while True:
        #CHECKING EVENTS --------------------------------------------------- #
        for event in pygame.event.get():
            gl.check_events(event)

        #updating window with new matrix
        gl.update_window(window, background)  