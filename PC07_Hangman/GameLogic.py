import sys
import pygame
import random
#
import Piece 
import Settings
import Button
import Text

# LOADING STUFF ------------------------------------------------------------ #
# LOADING BUTTONS
def load_buttons(settings, buttons):
    sx, sy = settings.button_spos
    
    for i in range(settings.buttons_num):
        x = sx + (i%6)*80 
        y = sy + int(i/6)*80 
        new_button = Button.Button(settings, i, [x,y])
        buttons.append(new_button)
    # last two y and z are hard coded as they cant be placed in loop
    button_y = Button.Button(settings, 24, [666,534])
    button_z = Button.Button(settings, 25, [746,534])
    buttons.append(button_y)
    buttons.append(button_z)


# UPDATING  ---------------------------------------------------------------- #
# refreshes the window
def update_window(window, background, pieces, text):
    window.blit(background.texture, background.rect)

    for i in range(len(pieces)):
        window.blit(pieces[i].texture, pieces[i].rect)

    window.blit(text.text, text.text_rect) 
    pygame.display.flip()


# CHECKING EVENTS ---------------------------------------------------------- #
# checks game events such as closing the game
def check_events(event, buttons, pressed):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        check_button_pressed(pos, buttons, pressed)

# 
def check_button_pressed(positon, buttons, pressed):
    x, y = positon
    width = buttons[0].rect.width
    for i in range(len(buttons)):
        bx, by = buttons[i].rect.x, buttons[i].rect.y
        if ((bx <= x <= bx + width) and (by <= y <= by + width) 
            and buttons[i].pressed == False):
            pressed.append(buttons[i].character)
            buttons[i].set_pressed()

# checking if chosen letter is in answer
def check_character(answer, pressed):
    if pressed[0] in answer:
        return True
    else:
        return False


# AUXILIARY FUNCTIONS ------------------------------------------------------ #
# returns randomn answer 
def select_answer(settings):
    num = random.randint(1, settings.lines_size)
    file = open("resources/answers.txt", "r")
    
    for i, line in enumerate(file):
        if i == num:
           file.close() 
           return line[:-1]




# TEST -------------------------------------------------------------------- #
def update_text(text, pressed, answer):
    char = pressed[0]
    for i in range(len(answer)):
        if char == answer[i]:
            text.update(i, char)

def add_piece(pieces, settings, missed):
    new_piece = Piece.Piece(settings, missed)
    pieces.append(new_piece)


def check_game_end(guessed, missed, answer):
    if missed == 10:
        print('you lost')
        return True

    for i in range(len(answer)):
        if answer[i] not in guessed:
            return False
    print('you win')
    return True

