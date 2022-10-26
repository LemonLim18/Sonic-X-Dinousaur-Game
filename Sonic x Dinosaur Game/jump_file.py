import pygame
from pygame.locals import *

class Jump(object):
    def __init__(self):
        #照片
        #音速小子跳跃的照片
        self.jump_1 = pygame.image.load("image/jumproll/1.png").convert_alpha()
        self.jump_2 = pygame.image.load("image/jumproll/2.png").convert_alpha()
        self.jump_3 = pygame.image.load("image/jumproll/3.png").convert_alpha()
        self.jump_4 = pygame.image.load("image/jumproll/4.png").convert_alpha()
        self.jump_5 = pygame.image.load("image/jumproll/5.png").convert_alpha()
        self.jump_6 = pygame.image.load("image/jumproll/6.png").convert_alpha()
        self.jump_7 = pygame.image.load("image/jumproll/7.png").convert_alpha()
        self.jump_8 = pygame.image.load("image/jumproll/8.png").convert_alpha()
        self.jump_roll = pygame.image.load("image/jumproll/roll.png").convert_alpha()
        #All fifteen elements in list
        self.jump_list = [self.jump_1, self.jump_2, self.jump_3, self.jump_4, self.jump_5, self.jump_6, self.jump_7, self.jump_roll, self.jump_8]
        
        for x in range(1,14,2):
            self.jump_list.insert(x,self.jump_roll)

        for y in range(len(self.jump_list)):
            self.jump_list[y] = pygame.transform.scale(self.jump_list[y], (84,84)) #88 IS THE VALUE REQUIRED!!!
        #移动数据
        self.jump_y = 420
        self.jump_speed = 20
        self.jump_status = False
        self.jump_able_click = True
        

    def update_jumpHeight(self):
        if self.jump_status:
            self.jump_speed -= 0.80 #这个1就好比是gravitational acceleration
            self.jump_y -= self.jump_speed
            self.jump_able_click = False  #while in the mid-air, unable to jump again

        if self.jump_y >= 420:
            self.jump_y = 420  #Make it stop at height of 420
            self.jump_status = False
            self.jump_able_click = True  #once it descends to the land, it can jump again