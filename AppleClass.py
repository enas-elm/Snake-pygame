import pygame 
import random

class Apple:
    def __init__(self, game):
        self.game = game
        self.color = "#DC1446"
        self.size = self.game.tile_size
        self.surface = pygame.Surface((self.size,self.size))
        self.x_food = random.randrange(0, 500, self.size)
        self.y_food = random.randrange(0, 500, self.size)


    def rand_position_apple(self):
        self.x_food = random.randrange(0, 500, self.size)
        self.y_food = random.randrange(0, 500,self.size)

                    
    def draw_apple(self):
        # self.check_collision()
        self.rect = pygame.rect.Rect((self.x_food, self.y_food, self.size, self.size))
        pygame.draw.rect(self.game.screen, self.color, self.rect)
    
