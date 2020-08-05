import sys
import pygame
import Piece 
import Settings
import Button

# LOADING STUFF ------------------------------------------------------------ #
# LOADING HANGMANS PARTS
def load_pieces(settings, pieces):
    for i in range(settings.pieces_num):
        new_piece = Piece.Piece(settings, i)
        pieces.append(new_piece)

# LOADING BUTTONS
def load_buttons(settings, buttons):
    sx, sy = settings.button_spos
    
    for i in range(settings.buttons_num):
        x = sx + (i%6)*80 
        y = sy + int(i/6)*80 #dokonczyc
        new_button = Button.Button(settings, i, [x,y])
        buttons.append(new_button)
    # last two y and z are hard coded as they cant be placed in loop
    button_y = Button.Button(settings, 24, [666,534])
    button_z = Button.Button(settings, 25, [746,534])
    buttons.append(button_y)
    buttons.append(button_z)


# CHECKING EVENTS ---------------------------------------------------------- #
# checks game events such as closing the game
def check_events(event, buttons):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONUP:
      pos = pygame.mouse.get_pos()
      check_button_pressed(pos, buttons)


# AUXILIARY FUNCTIONS ------------------------------------------------------ #
def check_button_pressed(pos, buttons):
    

# DRAWING ------------------------------------------------------------------ #
# refreshes the window
def update_window(window, background, pieces):
    window.blit(background.texture, background.rect)

    for piece in pieces:
        if piece.visible:
            window.blit(piece.texture, piece.rect)

    pygame.display.flip()


