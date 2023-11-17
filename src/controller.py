from src.alien import Alien
import pygame
import random
from src.player import Player
from src.laser import Laser

class Controller:
    def __init__(self):
        pygame.init()
        self.display=pygame.display.set_mode()
        self.width,self.height=pygame.display.get_window_size()
        self.background=pygame.image.load("assets/Space001.png")

        
    def mainloop(self):
        self.bg_rect = self.background.get_rect(topleft = (0,0))
        player1=Player(500,500,"assets/image.png")
        player1_group=pygame.sprite.Group()
        player1_group.add(player1)
        laser_group = pygame.sprite.Group()
        laser = Laser(500, 500)
        laser_group.add(laser)
        alien1=Alien(random.randint(0,1000),200,"assets/spaceship.png")
        alien_group=pygame.sprite.Group()
        alien_group.add(alien1)
        
        while True:
            self.display.blit(self.background,(0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        laser.rect.center=player1.rect.center
                        while laser.rect.y>0:
                            if laser.rect.colliderect(alien1.rect):
                                alien_group.remove(alien1)
                            y=laser.rect.y-8
                            laser_group.update(y)
                            laser_group.draw(self.display)
            pressed=pygame.key.get_pressed()
            if pressed[pygame.K_LEFT] and player1.rect.x>0:
                x=player1.rect.x-8
                player1_group.update(x)
            if pressed[pygame.K_RIGHT] and player1.rect.right<self.width:
                x=player1.rect.x+8
                player1_group.update(x)
           

            
            player1_group.draw(self.display)
            for i in range (0,6):

                alien_group.draw(self.display)
            pygame.display.flip()        