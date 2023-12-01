import pygame
import math

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
            
    # def draw_aliens(self,num,speed,width,display,alien_group):
    #     num_aliens=num 
    #     for a in range(num_aliens):
    #         alien_group.update(width,speed)
    #         alien_group.draw(display)
            
    # def alien_levels(self,alien_group,level,speed,num_aliens,ran_x,ran_y,alien):
    #     if not alien_group:
    #             level+=1                    
    #             if level == 2:
    #              num_aliens = 8
    #             if level == 3:
    #                 speed=1.2
    #                 num_aliens = 11
    #             if level == 4:
    #                 num_aliens = 15
    #             if level == 5:
    #                 speed=2
    #                 num_aliens = 20
    #             alien_group=self.adding_aliens(alien,num_aliens,alien_group,ran_x,ran_y)
    #             # for alien in range(num_aliens):
    #             #     alien = Alien(random.randint(0,1400), random.randint(0,500), "assets/spaceship.png")
    #             #     alien_group.add(alien)
    #     return level
    # def adding_aliens(self,alien,num_aliens,alien_group,ran_x,ran_y):
    #   for alien in range(num_aliens):
    #                 alien = Alien(ran_x, ran_y, "assets/spaceship.png")
    #                 alien_group.add(alien)
    #   return alien_group

    
        
    
        
        
    