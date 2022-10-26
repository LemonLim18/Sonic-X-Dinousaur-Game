import pygame
from pygame.locals import *

class Background(object):
    def __init__(self):
        #背景图
        self.background_image = pygame.image.load("image/background.png").convert_alpha()
        self.background_image = pygame.transform.scale(self.background_image,(1100,702))
        self.background_x = 0   

    def update_background(self):
        self.background_x -= 0.15
        if self.background_x <= -1100:
            self.background_x = 0