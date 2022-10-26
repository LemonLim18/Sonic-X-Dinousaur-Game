import pygame

def get_image(sheet,frame,width,height,scale,color):
    image = pygame.Surface((width,height)).convert_alpha() #Setting a new black-color surface with specified width and height
    image.fill(WHITE)
    #remember that blit can be used onto any pygame surface,thus
    image.blit(sheet,(0,0),(frame*width,0,width,height))
    #(0,0,width,height) labels the area of the part that you want to crop,from a point to another with the mean of coordinates
    #Enlarged the entire surface along with the element inside it  
    image = pygame.transform.scale(image,(width*scale,height*scale))
    #The color that is same as the specified color will be transparent
    image.set_colorkey(color)
    return image #Return a image


pygame.init()

size = width,height = 500,500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
bg_color = (50,50,50)
pygame.display.set_caption("Sonic Animation")

#sprite animation
sprite_sheet_image = pygame.image.load("image/run_sheet.png").convert_alpha()
BLACK = (0,0,0)
WHITE = (255,255,255)

#create animation list
animation_list = []
animation_steps = 30
#get_ticks() returns the number of milliseconds since pygame.init() was called
last_updated = pygame.time.get_ticks()
animation_cooldown = 100  #ori 100
frame = 0

for x in range(animation_steps):
    animation_list.append(get_image(sprite_sheet_image, x, 45.2, 40, 3, WHITE))


run = True
while run:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #update background color
    screen.fill(bg_color)

    #update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_updated >= animation_cooldown:
        frame += 1
        last_updated = current_time
        if frame >= len(animation_list):
            frame = 0

    #display frame image
    screen.blit(animation_list[frame],(150,200))

    pygame.display.update()

pygame.quit()