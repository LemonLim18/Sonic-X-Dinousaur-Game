import pygame
from pygame.locals import *

class Floor(object): #若是要叫唤某个class的变数，要创立一个实例，即object
    def __init__(self):
        self.floor_image = pygame.image.load("image/floor.jpg").convert_alpha()
        self.floor_image = pygame.transform.scale(self.floor_image,(1273,107))
        self.floor_x = 0
        self.floor_y = 602
        self.floor_rect = self.floor_image.get_rect()
        self.leftmove = 1

    def floor_animation(self):
        self.floor_x -= self.leftmove
        if self.floor_x < -190:
            self.floor_x = 0 