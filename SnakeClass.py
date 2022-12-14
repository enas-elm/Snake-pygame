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
    
        font = pygame.font.SysFont('freesansbold.ttf', 30)
        text_surface = font.render(str(self.score), False, '#314938')
        self.game.screen.blit(text_surface, (10,10))

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
        

