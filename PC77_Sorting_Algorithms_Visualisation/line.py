import pygame

# LINE---------------------------------------------------------------------- #
class Line():
    def __init__(self, position, height, color):
        self.x, self.y = position
        self.height = height
        self.color = color