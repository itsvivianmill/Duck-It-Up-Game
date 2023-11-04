import pygame
import math
import random
class world:
    def __init__(self, rx, ry,spriteX,spriteY, tileset):
        self.rx = rx
        self.ry = ry
        self.spriteRX = spriteX
        self.spriteRY = spriteY
        self.tileset = tileset
        self.tileIndexMap = [1] * (rx*ry)
        for y in range(ry):
            for x in range(rx):
                self.tileIndexMap[y*self.rx+x] = 0                                

    def renderSelf(self,screen,scaleF,playerCen):
        for y in range(self.ry):
            for x in range(self.rx):
                image = self.tileset.image[self.tileIndexMap[y*self.rx+x]]
                rect = image.get_rect()
                w, h = pygame.display.get_surface().get_size()
                if playerCen==None:
                    rect.x = math.floor(x*self.spriteRX*scaleF)
                    rect.y = math.floor(y*self.spriteRY*scaleF)
                else:
                    rect.x = playerCen.x*scaleF + w/2 + math.floor(x*self.spriteRX*scaleF)
                    rect.y = playerCen.y*scaleF + h/2 + math.floor(y*self.spriteRY*scaleF)
                screen.blit(pygame.transform.scale(image, (math.ceil(self.spriteRX*scaleF),math.ceil(self.spriteRY*scaleF))), rect)

    def loadTileMap(self,path):
        file = open(path, "r")
        data = file.read().split("\n")
        header = data[0].split(" ")
        if int(header[0])==self.rx and int(header[1])==self.ry:
            data.pop(0)
            print(data)
            for y in range(len(data)):
                for x in range(len(data[y].split(" "))):
                    currentIndex = data[y].split(" ")[x]
                    self.tileIndexMap[y*self.rx+x] = int(currentIndex)