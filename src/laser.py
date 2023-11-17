import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self,x, y, vel):
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill('red')
        self.rect = self.image.get_rect(center = (x,y))


    
    def update(self,y):
        self.rect.y = y