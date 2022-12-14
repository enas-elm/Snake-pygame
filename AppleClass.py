import pygame 
import sys
import random

class Apple:
    def __init__(self, game):
        self.game = game
        self.color = (220,20,70)
        self.size = 50
        self.surface = pygame.Surface((self.size,self.size))
        self.x_food = random.randrange(0, 500, self.size)
        self.y_food = random.randrange(0, 500, self.size)


    def rand_position_apple(self):
        self.x_food = random.randrange(0, 500, self.size)
        self.y_food = random.randrange(0, 500,self.size)

                    
    def draw_apple(self, screen):
        # self.check_collision()
        self.rect = pygame.rect.Rect((self.x_food, self.y_food, self.size, self.size))
        pygame.draw.rect(screen, self.color, self.rect)
    
