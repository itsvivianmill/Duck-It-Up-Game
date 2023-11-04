import pygame 
import worldRender
import tileset
import playerObj
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
    r"src\asset\mapTiles\watertipright.png",     #15
    r"src\asset\mapTiles\littlewaterbottomleftTip.png", #16
    r"src\asset\mapTiles\littlewaterbottomrightTip.png",#17
    r"src\asset\mapTiles\littlewaterbottomrightTip.png", #17
]

duckAssetList = [
    r"src\asset\duck\standfront.png", #0
    r"src\asset\duck\right1.png",
    r"src\asset\duck\right2.png",
    r"src\asset\duck\left1.png",
    r"src\asset\duck\left2.png",
    r"src\asset\duck\backwalk1.png",
    r"src\asset\duck\backwalk2.png",
    r"src\asset\duck\frontwalk1.png",
    r"src\asset\duck\frontwalk2.png"
]

tilemap = tileset.tileset(tileMapAssetList)
duckTileMap = tileset.tileset(duckAssetList)
duck = playerObj.playerObj(duckTileMap)
worldObj = worldRender.world(25,25,32,32,tilemap)
worldObj.loadTileMap("src\map.txt")
running = True
pos = 0
while running:  

    for event in pygame.event.get():    
        if event.type == pygame.QUIT: 
            running = False
    w, h = pygame.display.get_surface().get_size()
    duck.playerMove()
    worldObj.renderSelf(screen,w/300,duck)
    duck.playerRender(screen,w/300)
    pygame.display.update()