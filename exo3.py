# pip install pygame
import pygame 
import sys
import random


class Apple:
    def __init__(self, game):
        self.game = game
        self.color = (220,20,70)
        self.size = game.tile_size
        self.surface = pygame.Surface((self.size,self.size))
        self.radius = self.size // 2
        
        self.range = self.size // 2, self.game.window_size - self.size // 2, self.size
        self.x_food = 250
        self.y_food = 250

    def check_collision(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.x_food =random.randrange(0, 500)
                    self.y_food =random.randrange(0, 500)

    def draw_apple(self):
        
        self.x_food =random.randrange(0, 500)
        self.y_food =random.randrange(0, 500)
        print(self.x_food)
        pygame.draw.circle(self.game.screen, self.color, ( self.x_food, self.y_food), self.radius)

    


    

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
            pygame.draw.line(self.screen, '#003C13', (x, 0), (x, self.window_size))
        for y in range(0, self.window_size, self.tile_size):
            pygame.draw.line(self.screen, '#003C13', (0, y), (self.window_size, y))

        # Draw apple
        # Apple(self).draw_apple()


    def game_loop(self):
        while self.loop == True :

            self.screen_color= self.screen.fill('#BFE7CB')
            # Apple(self).check_collision()

            self.draw_game()
            
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
                if event.key == pygame.K_a:
                    Apple(self).draw_apple()

            if event.type == pygame.QUIT:
                self.loop = False




Game().game_loop()
