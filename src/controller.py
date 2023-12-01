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
        self.clock = pygame.time.Clock()
        self.clock.tick(30)
        
    def mainloop(self):
        self.bg_rect = self.background.get_rect(topleft = (0,0))
        player1=Player(500,650,"assets/image.png")
        player1_group=pygame.sprite.Group()
        player1_group.add(player1)
        laser_group = pygame.sprite.Group()
        laser = Laser(500, 500)
        laser_group.add(laser)
        # alien1=Alien(random.randint(0,1400),200,"assets/spaceship.png")
        num_aliens = 6
        alien_group=pygame.sprite.Group()
        for alien in range(num_aliens):
            alien = Alien(random.randint(0,1400), random.randint(0,300), "assets/spaceship.png")
            alien_group.add(alien)
        
        # level design?
        speed=1
        level=1


            
        
        while True:
            self.display.blit(self.background,(0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        laser.beam()
                        laser.rect.center=player1.rect.center
                        while laser.rect.y>0:
                            y=laser.rect.y-1
                            hit = pygame.sprite.spritecollide(laser,alien_group,True)   
                            if hit: # if an alien has been hit, meaning this list gets updated and is not empty, thus true, break the while loop
                                break                
                            laser_group.update(y)
                            laser_group.draw(self.display)
            pressed=pygame.key.get_pressed()
            if pressed[pygame.K_LEFT] and player1.rect.x>0:
                x=player1.rect.x-8
                player1_group.update(x)
            if pressed[pygame.K_RIGHT] and player1.rect.right<self.width:
                x=player1.rect.x+8
                player1_group.update(x)
            
            if not alien_group:
                level+=1                    
                if level == 2:
                  num_aliens = 8
                if level == 3:
                    speed=1.2
                    num_aliens = 11
                if level == 4:
                    num_aliens = 15
                if level == 5:
                    speed=2
                    num_aliens = 20
                if level == 6:
                    pygame.quit()
                for alien in range(num_aliens):
                    alien = Alien(random.randint(0,1400), random.randint(0,500), "assets/spaceship.png")
                    alien_group.add(alien)

            for a in range(num_aliens):
                alien_group.update(self.width,speed)
                alien_group.draw(self.display)
                
          
            
            player1_group.draw(self.display)
            
            
            pygame.display.flip()      
            
    
         
                    
