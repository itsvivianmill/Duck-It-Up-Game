import pygame


class bullet:
    def __init__(self, x,y,vx,vy,spriteSet):
        self.vx = vx
        self.vy = vy
        self.x = x
        self.y = y
        self.lifeTime = 120
        self.spriteSet = spriteSet

    def bulletUpdate(self,deltaT):
        self.x += self.vx * deltaT * 200
        self.y += self.vy * deltaT * 200
        self.lifeTime -= 1

    def bulletCheckCollide(self,enList,playerCen,scaleF):
        w, h = pygame.display.get_surface().get_size()
        renderedX = (-playerCen.x)*scaleF + (w/2-4) + (self.x*scaleF)
        renderedY = (-playerCen.y)*scaleF + (h/2-4) + (self.y*scaleF)
        bulletRect = pygame.Rect(renderedX, renderedY, 8*scaleF, 8*scaleF)
        for i in enList:
            enRenX = (-playerCen.x)*scaleF + (w/2-16) + (i.x*scaleF)
            enRenY = (-playerCen.y)*scaleF + (h/2-16) + (i.y*scaleF)
            collidedY = (bulletRect.y+8 > enRenY and bulletRect.y < enRenY + 32)
            collidedX = (bulletRect.x+8 > enRenX and bulletRect.x < enRenX + 32)
            if (collidedX and collidedY):
                enList.remove(i)

    def renderSelf(self,screen,scaleF,playerCen):
        image = self.spriteSet.image[0]
        rect = image.get_rect()
        w, h = pygame.display.get_surface().get_size()
        rect.x = (-playerCen.x)*scaleF + (w/2-4) + (self.x*scaleF)
        rect.y = (-playerCen.y)*scaleF + (h/2-4) + (self.y*scaleF)
        screen.blit(pygame.transform.scale(image, (8*scaleF,8*scaleF)), rect)