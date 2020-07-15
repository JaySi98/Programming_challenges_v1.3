import sys
import pygame

#CHECKING EVENTS ----------------------------------------------------------- #
#checks game events such ass closing the game
def check_events(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


#DRAWING -----------------------------------------------------------
#refreshes the window
def update_window(window, background):
    window.blit(background.texture, background.rect)
    pygame.display.flip()