import sys
import pygame
import random
#
from line import Line

# INITALIZATION ------------------------------------------------------------ #
def create_lines(settings):
    lines = []
    sx, sy = settings.line_init_pos
    init_height = settings.line_init_height
    color = settings.white
    for i in range(settings.lines_num):
        x = sx + settings.line_width*i + 1
        new_line = Line((x, sy), init_height+i, color) 
        lines.append(new_line)
    return lines

# CHECKING EVENTS ---------------------------------------------------------- #
# checks game events such as closing the game
def check_events(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        

# UPDATING ----------------------------------------------------------------- #
# refreshes the window
def update_window(window, settings, background, lines):
    window.blit(background.texture, background.rect)

    width = settings.line_width
    for i in range(len(lines)):
        #line(surface, color, start_pos, end_pos, width)
        start_pos = (lines[i].x, lines[i].y)
        end_pos = (lines[i].x, lines[i].y-lines[i].height)
        pygame.draw.line(window, lines[i].color, 
                        start_pos, end_pos, width)

    pygame.display.flip()
