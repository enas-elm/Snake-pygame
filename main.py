# pip install pygame
import pygame 
import sys
import random

from SnakeClass import Snake
from AppleClass import Apple
from BoardClass import Board


class Game:
    def __init__(self):
        #verifie si tout les modules sont charges
        module_charge = pygame.init()
        print(module_charge)
        pygame.font.init()

        self.caption = pygame.display.set_caption("Snake")

        self.screen = pygame.display.set_mode((500,500))
        # self.screen_color= self.screen.fill('#BFE7CB')
        self.window_size = 500
        self.tile_size = 50
        self.loop = True

        self.apple = Apple(self)
        self.snake = Snake(self)
        self.board = Board(self)



    def game_loop(self): 
        while self.loop == True :
            self.screen_color= self.screen.fill('#BFE7CB')
            self.draw()
            
            self.event_check()
            pygame.display.flip()

        pygame.quit()
        sys.exit()
        
    def draw(self):
        self.board.draw_game()
        
        self.snake.draw_snake(self.screen)
        self.apple.draw_apple(self.screen)
        

    def event_check(self):
        for event in pygame.event.get():
            # event input clavier 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.loop = False 
            if event.type == pygame.QUIT:
                self.loop = False

        self.snake.snake_check(self.screen)
        




Game().game_loop()
