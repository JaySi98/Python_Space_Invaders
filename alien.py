import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, settings, x, y):
        super(Alien, self).__init__()
        self.settings = settings

        self.image = pygame.image.load('images/alien2.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def checkEdges(self):
        if self.rect.right >= self.settings.screen_dim[0]:
            return True
        elif self.rect.left <= 0:
            return True
        
        
    def update(self):
        self.rect.x += (self.settings.alien_x_speed *
                        self.settings.alien_direction)
         
