import sys
import pygame
import random

# CHECKING EVENTS ---------------------------------------------------------- #
# checks game events such as closing the game
def check_events(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        

# UPDATING  ---------------------------------------------------------------- #
# refreshes the window
def update_window(window, background):
    window.blit(background.texture, background.rect)

    pygame.display.flip()
