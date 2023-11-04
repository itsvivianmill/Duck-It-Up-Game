import pygame


class world:
    def __init__(self, rx,ry,spriteX,spriteY):
        self.rx = rx
        self.ry = ry
        self.spriteRX = spriteX
        self.spriteRY = spriteY
        self.tileIndexMap = [rx*ry]
        for y in range(ry):
            for x in range(rx):
                self.tileIndexMap[y*self.rx+x] = 1                                

    def renderSelf(self):
        pass

