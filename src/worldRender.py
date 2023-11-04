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
                self.tileIndexMap[y*self.rx+x] = random.randint(0,1)                                

    def renderSelf(self,screen):
        for y in range(self.ry):
            for x in range(self.rx):
                image = self.tileset.image[self.tileIndexMap[y*self.rx+x]]
                rect = image.get_rect()
                w, h = pygame.display.get_surface().get_size()
                scaleF = w/300
                rect.x = math.floor(x*self.spriteRX*scaleF)
                rect.y = math.floor(y*self.spriteRY*scaleF    )
                screen.blit(pygame.transform.scale(image, (math.ceil(self.spriteRX*scaleF),math.ceil(self.spriteRY*scaleF))), rect)

