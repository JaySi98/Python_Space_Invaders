import sys
import pygame
from pygame.sprite import Group
import game_logic as gl
from player import Player
from alien import Alien
from settings import Settings
from background import Background
from hp import Hearth
from text import Text

#Main 
def main():
    
    #settings initialization
    settings = Settings()

    #screen initialization
    pygame.init()
    screen = pygame.display.set_mode(settings.screen_dim)
    pygame.display.set_caption("Alien Invasion")

    #creating hearths
    hearths = []
    gl.createHearths(settings, hearths)

    #loading background image
    bg = Background(settings)

    #creating player
    player = Player(settings)

    #creating group to store inf about fired bullets
    bullets = Group()

    #creating aliens fleet
    aliens = Group()
    gl.createFleet(settings, aliens)

    #concept#########################################################################
    wave_counter = Text(settings)
    
    #Main loop of the game.
    while True:
        
        #checking keyboard events
        gl.checkEvents(settings, screen, player, bullets)
        
        if settings.game_active:
            #updating player
            player.update()

            #updating bullets
            gl.updateBullets(settings, aliens, bullets, wave_counter)

            #updating aliens
            gl.updateAliens(settings, screen, player, aliens, bullets, hearths)

            #updating screen
            gl.updateScreen(screen, bg, player, bullets, 
                            aliens, hearths, wave_counter)

        else:
            pygame.quit()
            sys.exit()

main()
