import sys
import pygame
import random
#    

# CHECK_EVENTS ---------------------------------------------------------- #
# checks game events such as closing the game
def check_events(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        

# UPDATE_WINDOW ----------------------------------------------------------------- #
# refreshes the window
def update_window(window, settings):
    pygame.display.flip()