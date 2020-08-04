import pygame
from pygame.sprite import Sprite


# BUTTON ------------------------------------------------------------------- #
class Button():
    def __init__(self, settings, number, position):
        self.rect = (settings.button_width, settings.button_width)
        self.rect.x, self.rect.y = position
        self.character = settings.buttons_chars[number]
    
    def get_character(self):
        return self.character