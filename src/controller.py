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
        self.text_color = (255,255,255)
        self.font = pygame.font.Font(None, 48)
                
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
        alien_group=self.add(num_aliens,alien_group)
        # level design?
        speed=1
        level=1
        move=8
        text = self.font.render(f"Level: {level}", True, "white")
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
            # if pressed[pygame.K_LEFT] and player1.rect.x>0:
            #     x=player1.rect.x-move
            #     player1_group.update(x)
            # if pressed[pygame.K_RIGHT] and player1.rect.right<self.width:
            #     x=player1.rect.x+move
            #     player1_group.update(x)
            self.movement(pressed,player1,player1_group,move)
            # alien_group=self.levels(alien_group,level,num_aliens,speed,ran_x,ran_y)
            if not alien_group:
                level+=1                    
                if level == 2:
                  num_aliens = 8
                  text = self.font.render(f"Level: {level}", True, "white")
                if level == 3:
                    speed=1.2
                    text = self.font.render(f"Level: {level}", True, "white")
                    num_aliens = 11
                if level == 4:
                    num_aliens = 15
                    text = self.font.render(f"Level: {level}", True, "white")
                if level == 5:
                    speed=1.5
                    num_aliens = 20
                    text = self.font.render(f"Level: {level}", True, "white")
                if level == 6:
                    text = self.font.render(f"Level: {level}", True, "white")
                    pygame.quit()
                alien_group=self.add(num_aliens,alien_group)
            self.draw(num_aliens,alien_group,self.width,speed,self.display)
            # for a in range(num_aliens):
            #     alien_group.update(self.width,speed)
            #     alien_group.draw(self.display)
                
            player1_group.draw(self.display)
            self.display.blit(text, (900, 800))
            pygame.display.flip()      
            
    def rand(self,one,two):
        ran_x=random.randint(0,one)
        ran_y=random.randint(0,two)
        return ran_x,ran_y
    
    def add(self,num_aliens,alien_group):
        for alien in range(num_aliens):
            ran_x,ran_y = self.rand(1400,500)
            alien = Alien(ran_x, ran_y, "assets/spaceship.png")
            alien_group.add(alien)
        return alien_group
    
    def draw(self,num_aliens,alien_group,width,speed,display):
        for a in range(num_aliens):
                alien_group.update(width,speed)
                alien_group.draw(display)
    
    def movement(self, pressed,player1,player1_group,move):
         if pressed[pygame.K_LEFT] and player1.rect.x>0:
                x=player1.rect.x-move
                player1_group.update(x)
         if pressed[pygame.K_RIGHT] and player1.rect.right<self.width:
                x=player1.rect.x+move
                player1_group.update(x)
        
        
         
                    
