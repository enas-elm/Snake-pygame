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
        self.window_size = 500
        self.tile_size = 50
        self.loop = True

        self.apple = Apple(self)
        self.snake = Snake(self)
        self.board = Board(self)

        self.alive = True


    def game_loop(self): 
        while self.loop == True :
            self.screen_color= self.screen.fill('#FFFFFF')
            self.draw()
            
            self.event_check()
            pygame.display.flip()

        pygame.quit()
        sys.exit()
        
    def draw(self):
        self.board.draw_game()
        
        if self.alive == True :
            self.apple.draw_apple()
            self.snake.draw_snake()
        else :
            font = pygame.font.Font('freesansbold.ttf', 50)
            text = font.render('GAME OVER', True, '#000000')
            textRect = text.get_rect()
            textRect.center = (self.window_size // 2, self.window_size // 2)
            self.screen.blit(text, textRect)

        font = pygame.font.SysFont('freesansbold.ttf', 30)
        text_surface = font.render(str(self.snake.score), False, '#000000')
        self.screen.blit(text_surface, (10,10))


    def event_check(self):
        for event in pygame.event.get():
            # event input clavier 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.loop = False 
            if event.type == pygame.QUIT:
                self.loop = False

        self.snake.snake_check()
        




Game().game_loop()
