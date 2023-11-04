import pygame 
import worldRender
import tileset
#init
screen = pygame.display.set_mode((300, 300), flags=pygame.RESIZABLE) 
pygame.display.set_caption('duck')   

tileMapAssetList = [
    r"src\asset\mapTiles\grass.png",            #0
    r"src\asset\mapTiles\grassFlower.png",      #1
    r"src\asset\mapTiles\grassFlower2.png",     #2
    r"src\asset\mapTiles\grassTree.png",        #3
    r"src\asset\mapTiles\rock.png",             #4
    r"src\asset\mapTiles\water.png",            #5
    r"src\asset\mapTiles\boderbottom.png",      #6
    r"src\asset\mapTiles\borderleft.png",       #7
    r"src\asset\mapTiles\borderright.png",      #8
    r"src\asset\mapTiles\bordertop.png",        #9
    r"src\asset\mapTiles\cornertopright.png",   #10
    r"src\asset\mapTiles\cornertopleft.png",    #11
    r"src\asset\mapTiles\cornerbottomright.png",#12
    r"src\asset\mapTiles\cornerbottomleft.png", #13
    r"src\asset\mapTiles\watertipleft.png",     #14
    r"src\asset\mapTiles\watertipright.png"     #15
]

tilemap = tileset.tileset(tileMapAssetList)
worldObj = worldRender.world(25,25,32,32,tilemap)
worldObj.loadTileMap("src\map.txt")
running = True
pos = 0
while running:  

    for event in pygame.event.get():    
        if event.type == pygame.QUIT: 
            running = False

    worldObj.renderSelf(screen)
    pygame.display.update()