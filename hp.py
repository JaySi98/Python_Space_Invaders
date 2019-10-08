import pygame
from pygame.sprite import Sprite

class Hearth(Sprite):

    def __init__(self, settings, x):
        super(Hearth, self).__init__()
        self.settings = settings

        self.image = pygame.image.load('images/hearth2.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = settings.hearth_y
