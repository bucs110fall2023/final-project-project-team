import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self,x, y, vel):
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill('red')
        self.rect = self.image.get_rect(center = (x,y))
        self.vel = vel

    
    def update(self,x):
        self.rect.x = x
        self.vel +=1
