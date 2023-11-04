import pygame 
import worldRender
#init
screen = pygame.display.set_mode((300, 300), flags=pygame.RESIZABLE) 
pygame.display.set_caption('duck')   

file = '.\\src\\testsprite.png'
image = pygame.image.load(file)
rect = image.get_rect()
worldObj = worldRender.world(20,20,32,32)

running = True
pos = 0
while running:  

    for event in pygame.event.get():    
        if event.type == pygame.QUIT: 
            running = False

    worldObj.renderSelf()
    pygame.display.update()