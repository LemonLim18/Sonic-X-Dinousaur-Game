import sys
import pygame
from pygame.locals import *
from pygame import mixer
from tkinter import font
import random 
"""导入外面自建的公式&函数"""
from background_file import Background
from floor_file import Floor    #第一个是文件或来源名字，第二个是class的名字
from sprint_file import Sprint 
from run_file import Run
from jump_file import Jump
from spindash_file import Spindash


"""本地的公式&函数"""
def createMap():
    #Background
    screen.fill(color)
    screen.blit(Background.background_image,(Background.background_x, 0))
    screen.blit(Background.background_image,(Background.background_x+1100, 0))
    Background.update_background()
    #Floor
    screen.blit(Floor.floor_image,(Floor.floor_x, Floor.floor_y))
    screen.blit(Floor.floor_image,(Floor.floor_x + 1272, Floor.floor_y))
    Floor.floor_animation()
    #Sonic
    if sprint and not run:
        screen.blit(animation_list[sprint_frame],(100,490))
        #Switch to the run animation after a short sprint
    elif run and not Jump.jump_status and not spindash:
        screen.blit(Run.run_list[run_frame],(88,458))
    elif Jump.jump_status and not spindash:
        screen.blit(Jump.jump_list[jump_frame],(137, Jump.jump_y))
    elif spindash :
        screen.blit(Spindash.spindash_list[spindash_frame],(110,524))
        screen.blit(Spindash.dust_list[dust_frame],(45,536))
    
    Jump.update_jumpHeight()  #不能include在任何一个if函数里，不然的话就不能把jump_status变回false了  

"""主程序"""
if __name__ == '__main__':
    pygame.init()

    #窗口
    clock = pygame.time.Clock()
    size = width,height = 1100, 702
    screen = pygame.display.set_mode(size)
    color = (255,255,255)

    #背景音乐
    """For music, it's pygame.mixer.music.load or play; For soundtrack, it's pygame.mixer.Sound()"""
    mixer.init()
    mixer.music.load("soundtrack/Angel Island Zone _ Act 1.mp3")
    mixer.music.play()
    mixer.music.set_volume(0.5)

    #动作音乐
    #(跳跃)
    jump_sound = mixer.Sound("soundtrack/jump.wav")
    jump_sound.set_volume(0.42)
    #(滚动)
    spindash_sound = mixer.Sound("soundtrack/spindash.wav")
    spindash_sound.set_volume(0.06)


    #实例(要创造实例才可以使用class里头的变数和函数)
    Background = Background()
    Floor = Floor() 
    Sprint = Sprint()
    Run = Run()
    Jump = Jump()
    Spindash = Spindash()


    #初始状态
    sprint = True
    sprint_frame = 0
    run = False
    run_frame = 0
    jump = False
    jump_frame = 0
    spindash = False
    spindash_frame = 0
    dust_frame = 0


    #用户事件
    SONIC_RUN = pygame.USEREVENT #奔跑
    SONIC_JUMP = pygame.USEREVENT + 1 #跳跃
    SONIC_SPINDASH = pygame.USEREVENT + 2
    #定时呼叫用户事件
    pygame.time.set_timer(SONIC_RUN,80)
    pygame.time.set_timer(SONIC_JUMP,80) #每隔0.08秒呼叫一次
    pygame.time.set_timer(SONIC_SPINDASH,20)
    
    
    #制造起跑动画
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
            if event.type == pygame.KEYDOWN and Jump.jump_able_click:
                if (event.key == K_SPACE or event.key == K_UP or event.key == K_w) and not sprint:
                    run = False
                    Jump.jump_status = True
                    Jump.jump_speed = 20
                    spindash = False
                    jump_sound.play()
                elif (event.key == K_DOWN or event.key == K_s) and not sprint:
                    if pygame.key.get_pressed()[K_DOWN] == 1 or pygame.key.get_pressed()[K_s] == 1:
                        run = False
                        Jump.jump_status = False
                        spindash = True
                    spindash_sound.play()

            if event.type == SONIC_RUN:
                run_frame += 1
                if run_frame > 7:
                    run_frame = 0
            if event.type == SONIC_JUMP and Jump.jump_status:
                jump_frame += 1
                if jump_frame > 14:
                    jump_frame = 0
            if event.type == SONIC_SPINDASH:
                spindash_frame += 1
                dust_frame += 1
                if spindash_frame > 5:
                    spindash_frame = 0
                if dust_frame > 5:
                    dust_frame = 0
            
        
        current_time = pygame.time.get_ticks()
        if current_time - last_updated >= animation_cooldown:
            sprint_frame += 1
            Floor.leftmove += 0.2 #The floor accelerates in speed by 0.2
            if Floor.leftmove >= 5: #Once the speed reaches 5, it will hold on at 5
                Floor.leftmove = 5
            last_updated = current_time
            if sprint_frame >= 22: #Once the sprint is done, auto switch to running frame
                sprint = False
                run = True
            
        createMap()
    
        pygame.display.update()

