import pygame

black = (0, 0, 0)
white = (255, 255, 255)

class Text():

    def __init__(self, settings):
        self.font = pygame.font.Font('images/8-BIT WONDER.ttf', 25)

        self.text = self.font.render(str(settings.wave), True, white, black)
        self.text_rect = self.text.get_rect()
        self.text_rect.x = 140
        self.text_rect.y = 572
    
    def update(self, number):
        self.text = self.font.render(str(number), True, white, black)
