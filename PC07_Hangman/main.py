import random
import pygame
#
import GameLogic as gl
from Background import Background
from Piece import Piece
from Settings import Settings


# MAIN --------------------------------------------------------------------- #
if __name__ == '__main__':
    # INITIALIZATION ------------------------------------------------------- #
    #settings initialization
    settings = Settings()

    #screen initialization
    pygame.init()
    window = pygame.display.set_mode(settings.screen_dim)
    pygame.display.set_caption('Hangman')

    #loading background texture
    background = Background(settings)

    #loading hangmans textures 
    pieces = []
    gl.load_pieces(settings, pieces)

    #loading letters textures
    

    # GAME VARIABLES ------------------------------------------------------- # 
    counter = 0 # number missed letters, when it reaches 10, game ends


    # MAIN LOOP ------------------------------------------------------------ #
    while True:
        #CHECKING EVENTS --------------------------------------------------- #
        for event in pygame.event.get():
            gl.check_events(event)

        #updating window with new matrix
        gl.update_window(window, background, pieces)