import sys
import pygame
from pygame.sprite import Sprite

#BACKGROUND ---------------------------------------------------------------- #
class Background(Sprite):
    def __init__(self, settings):
        pygame.sprite.Sprite.__init__(self)
        self.texture = pygame.image.load(settings.background_path)
        self.rect = self.texture.get_rect()