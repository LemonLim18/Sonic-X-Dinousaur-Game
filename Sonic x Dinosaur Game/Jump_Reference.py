import sys
import pygame
from pygame.locals import *
from pygame import mixer

class Jump(object):
    def __init__(self):
        self.jump_y = 280
        self.jump_speed = 20
        self.jump_status = False
        self.jump_able_click = True
        

    
if __name__ == '__main__':
    pygame.init()
    size = width,height = 600,500
    screen = pygame.display.set_mode(size) 
    title = pygame.display.set_caption("SONIC Jump")
    WHITE = (255,255,255)
    GREY = (50,50,50)
    clock = pygame.time.Clock()

    #jump image import
    jump_1 = pygame.image.load("image/jumproll/1.png").convert_alpha()
    jump_2 = pygame.image.load("image/jumproll/2.png").convert_alpha()
    jump_3 = pygame.image.load("image/jumproll/3.png").convert_alpha()
    jump_4 = pygame.image.load("image/jumproll/4.png").convert_alpha()
    jump_5 = pygame.image.load("image/jumproll/5.png").convert_alpha()
    jump_6 = pygame.image.load("image/jumproll/6.png").convert_alpha()
    jump_7 = pygame.image.load("image/jumproll/7.png").convert_alpha()
    jump_8 = pygame.image.load("image/jumproll/8.png").convert_alpha()
    jump_roll = pygame.image.load("image/jumproll/roll.png").convert_alpha()
    #All fifteen elements in list
    jump_list = [jump_1, jump_roll, jump_2,jump_roll, jump_3, jump_roll, jump_4, jump_roll, jump_5, jump_roll, jump_6, jump_roll, jump_7, jump_roll, jump_8]
    for x in range(len(jump_list)):
        jump_list[x] = pygame.transform.scale(jump_list[x], (88,88)) #88 IS THE VALUE REQUIRED!!!

    #Initial status
    run = True
    run_frame = 0
    jump_frame = 0
    roll = False
    """奔跑画面没有包括在这个程序里"""
    #User-defined event
    SONIC_ROLL = pygame.USEREVENT + 1
    pygame.time.set_timer(SONIC_ROLL,80)

    Jump = Jump()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and Jump.jump_able_click:
                if pygame.key.get_pressed()[K_DOWN]:
                    roll = True
            
                
                    
            if event.type == SONIC_ROLL and roll:
                jump_frame += 1
                if jump_frame > 14:
                    jump_frame = 0 

        

        #screen
        screen.fill(GREY)   
          
        screen.blit(jump_list[jump_frame],(250, Jump.jump_y))

        #update screen
        pygame.display.update()
