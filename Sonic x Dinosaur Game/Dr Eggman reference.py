import sys
import pygame
from pygame.locals import *

if __name__ == '__main__':
    pygame.init()
    
    size = width,height = 1100,702
    screen = pygame.display.set_mode(size)
    
    scale = 2.5

    #Dr Eggman的照片
    drEggman = pygame.image.load("image/drEggman/fly2.png").convert_alpha()
    drEggman = pygame.transform.scale(drEggman,(98*scale,81*scale))
    drEggman_x = -1800
    drEggman_y = 50
    rightmove = 0.5
    upmove = -20
    downmove = 20
    last_updated = pygame.time.get_ticks()
    animation_cooldown = 800
    
    while True:
        current_time = pygame.time.get_ticks()
        i = 1
        i += 2
        if current_time - last_updated == animation_cooldown:
            last_updated = current_time
            if i  % 2 == 0:
                drEggman_y += upmove
            elif i % 2 == 1:
                drEggman_y += downmove
            


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        drEggman_x += rightmove
        if drEggman_x >=800:
            drEggman_x = 800
            
        screen.fill((50,50,50))    
        screen.blit(drEggman,(drEggman_x,drEggman_y))
        
        pygame.display.update()