import pygame
from pygame.sprite import Sprite


# BUTTON ------------------------------------------------------------------- #
class Button():
    def __init__(self, settings, number, position):
        width = settings.button_width
        x, y = position
        self.rect = pygame.Rect(x, y, width, width)
        self.character = settings.buttons_chars[number]
        self.pressed = False

    def get_character(self):
        return self.character
    
    def set_pressed(self):
        self.pressed = True