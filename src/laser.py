import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self,x, y):
        """
        Creates the laser onject, including the image and rectangle surrounding the image.
        
        Args: 
        x(int): x pos of the laser
        y(int): y pos of the laser
        
        """
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill('red')
        self.rect = self.image.get_rect(center = (x,y))
        self.sound=pygame.mixer.Sound("assets/shoot.wav")

    def beam(self):
        """
        This function is responsible for containing the laser sound from the player.
        """
        self.sound.play()
    
    def update(self,y):
        """
        This function contains the movement update for the laser.
        
        """
        self.rect.y = y