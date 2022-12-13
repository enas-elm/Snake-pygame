# pip install pygame
import pygame 
import sys
import random
from random import randrange

class Snake: 
    def __init__(self, game):
        self.game = game
        self.size = game.tile_size
        self.rect = pygame.rect.Rect([0, 0, game.tile_size - 2, game.tile_size - 2])
        self.range = self.size // 2, self.game.window_size - self.size // 2, self.size
        self.rect.center = self.get_random_position()
        self.step_delay = 100  # milliseconds
        self.time = 0
        self.length = 1
        self.segments = []
        self.directions = {pygame.K_z: 1, pygame.K_s: 1, pygame.K_q: 1, pygame.K_d: 1}
        




    def get_random_position(self):
        return [randrange(*self.range), randrange(*self.range)]


    def check_food(self):

        if self.game.a == 'b':
            # print('aaaa')
            self.game.apple.rect.center = self.get_random_position()
            self.length += 1



    def update(self):
        self.check_food()


class Apple:
    def __init__(self, game):
        self.game = game
        self.color = (220,20,70)
        self.size = game.tile_size
        self.rect = pygame.rect.Rect([0, 0, game.tile_size - 2, game.tile_size - 2])
        self.rect.center = self.game.snake.get_random_position()

    def draw(self):
        pygame.draw.rect(self.game.screen, 'red', self.rect)
        print(self.rect)

    



class Game:
    def __init__(self):
        #verifie si tout les modules sont charges
        module_charge = pygame.init()
        print(module_charge)

        self.caption = pygame.display.set_caption("Snake")

        self.screen = pygame.display.set_mode((500,500))
        self.screen_color= self.screen.fill('#BFE7CB')
        self.window_size = 500
        self.tile_size = 25
        self.loop = True
        self.a = "a"

        self.snake = Snake(self)
        self.apple = Apple(self)

    def draw_game(self):
        # Draw grid
        for x in range(0, self.window_size, self.tile_size):
            pygame.draw.line(self.screen, '#003C13', (x, 0), (x, self.window_size))
        for y in range(0, self.window_size, self.tile_size):
            pygame.draw.line(self.screen, '#003C13', (0, y), (self.window_size, y))

        # Draw apple
        # Apple(self).draw_apple()


    def game_loop(self):
        while self.loop == True :

            # self.screen_color= self.screen.fill('#BFE7CB')
            # Apple(self).check_collision()

            self.draw_game()
            

            self.check_event()

            self.snake.update()
            pygame.display.flip()

        pygame.quit()
        sys.exit()
        
   

    def check_event(self):
        for event in pygame.event.get():
            # event input clavier 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.a = "b" 
            if event.type == pygame.QUIT:
                self.loop = False




Game().game_loop()
