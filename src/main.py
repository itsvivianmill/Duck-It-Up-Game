import pygame 
import worldRender
import tileset
import playerObj
import random
import bullet
import time
import math
#init
screen = pygame.display.set_mode((600, 600)) 
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
    r"src\asset\mapTiles\bottomTreeBorder.png",         #18
    r"src\asset\mapTiles\leftTreeBorder.png",           #19
    r"src\asset\mapTiles\rightTreeBorder.png",          #20
    r"src\asset\mapTiles\treecorner.png",              #21
    r"src\asset\mapTiles\middleTree.png",              #22
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
    r"src\asset\duck\frontwalk2.png",
    r"src\asset\duck\gunleft.png",
    r"src\asset\duck\gunright.png",
    r"src\asset\duck\gunback.png",
    r"src\asset\duck\gunforward.png"
]

enemyAsset = [
    r"src\asset\enemy\idle1.png",
    r"src\asset\enemy\idle2.png",
    r"src\asset\enemy\idle3.png"
]

tilemap = tileset.tileset(tileMapAssetList)
duckTileMap = tileset.tileset(duckAssetList)
enemyTileMap = tileset.tileset(enemyAsset)
bulletTile = tileset.tileset([r"src\asset\duck\bullet.png"])

duck = playerObj.duck(duckTileMap)
bulletPool =[]
enemyPool = []
worldObj = worldRender.world(25,25,32,32,tilemap)
worldObj.loadTileMap("src\map.txt")
running = True

for i in range(10):
    enemyPool.append(playerObj.enemy(enemyTileMap))
    enemyPool[len(enemyPool)-1].x = random.randint(20,800)
    enemyPool[len(enemyPool)-1].y = random.randint(20,800)
deltaT = 0.1
start = 0
while running:  
    start = time.time()
    for event in pygame.event.get():    
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            w, h = pygame.display.get_surface().get_size()
            mpos = pygame.mouse.get_pos()
            dirX = (w/2-16) - mpos[0]
            dirY = (h/2-16-10) - mpos[1]
            print(mpos,duck.x,duck.y)
            length = math.sqrt(dirX**2+dirY**2)
            dirX/=-length
            dirY/=-length
            bulletPool.append(bullet.bullet(duck.x,duck.y-10,dirX,dirY,bulletTile))
    w, h = pygame.display.get_surface().get_size()
    duck.playerMove(deltaT)
    background = pygame.image.load(r"src\asset\mapTiles\tree middle.png")
    screen.blit(background, background.get_rect())
    worldObj.renderSelf(screen,w/300,duck)
    for i in enemyPool:
        i.renderSelf(screen,w/300,duck)

    for i in bulletPool:
        i.bulletUpdate(deltaT)
        i.bulletCheckCollide(enemyPool,duck,w/300)
        i.renderSelf(screen,w/300,duck)
        if i.lifeTime <= 0:
            bulletPool.remove(i)

        

    duck.playerRender(screen,w/300)
    pygame.display.update()

    deltaT = time.time() - start
    start = time.time()