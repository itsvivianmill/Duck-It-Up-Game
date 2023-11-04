import pygame 
import worldRender
import tileset
#init
screen = pygame.display.set_mode((300, 300), flags=pygame.RESIZABLE) 
pygame.display.set_caption('duck')   

tileMapAssetList = [
    r"src\asset\mapTiles\grass.png",
    r"src\asset\mapTiles\grassFlower.png",
    r"src\asset\mapTiles\grassFlower2.png",
    r"src\asset\mapTiles\grassTree.png",
    r"src\asset\mapTiles\rock.png",
    r"src\asset\mapTiles\water.png",
    r"src\asset\mapTiles\boderbottom.png",
    r"src\asset\mapTiles\borderleft.png",
    r"src\asset\mapTiles\borderright.png",
    r"src\asset\mapTiles\bordertop.png",
    r"src\asset\mapTiles\cornertopright.png",
    r"src\asset\mapTiles\cornertopleft.png",
    r"src\asset\mapTiles\cornerbottomright.png",
    r"src\asset\mapTiles\cornerbottomleft.png"
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