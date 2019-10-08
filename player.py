import pygame

class Player():

    def __init__(self, settings):
        self.settings = settings
        
        #loading image 
        self.image = pygame.image.load('images/player2.bmp')
        self.rect = self.image.get_rect()

        #setting starting position
        self.rect.centerx = self.settings.player_start_pos[0]
        self.rect.bottom = self.settings.player_start_pos[1]
        self.center = float(self.rect.centerx)

        #movement flags
        self.moving_right = False
        self.moving_left = False

    def centerPlayer(self):
        self.center = self.settings.player_start_pos[0]

    def update(self):
        if self.moving_right and self.rect.right <= self.settings.screen_dim[0]:
            self.center += self.settings.player_speed_factor

        if self.moving_left and self.rect.left >= 0:
            self.center -= self.settings.player_speed_factor

        self.rect.centerx = self.center
