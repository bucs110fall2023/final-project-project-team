from src.alien import Alien
from src.player import Player
import pygame

class Controller:
    def __init__(self):
        pygame.init()
        self.display=pygame.display.set_mode()
        self.width,self.height=pygame.display.get_window_size()
    def mainloop(self):
        background=pygame.image.load("assets/Space001.png")
        player1=Player(500,500,"assets/image.png")
        player1_group=pygame.sprite.Group()
        player1_group.add(player1)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
        
            self.display.blit(background,(0,0))
            player1_group.draw(self.display)
            pygame.display.flip()        