# pip install pygame
import pygame 
import sys
import random


class Snake:
    def __init__(self, game):
        self.game = game
        self.color = '#2B5A39'
        self.size = 50
        self.surface = pygame.Surface((self.size,self.size))

        self.x_snake = 200
        self.y_snake = 200

        self.right = False
        self.left = False
        self.up = False
        self.down = False

        self.score = 0


    def move_snake(self):
        if self.right == True:
            pygame.time.delay(150)
            self.x_snake = self.x_snake + self.size
        if self.left == True:
            pygame.time.delay(150)
            self.x_snake = self.x_snake - self.size
        if self.up == True:
            pygame.time.delay(150)
            self.y_snake = self.y_snake - self.size
        if self.down == True:
            pygame.time.delay(150)
            self.y_snake = self.y_snake + self.size

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.right = True
                    self.left = self.up = self.down = False
                elif event.key == pygame.K_q:
                    self.left = True
                    self.right = self.up = self.down = False
                elif event.key == pygame.K_z:
                    self.up = True
                    self.right = self.left = self.down = False
                elif event.key == pygame.K_s:
                    self.down = True
                    self.up = self.left = self.right = False


    def draw_snake(self, screen):
        self.move_snake()
        self.rect = pygame.rect.Rect((self.x_snake, self.y_snake, self.size, self.size))
        pygame.draw.rect(screen, self.color, self.rect)

    def check_out_screen(self, screen):
        if self.x_snake < 0 or self.x_snake > 500 or self.y_snake < 0 or self.y_snake > 500:
            print('dead')

    def check_eat_apple(self, apple):
        if self.x_snake == self.game.apple.x_food and self.y_snake == self.game.apple.y_food:
            self.game.apple.rand_position_apple()
            self.score = self.score + 1
            print(self.score)

    def snake_check(self, screen):
        self.check_out_screen(screen)
        self.check_eat_apple(self.game.apple)
        



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
    


class Game:
    def __init__(self):
        #verifie si tout les modules sont charges
        module_charge = pygame.init()
        print(module_charge)

        self.caption = pygame.display.set_caption("Snake")

        self.screen = pygame.display.set_mode((500,500))
        # self.screen_color= self.screen.fill('#BFE7CB')
        self.window_size = 500
        self.tile_size = 50
        self.loop = True

        self.apple = Apple(self)
        self.snake = Snake(self)

    def draw_game(self):
        # Draw grid
        for x in range(0, self.window_size, self.tile_size):
            pygame.draw.line(self.screen, '#B2DDBF', (x, 0), (x, self.window_size), 5)
        for y in range(0, self.window_size, self.tile_size):
            pygame.draw.line(self.screen, '#B2DDBF', (0, y), (self.window_size, y), 5)


    def game_loop(self): 
        while self.loop == True :
            self.screen_color= self.screen.fill('#BFE7CB')
            self.draw()
            
            self.event_check()
            pygame.display.flip()

        pygame.quit()
        sys.exit()
        
    def draw(self):
        self.draw_game()
        
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
