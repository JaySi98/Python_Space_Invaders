import pygame
import sys
from time import sleep
from bullet import Bullet
from alien import Alien
from hp import Hearth

##############################creating aliens##################################

def createFleet(settings, aliens):
    for row in range(settings.wave_spec[settings.wave][1]):
        for col in range(settings.wave_spec[settings.wave][0]):
            x = ((settings.wave_spec[settings.wave][2] * (col +1)) +
                (settings.alien_width * col))

            y = ((settings.wave_spec[settings.wave][2] * (row +1)) +
                (settings.alien_width * row) + settings.screen_gap)

            alien = Alien(settings, x, y)
            aliens.add(alien)

############################checking events#####################################
def checkEvents(settings, screen, player, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            endGame(settings)

        elif event.type == pygame.KEYDOWN:
            keydown_events(event, settings, screen, player, bullets)

        elif event.type == pygame.KEYUP:
            keyup_events(event, player)

def keydown_events(event, settings, screen, player, bullets):
    if event.key == pygame.K_RIGHT:
        player.moving_right = True

    elif event.key == pygame.K_LEFT:
        player.moving_left = True

    elif event.key == pygame.K_SPACE:
        fireBullet(settings, screen, player, bullets)

    elif event.key == pygame.K_q:
        settings.game_active = False

def keyup_events(event, player):
    if event.key == pygame.K_RIGHT:
        player.moving_right = False

    elif event.key == pygame.K_LEFT:
        player.moving_left = False


def endGame(settings):
    #print(settings.wave)
    settings.game_active = False
    
#################################updating screen################################
def updateScreen(screen, bg, player, bullets, aliens, hearths, wave_counter):
    screen.blit(bg.image, bg.rect)
    for bullet in bullets.sprites():
        bullet.draw()

    aliens.draw(screen)
    screen.blit(player.image, player.rect)
    for hearth in hearths:
        screen.blit(hearth.image, hearth.rect)
    screen.blit(wave_counter.text, wave_counter.text_rect) 
    pygame.display.flip()

def createHearths(settings, hearths):
    for hearth in range(settings.player_max_hp + 1):
        x = settings.hearth_x - (hearth * settings.screen_gap) - hearth
        hr = Hearth(settings, x)
        hearths.append(hr)
    
#########################updating aliens########################################
def updateAliens(settings, screen, player, aliens, bullets, hearths):
    checkAliensEdges(settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(player, aliens):
        playerHit(settings, screen, player, aliens, bullets, hearths)

    checkAliensBottom(settings, screen, player, aliens, bullets, hearths)
    
def changeAliensDirection(settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.alien_y_speed
    settings.alien_direction *= -1.0

def checkAliensEdges(settings, aliens):
    for alien in aliens.sprites():
        if alien.checkEdges():
            changeAliensDirection(settings, aliens)
            break

def checkAliensBottom(settings, screen, player, aliens, bullets, hearths):
    for alien in aliens.sprites():
        if alien.rect.bottom >= settings.screen_dim[1] - settings.screen_gap:
            playerHit(settings, screen, player, aliens, bullets, hearths)
            break

def playerHit(settings, screen, player, aliens, bullets, hearths):
    if settings.player_hp > 0:
        settings.player_hp -= 1
        aliens.empty()
        bullets.empty()
        createFleet(settings, aliens)
        player.centerPlayer()
        sleep(0.5)
    else:
        endGame(settings)

    hearths.pop()
################################updating bullets###############################
def updateBullets(settings, aliens, bullets,  text):
    #updating bullets position
    bullets.update()

    #deleting offscreen bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
    checkBulletCollision(settings, aliens, bullets, text)

#adding new bullet to the group
def fireBullet(settings, screen, player, bullets):
    new_bullet = Bullet(settings, screen, player)
    bullets.add(new_bullet)

#checking colisions between bullets and aliens
def checkBulletCollision(settings, aliens, bullets, text):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        if settings.wave == settings.wave_max:
            settings.alien_y_speed += 1
            createFleet(settings, aliens)
            #endGame(settings)
        else:
            settings.wave += 1
            bullets.empty()
            createFleet(settings, aliens)

        settings.wave_counter += 1
        text.update(settings.wave_counter)
