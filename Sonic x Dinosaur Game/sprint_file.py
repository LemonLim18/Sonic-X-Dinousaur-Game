import pygame
from pygame.locals import *

class Sprint(object):
    def __init__(self):
        self.sheet = pygame.image.load("image/sprint_sheet.png").convert_alpha()

    def get_image(self,frame,width,height,scale):
        self.image = pygame.Surface((width,height)).convert_alpha()
        self.image.fill((255,255,255))
        self.image.blit(self.sheet,(0,0),(frame*width,0,width,height))
        self.image = pygame.transform.scale(self.image,(width*scale,height*scale))
        self.image.set_colorkey((255,255,255))
        return self.image