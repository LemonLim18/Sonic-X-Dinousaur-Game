import pygame
from pygame.locals import *

class Run(object):
    def __init__(self):
        #音速小子全速跑的照片
        self.run_1 = pygame.image.load("image/run/1.png").convert_alpha()
        self.run_2 = pygame.image.load("image/run/2.png").convert_alpha()
        self.run_3 = pygame.image.load("image/run/3.png").convert_alpha()
        self.run_4 = pygame.image.load("image/run/4.png").convert_alpha()
        self.run_5 = pygame.image.load("image/run/5.png").convert_alpha()
        self.run_6 = pygame.image.load("image/run/6.png").convert_alpha()
        self.run_7 = pygame.image.load("image/run/7.png").convert_alpha()
        self.run_8 = pygame.image.load("image/run/8.png").convert_alpha()
    
        self.run_list = [self.run_1, self.run_2, self.run_3, self.run_4, self.run_5, self.run_6, self.run_7, self.run_8]
        for i in range(8):
            self.run_list[i] = pygame.transform.scale(self.run_list[i],(158,145))