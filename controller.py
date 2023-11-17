from alien import Alien
from src.player import Player
import pygame

class Controller:
    def __init__(self):
        pygame.init()
        self.display=pygame.display.set_mode()
        self.width,self.height=pygame.display.get_window_size()
        # self.space=pygame.surface((self.width,self.height))
    def mainloop(self):
        background=pygame.image.load("assets/Space001.png")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
        
            self.display.blit(background,(0,0))
            
            pygame.display.flip()        