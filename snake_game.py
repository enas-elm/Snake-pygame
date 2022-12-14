# pip install pygame
import pygame 
import sys
import random


class Snake:
    def __init__(self):
        self.color = '#2B5A39'
        self.size = 50
        self.surface = pygame.Surface((self.size,self.size))

        self.x_snake = 250
        self.y_snake = 250

        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def move_snake(self):

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.right = True
                    self.left = False
                    self.up = False
                    self.down = False
                if event.key == pygame.K_q:
                    self.right = False
                    self.left = True
                    self.up = False
                    self.down = False
                if event.key == pygame.K_z:
                    self.right = False
                    self.left = False
                    self.up = True
                    self.down = False
                if event.key == pygame.K_s:
                    self.right = False
                    self.left = False
                    self.up = False
                    self.down = True
        

        if self.right == True:
            pygame.time.delay(300)
            self.x_snake = self.x_snake + self.size
        if self.left == True:
            pygame.time.delay(300)
            self.x_snake = self.x_snake - self.size
        if self.up == True:
            pygame.time.delay(300)
            self.y_snake = self.y_snake + self.size
        if self.down == True:
            pygame.time.delay(300)
            self.y_snake = self.y_snake + self.size
        
        print(str(self.x_snake) + ',' + str(self.y_snake))

    # def time(self):
    #     pygame.time.set_timer(self.move_snake,300)
                   


    def draw_snake(self, screen):
        self.move_snake()
        self.rect = pygame.rect.Rect((self.x_snake, self.y_snake, self.size, self.size))
        pygame.draw.rect(screen, self.color, self.rect)
        



class Apple:
    def __init__(self):
        self.color = (220,20,70)
        self.size = 50
        self.surface = pygame.Surface((self.size,self.size))
        self.radius = self.size // 2
        self.x_food = 250
        self.y_food = 250

    def check_collision(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    print("apple")
                    self.x_food =random.randrange(0, 500,50)
                    self.y_food =random.randrange(0, 500,50)

    def draw_apple(self, screen):
        self.check_collision()
        pygame.draw.circle(screen, self.color, ( self.x_food, self.y_food), self.radius)

    


class Game:
    def __init__(self):
        #verifie si tout les modules sont charges
        module_charge = pygame.init()
        print(module_charge)

        self.caption = pygame.display.set_caption("Snake")

        self.screen = pygame.display.set_mode((500,500))
        # self.screen_color= self.screen.fill('#BFE7CB')
        self.window_size = 500
        self.tile_size = 25
        self.loop = True


    def draw_game(self):
        # Draw grid
        for x in range(0, self.window_size, self.tile_size):
            pygame.draw.line(self.screen, '#9BCFAB', (x, 0), (x, self.window_size))
        for y in range(0, self.window_size, self.tile_size):
            pygame.draw.line(self.screen, '#9BCFAB', (0, y), (self.window_size, y))


    def game_loop(self):
        apple = Apple()
        snake = Snake()

        while self.loop == True :

            self.screen_color= self.screen.fill('#BFE7CB')

            self.draw_game()

            # !!! Que le plus haut qui marche
            snake.draw_snake(self.screen)
            apple.draw_apple(self.screen)

            self.check_event()
            pygame.display.flip()


        pygame.quit()
        sys.exit()
        
   

    def check_event(self):
        for event in pygame.event.get():
            # event input clavier 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.loop = False 
            if event.type == pygame.QUIT:
                self.loop = False




Game().game_loop()
