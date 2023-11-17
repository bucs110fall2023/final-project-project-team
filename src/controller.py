# from src.alien import Alien
import pygame
from src.player import Player
from src.laser import Laser

class Controller:
    def __init__(self):
        pygame.init()
        self.display=pygame.display.set_mode()
        self.width,self.height=pygame.display.get_window_size()
        
    def mainloop(self):
        background=pygame.image.load("assets/Space001.png")
        self.bg_rect = background.get_rect(topleft = (0,0))
        player1=Player(500,500,"assets/image.png")
        player1_group=pygame.sprite.Group()
        player1_group.add(player1)
        laser_group = pygame.sprite.Group()
        laser = Laser(500, 500)
        laser_group.add(laser)
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                if event.type==pygame.K_SPACE:
                    pass
            pressed=pygame.key.get_pressed()
            if pressed[pygame.K_LEFT] and player1.rect.x>0:
                x=player1.rect.x-8
                player1_group.update(x)
            if pressed[pygame.K_RIGHT] and player1.rect.right<self.width:
                x=player1.rect.x+8
                player1_group.update(x)
           

            
            self.display.blit(background,(0,0))
            player1_group.draw(self.display)
            pygame.display.flip()        