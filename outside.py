import pygame, sys, math
from sys import exit
import random
from random import randint

screen = pygame.display.set_mode((1000, 800))
player1 = pygame.image.load('C:\\Users\\Robert\\Downloads\\topdown\\topplayer.png')

ground = pygame.image.load('C:\\Users\\Robert\\Downloads\\topdown\\Groundeagle.png')
running = True
clock = pygame.time.Clock()
WIDTH = 1000
HEIGHT = 800



class Object:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(randint(0, 800), randint(0, 800), 32, 32)
        self.color = (59, 82, 61)
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

object = Object(randint(0, 0), randint(0, 0))

class Player:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.color = (217, 177, 78)
        self.velX = 0
        self.velY = 0
        self.speed = 5

        #tools
        self.selected_tool = 'axe'
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

        
    
        
        

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)

    def input(self):
        self.velX = 0
        self.velY = 0
        keys = pygame.key.get_pressed()

        
        if keys[pygame.K_w]:
                self.velY = -self.speed
        if keys[pygame.K_a]:
                self.velX = -self.speed
        if keys[pygame.K_d]:
                self.velX = self.speed
        if keys[pygame.K_s]:
                self.velY = self.speed
        if keys[pygame.K_SPACE]:
            print('use')
        #
        self.x += self.velX
        self.y += self.velY

        if self.rect.left + self.x < 0:
            self.x = -self.rect.left
        if self.rect.right + self.x > 1970:
            self.x = 1970 -self.rect.right
        if self.rect.top + self.y < 0:
            self.y = -self.rect.top
        if self.rect.bottom + self.y > 1570:
            self.y = 1570 -self.rect.bottom
        
             
             


player = Player(WIDTH/2, HEIGHT/2)
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if player.rect.colliderect(object.rect):
         object.rect.x, object.rect.y = randint(0, 800), randint(0, 800)
        
        
    object.draw(screen)
    
             
        
    
    
        
        

    #Movement
    player.input()
        
        
    
    screen.fill((48, 48, 48))  
    player.draw(screen)
    object.draw(screen)

    
    
    pygame.display.flip()

    clock.tick(60)
