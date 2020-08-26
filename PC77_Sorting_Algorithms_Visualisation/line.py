import pygame

# LINE---------------------------------------------------------------------- #
class Line():
    def __init__(self, position, height, color):
        self.x, self.y = position
        self.height = height
        self.color = color

    def get_height(self):
        return self.height

    def set_height(self, new_height):
        self.height = new_height