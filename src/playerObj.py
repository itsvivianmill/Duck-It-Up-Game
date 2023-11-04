import pygame
class playerObj():
    def __init__(self,spriteSet):
      self.x = 0
      self.y = 0
      self.rotation = 0
      self.moveSpeed =0.1
      self.spriteSet


    def playerMove(self):
        keys=pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.moveSpeed
            print('up')
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.moveSpeed
            print('down')
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.moveSpeed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.moveSpeed



    