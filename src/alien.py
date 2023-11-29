import pygame

class Alien(pygame.sprite.Sprite):
    
    def __init__(self, x,y, img):
        super().__init__()
        self.image=pygame.image.load(img)
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def update(self,w,speed):
        self.rect.x+=speed
        if self.rect.left>w:
            self.rect.right=0
    
        
    
        
        
    