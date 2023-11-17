# from src.alien import Alien
import pygame
import player

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
            pressed=pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                x=player1.rect.x-5
                player1_group.update(x)
            if pressed[pygame.K_RIGHT]:
                x=player1.rect.x+5
                player1_group.update(x)
            if pressed[pygame.K_SPACE]:
                pass

        
            self.display.blit(background,(0,0))
            player1_group.draw(self.display)
            pygame.display.flip()        