import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion():
    """Class for manage resources from game."""
    
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self.screen)
    
    def run_game(self):
        """Running a main cycle"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    
    def _check_events(self):
        # Tracking an event from keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move to right
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                    
    
    def _update_screen(self):
        # Screen filled in custom color which is defined in __init__
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
            
        # Display the last animation screen
        pygame.display.flip()        

if __name__ == '__main__':
    # Creating an object and running the game
    ai = AlienInvasion()
    ai.run_game()
    