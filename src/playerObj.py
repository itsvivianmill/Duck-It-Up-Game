import pygame
import time
class playerObj():
    def __init__(self,spriteSet):
      self.x = 0
      self.y = 0
      self.rotation = 0
      self.moveSpeed =0.5
      self.spriteSet =spriteSet
      self.renderIndex = 0


    def playerMove(self):
        keys=pygame.key.get_pressed()
        print(self.x,self.y)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.moveSpeed
            self.renderIndex = int((time.time()*5)%2+5)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.moveSpeed
            self.renderIndex = int((time.time()*5)%2+7)
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.moveSpeed
            self.renderIndex = int((time.time()*5)%2+3)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.moveSpeed
            self.renderIndex = int((time.time()*5)%2+1)
        else:
            self.renderIndex = 0


    def playerRender(self,screen,scale):
        image = self.spriteSet.image[self.renderIndex]
        rect = image.get_rect()
        #rect.x = self.x * scale
        #rect.y = self.y * scale

        w, h = pygame.display.get_surface().get_size()
        rect.x = w/2-16
        rect.y = h/2-16
        screen.blit(pygame.transform.scale(image, (32*scale,32*scale)), rect)




    