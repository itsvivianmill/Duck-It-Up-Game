import pygame 
import worldRender
import tileset
#init
screen = pygame.display.set_mode((300, 300), flags=pygame.RESIZABLE) 
pygame.display.set_caption('duck')   

tilemap = tileset.tileset((r"src\asset\mapTiles\grass.png",r"src\asset\mapTiles\water.png"))
worldObj = worldRender.world(5,5,32,32,tilemap)

running = True
pos = 0
while running:  

    for event in pygame.event.get():    
        if event.type == pygame.QUIT: 
            running = False

    worldObj.renderSelf(screen)
    pygame.display.update()