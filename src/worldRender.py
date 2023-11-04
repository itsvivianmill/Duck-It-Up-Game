import pygame
import math

class world:
    def __init__(self, rx, ry,spriteX,spriteY):
        self.rx = rx
        self.ry = ry
        self.spriteRX = spriteX
        self.spriteRY = spriteY
        self.tileIndexMap = [1] * (rx*ry)
        for y in range(ry):
            for x in range(rx):
                self.tileIndexMap[y*self.rx+x] = 1                                

    def renderSelf(self,screen):
        file = '.\\src\\grass.png'
        image = pygame.image.load(file)
        rect = image.get_rect()
        for y in range(self.ry):
            for x in range(self.rx):
                w, h = pygame.display.get_surface().get_size()
                scaleF = w/300
                rect.x = math.floor(x*self.spriteRX*scaleF)
                rect.y = math.floor(y*self.spriteRY*scaleF    )
                screen.blit(pygame.transform.scale(image, (math.ceil(self.spriteRX*scaleF),math.ceil(self.spriteRY*scaleF))), rect)

