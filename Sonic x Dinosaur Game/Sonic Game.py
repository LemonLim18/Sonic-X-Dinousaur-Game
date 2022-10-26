import sys
import pygame
from pygame.locals import *
from pygame import mixer
from tkinter import font
import random 
"""导入外面自建的公式&函数"""
from sprint_file import Sprint  #第一个是文件或来源名字，第二个是class的名字
from floor_file import Floor



"""本地的公式&函数"""    
def createMap():
    #Background
    screen.fill(color)
    screen.blit(background_image,(0,0))
    #Floor
    screen.blit(Floor.floor_image,(Floor.floor_x, Floor.floor_y))
    screen.blit(Floor.floor_image,(Floor.floor_x + 1272, Floor.floor_y))
    Floor.floor_animation()
    #Sonic
    if run == False:
        screen.blit(animation_list[sprint_frame],(100,490))
        #Switch to the run animation after a short sprint
    elif run == True:
        screen.blit(run_list[run_frame],(88,458))



"""主程序"""
if __name__ == '__main__':
    pygame.init()

    #窗口
    clock = pygame.time.Clock()
    size = width,height = 1100, 702
    screen = pygame.display.set_mode(size)
    color = (255,255,255)

    #背景音乐
    """For music, it's pygame.mixer.music.load or play; For soundtrack, it's pygame.mixer.sound()"""
    mixer.init()
    mixer.music.load("soundtrack/Angel Island Zone _ Act 1.mp3")
    mixer.music.play()
    mixer.music.set_volume(0.5)
    
    #背景图
    background_image = pygame.image.load("image/background.png").convert_alpha()
    background_image = pygame.transform.scale(background_image,(1100,702))

    #音速小子全速跑的照片
    run_1 = pygame.image.load("image/run/1.png").convert_alpha()
    run_2 = pygame.image.load("image/run/2.png").convert_alpha()
    run_3 = pygame.image.load("image/run/3.png").convert_alpha()
    run_4 = pygame.image.load("image/run/4.png").convert_alpha()
    run_5 = pygame.image.load("image/run/5.png").convert_alpha()
    run_6 = pygame.image.load("image/run/6.png").convert_alpha()
    run_7 = pygame.image.load("image/run/7.png").convert_alpha()
    run_8 = pygame.image.load("image/run/8.png").convert_alpha()
    
    run_list = [run_1, run_2,run_3,run_4,run_5,run_6,run_7,run_8]
    for i in range(8):
        run_list[i] = pygame.transform.scale(run_list[i],(158,145))
    run_frame = 0

    #实例(要创造实例才可以使用class里头的变数和函数)
    Floor = Floor() 
    Sprint = Sprint()

    #用户事件
    SONIC_RUN = pygame.USEREVENT #奔跑
    SONIC_JUMP = pygame.USEREVENT + 1 #跳跃
    #定时呼叫用户事件
    pygame.time.set_timer(SONIC_RUN,80)
    pygame.time.set_timer(SONIC_JUMP,80) #每隔

    #初始状态
    run = False
    jump = False

    #制造起跑动画
    sprint_frame = 0
    last_updated = pygame.time.get_ticks()
    animation_cooldown = 80
    animation_list = []
    animation_steps = 30
    for x in range(animation_steps):
        animation_list.append(Sprint.get_image(x ,45.2, 40, 3))


    while True:
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SONIC_RUN:
                run_frame += 1
                if run_frame > 7:
                    run_frame = 0
            
        
        current_time = pygame.time.get_ticks()
        if current_time - last_updated >= animation_cooldown:
            sprint_frame += 1
            Floor.leftmove += 0.2 #The floor accelerates in speed by 0.2
            if Floor.leftmove >= 5: #Once the speed reaches 5, it will hold on at 5
                Floor.leftmove = 5
            last_updated = current_time
            if sprint_frame >= 22: #Once the sprint is done, auto switch to running frame
                run = True
            
        createMap()
    
        pygame.display.update()

