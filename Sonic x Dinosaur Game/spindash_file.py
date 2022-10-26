import pygame
from pygame.locals import *

class Spindash(object):
    def __init__(self):
        #照片
        #音速小子跳跃的照片
        self.spindash_1 = pygame.image.load("image/spindash/1.png").convert_alpha()
        self.spindash_2 = pygame.image.load("image/spindash/2.png").convert_alpha()
        self.spindash_3 = pygame.image.load("image/spindash/3.png").convert_alpha()
        self.spindash_4 = pygame.image.load("image/spindash/4.png").convert_alpha()
        self.spindash_5 = pygame.image.load("image/spindash/5.png").convert_alpha()
        self.spindash_6 = pygame.image.load("image/spindash/6.png").convert_alpha()
        #All six elements in list
        self.spindash_list = [self.spindash_1, self.spindash_2, self.spindash_3, self.spindash_4, self.spindash_5, self.spindash_6]

        for x in range(len(self.spindash_list)):
            self.spindash_list[x] = pygame.transform.scale(self.spindash_list[x], (110,80)) #88 IS THE VALUE REQUIRED!!!


        #灰尘的照片
        self.dust_1 = pygame.image.load("image/dust/1.png").convert_alpha()
        self.dust_2 = pygame.image.load("image/dust/2.png").convert_alpha()
        self.dust_3 = pygame.image.load("image/dust/3.png").convert_alpha()
        self.dust_4 = pygame.image.load("image/dust/4.png").convert_alpha()
        self.dust_5 = pygame.image.load("image/dust/5.png").convert_alpha()
        self.dust_6 = pygame.image.load("image/dust/6.png").convert_alpha()
        #All six elements in list
        self.dust_list = [self.dust_1, self.dust_2, self.dust_3, self.dust_4, self.dust_5, self.dust_6]

        for x in range(len(self.dust_list)):
            self.dust_list[x] = pygame.transform.scale(self.dust_list[x], (93,70)) #88 IS THE VALUE REQUIRED!!!