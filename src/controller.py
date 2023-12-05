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
        """
        This function is basically the bulk of the project. Here we call instances of our
        classes and set values for background and sprite groups. We also have the event loop 
        that handles the 'shootable' laser and the laser collision with aliens. Finally it checks
        for player movement and if all aliens have been cleared out. 
        """
        self.bg_rect = self.background.get_rect(topleft = (0,0))
        player1=Player(500,650,"assets/image.png")
        player1_group=pygame.sprite.Group()
        player1_group.add(player1)
        laser_group = pygame.sprite.Group()
        laser = Laser(500, 500)
        laser_group.add(laser)
        num_aliens = 6
        alien_group=pygame.sprite.Group()
        alien_group=self.add(num_aliens,alien_group)
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
                            if hit: 
                                break                
                            laser_group.update(y)
                            laser_group.draw(self.display)
            pressed=pygame.key.get_pressed()
            self.movement(pressed,player1,player1_group,move)
            if not alien_group:
                level+=1                    
                speed,num_aliens,text=self.levels(level,speed,num_aliens,text)
                alien_group=self.add(num_aliens,alien_group)
            self.draw_aliens(num_aliens,alien_group,self.width,speed,self.display)
                
            player1_group.draw(self.display)
            self.display.blit(text, (900, 800))
            pygame.display.flip()      
            
    def rand(self,one,two):
        """
        This function decides the random values for the spawning of the enemies
        
        Args:
            one (int): an integer that represents a random x value
            two (int): an integer that represents a random y value
        
        Returns:
            ran_x(int): a random value between 0 to the 'one' variable
            ran_y(int): a random value between o to the 'two' variable
        
        """
        ran_x=random.randint(0,one)
        ran_y=random.randint(0,two)
        return ran_x,ran_y
    
    def add(self,num_aliens,alien_group):
        """_summary_

        Args:
            num_aliens (int): amount of aliens in the sprite group
            alien_group (sprite Group): The sprite group containing the amount of aliens

        Returns:
            alien_group (sprite Group): The sprite gorup containing the amount of aliensß
        """
        for alien in range(num_aliens):
            ran_x,ran_y = self.rand(1400,500)
            alien = Alien(ran_x, ran_y, "assets/spaceship.png")
            alien_group.add(alien)
        return alien_group
    
    def draw_aliens(self,num_aliens,alien_group,width,speed,display):
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
        
    def levels(self, level,speed,num_aliens,text):
        if level == 2:
            num_aliens = 8
            text = self.font.render(f"Level: {level}", True, "white")
        elif level == 3:
            speed=1.2
            text = self.font.render(f"Level: {level}", True, "white")
            num_aliens = 11
        elif level == 4:
            num_aliens = 15
            text = self.font.render(f"Level: {level}", True, "white")
        elif level == 5:
            speed=1.5
            num_aliens = 20
            text = self.font.render(f"Level: {level}", True, "white")
        elif level == 6:
            text = self.font.render(f"Level: {level}", True, "white")
            pygame.quit()
        return speed,num_aliens,text
                
