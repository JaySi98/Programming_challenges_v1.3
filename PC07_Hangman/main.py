import random
import pygame
#
import GameLogic as gl
from Background import Background
from Piece import Piece
from Settings import Settings
import Text

# MAIN --------------------------------------------------------------------- #
if __name__ == '__main__':
    # INITIALIZATION ------------------------------------------------------- #
    # settings initialization
    settings = Settings()

    # screen initialization
    pygame.init()
    window = pygame.display.set_mode(settings.screen_dim)
    pygame.display.set_caption('Hangman')

    # loading background texture
    background = Background(settings)

    # loading buttons
    buttons = [] 
    gl.load_buttons(settings, buttons)

    # hangmans textures 
    pieces = []

    # creating answer to find
    # selecting random answer from txt file
    answer = gl.select_answer(settings)
    #creating text to be displayed
    text = Text.Text(settings, answer)


    # GAME VARIABLES ------------------------------------------------------- # 
    missed = 0             # number missed letters, if reaches 10, game ends
    guessed = []           # list of letter that player already guessed 
    pressed = []           # pressed characters


    # MAIN LOOP ------------------------------------------------------------ #
    while True:
        # checking if mouse was pressed
        for event in pygame.event.get():
            gl.check_events(event, buttons, pressed)

        if settings.game_active == True:
            if pressed:
                # checking if pressed letter is correct
                if gl.check_character(answer, pressed) == True:
                    gl.update_text(text, pressed, answer)
                    guessed.append(pressed[0])
                else:
                    gl.add_piece(pieces, settings, missed)
                    missed += 1
                pressed.pop()

            # checking if palyer either won or lost
            if gl.check_game_end(guessed, missed, answer):
                settings.game_active = False

            # refreshing window 
            gl.update_window(window, background, pieces, text)