import pygame
class tileset:
    def __init__(self, tileList):
        self.image=[]
        for i in tileList:
            self.image.append(pygame.image.load(i))