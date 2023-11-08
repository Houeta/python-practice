import pygame

class Ship():
    """Ship control class"""
    
    def __init__(self, ai_game):
         """init ship and sets start position"""
         self.screen = ai_game
         self.screen_rect = ai_game.get_rect()
         self.moving_right = False
         
         # Download the ship image and get rectangle
         self.image = pygame.image.load('images/ship.bmp')
         self.rect = self.image.get_rect()
         # Even new ship was spawned on midbottom
         self.rect.midbottom = self.screen_rect.midbottom
         
    def update(self):
        """Renew ship position via flag"""
        if self.moving_right:
            self.rect.x += 1
         
    def blitme(self):
        """Ship painted in start position"""
        self.screen.blit(self.image, self.rect)
         