import pygame

black = (0, 0, 0)
white = (255, 255, 255)

# TEXT -------------------------------------------------------------------- #
class Text():

    def __init__(self, settings, answer):        
        self.characters = ''
        for i in range(len(answer)):
            self.characters = self.characters + '*'
        #
        self.font = pygame.font.Font(settings.font_path, settings.font_size)
        self.text = self.font.render(str(self.characters), True, white)
        self.text_rect = self.text.get_rect()
        #
        start = int((20 - len(answer)) / 2) + 1
        x = settings.letter_sx + start*settings.letter_width
        self.text_rect.x, self.text_rect.y = x, settings.letter_sy
    
    def update(self, number, character):
        new_text = ''
        for i in range(len(self.characters)):
            if self.characters[i] != '*':
                new_text += self.characters[i]
            elif i == number:
                new_text += character
            else:
                new_text += '*'
        self.characters = new_text
        self.text = self.font.render(self.characters, True, white)