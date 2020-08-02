import sys
import pygame
import Piece 
import Settings

#CHECKING EVENTS ----------------------------------------------------------- #
#checks game events such ass closing the game
def check_events(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


#DRAWING -----------------------------------------------------------
#refreshes the window
def update_window(window, background, pieces):
    window.blit(background.texture, background.rect)

    for piece in pieces:
        if piece.visible:
            window.blit(piece.texture, piece.rect)

    pygame.display.flip()


#LOADING HANGMANS PARTS
def load_pieces(settings, pieces):
    for i in range(settings.number_pieces):
        new_piece = Piece.Piece(settings, i)
        pieces.append(new_piece)