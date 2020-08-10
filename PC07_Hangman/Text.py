import pygame

black = (0, 0, 0)
white = (255, 255, 255)

# TEXT -------------------------------------------------------------------- #
class Text():

    def __init__(self, settings, answer):        
        self.answer = answer
        self.show = ''
        for i in range(len(self.answer)):
            self.show = self.show + '*'
        #
        self.font = pygame.font.Font(settings.font_path, settings.font_size)
        self.text = self.font.render(str(self.show), True, white)
        self.text_rect = self.text.get_rect()
        #
        start = int((20 - len(answer)) / 2)
        x = settings.letter_sx + start*settings.letter_width
        self.text_rect.x, self.text_rect.y = x, settings.letter_sy
    
    def update(self):
        pass#self.text = self.font.render(str(number), True, white, black)



'''
import pygame
from pygame.sprite import Sprite


# LETTER ------------------------------------------------------------------ #
class Letter(Sprite):
    def __init__(self, settings, position, character):
        pygame.sprite.Sprite.__init__(self)
        self.texture = pygame.image.load(settings.letter_path)

        self.position = position
        self.character = character
        self.visible = False
    
    def make_visible(self):
        self.visible = True
    
    def get_character(self):
        return self.character
'''