# Python Crash Course (Third Edition) - Part II: Project 1
# Alien Invasion Game 

import os       # os module provides a way of using operating system dependent functionality
import sys      # sys module allows us to exit the game when the player quits
import pygame   # pygame module contains the functionality needed to make a game
from settings import Settings 
from ship import Ship


# Set the working directory to the directory of the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock() # Create a clock object to control the speed of the game
        self.settings = Settings()

        # Set the display window size and caption
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Create an instance of the Ship class
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()  # Draw the ship on the screen
            
            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60) # Set the frame rate to 60 frames per second

if __name__ == '__main__': # This line checks whether the file is being run directly
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()