# pip install pygame
import pygame 
import sys
import random

class Board:
    def __init__(self, game):
        self.game = game
        self.tile_size = self.game.tile_size

    def draw_game(self):
        # Draw grid
        for x in range(0, self.game.window_size, self.tile_size):
            pygame.draw.line(self.game.screen, '#B3B3B3', (x, 0), (x, self.game.window_size), 1)
        for y in range(0, self.game.window_size, self.tile_size):
            pygame.draw.line(self.game.screen, '#B3B3B3', (0, y), (self.game.window_size, y), 1)

        pygame.draw.line(self.game.screen, '#444444', (0, 0), (self.game.window_size, 0), 5)
        pygame.draw.line(self.game.screen, '#444444', (self.game.window_size, self.game.window_size), (self.game.window_size, 0), 5)
        pygame.draw.line(self.game.screen, '#444444', (0, 500), (self.game.window_size, self.game.window_size), 5)
        pygame.draw.line(self.game.screen, '#444444', (0, 0), (0, self.game.window_size), 5)


        





