import pygame 
import worldRender
#init
screen = pygame.display.set_mode((300, 300), flags=pygame.RESIZABLE) 
pygame.display.set_caption('duck')   

worldObj = worldRender.world(5,5,32,32)

running = True
pos = 0
while running:  

    for event in pygame.event.get():    
        if event.type == pygame.QUIT: 
            running = False

    worldObj.renderSelf(screen)
    pygame.display.update()