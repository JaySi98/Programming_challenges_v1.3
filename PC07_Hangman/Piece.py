import pygame
from pygame.sprite import Sprite


# PIECE ------------------------------------------------------------------- #
class Piece(Sprite):
    def __init__(self, settings, number):
        pygame.sprite.Sprite.__init__(self)
        self.texture = pygame.image.load(settings.piece_path[number])
        self.rect = self.texture.get_rect()
        self.rect.x, self.rect.y = settings.piece_position[number]