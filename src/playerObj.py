import pygame
import time
class duck():
    def __init__(self,spriteSet):
      self.x = 0
      self.y = 0
      self.dir = 0
      self.moveSpeed =100
      self.spriteSet =spriteSet
      self.renderIndex = 0


    def playerMove(self,deltaT):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.moveSpeed * deltaT
            self.dir =4
            self.renderIndex = int((time.time()*5)%2+5)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.moveSpeed * deltaT
            self.dir =3
            self.renderIndex = int((time.time()*5)%2+7)
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.moveSpeed * deltaT
            self.dir = 2
            self.renderIndex = int((time.time()*5)%2+3)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.moveSpeed * deltaT
            self.dir = 1
            self.renderIndex = int((time.time()*5)%2+1)
        else:
            self.renderIndex = 0
            self.dir = 1


    def playerRender(self,screen,scale):
        duck = self.spriteSet.image[self.renderIndex]
        gun = None
        if self.dir == 1:
            gun = self.spriteSet.image[10]
        elif self.dir == 2:
            gun = self.spriteSet.image[9]
        elif self.dir ==3:
            gun = self.spriteSet.image[11]
        elif self.dir ==4:
            gun = self.spriteSet.image[12]

        rectduck = duck.get_rect()
        #rect.x = self.x * scale
        #rect.y = self.y * scale

        w, h = pygame.display.get_surface().get_size()
        rectduck.x = w/2-16
        rectduck.y = h/2-16
        screen.blit(pygame.transform.scale(duck, (32*scale,32*scale)), rectduck)
        if gun!=None:
           gun = pygame.transform.scale(gun, (32*scale,32*scale))
           gunrect = gun.get_rect()
           gunrect.x = w/2-16
           gunrect.y = h/2-45
           screen.blit(gun, gunrect)
         
class enemy():
    def __init__(self,spriteSet):
        self.x = 10
        self.y = 10
        self.dir = 0
        self.spriteSet =spriteSet
        self.renderIndex = 0

    def renderSelf(self,screen,scaleF,playerCen):
        image = self.spriteSet.image[int((time.time()*8%3))]
        rect = image.get_rect()
        w, h = pygame.display.get_surface().get_size()
        rect.x = (-playerCen.x)*scaleF + (w/2-16) + (self.x*scaleF)
        rect.y = (-playerCen.y)*scaleF + (h/2-16) + (self.y*scaleF)
        screen.blit(pygame.transform.scale(image, (32*scaleF,32*scaleF)), rect)