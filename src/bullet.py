import pygame


class bullet:
    def __init__(self, x,y,vx,vy):
        self.vx = vx
        self.vy = vy
        self.x = x
        self.y = y
        self.lifeTime = 120

    def bulletUpdate(self):
        self.x += self.vx
        self.y += self.xy
        self.lifeTime -= 1

    def renderSelf(self,screen,scaleF,playerCen):
        image = self.spriteSet.image[8]
        rect = image.get_rect()
        w, h = pygame.display.get_surface().get_size()
        rect.x = (-playerCen.x)*scaleF + (w/2-4) + (self.x*scaleF)
        rect.y = (-playerCen.y)*scaleF + (h/2-4) + (self.y*scaleF)
        screen.blit(pygame.transform.scale(image, (8*scaleF,8*scaleF)), rect)