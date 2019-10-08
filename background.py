import pygame
from pygame.sprite import Sprite

class Background(Sprite):

    def __init__(self, settings):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(settings.screen_path)
        self.rect = self.image.get_rect()
        

        
