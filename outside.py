#All keys that are used: W, A, S, D, SPACE
import pygame, sys, math
from sys import exit
import random
from random import randint

screen = pygame.display.set_mode((1000, 800))

running = True
clock = pygame.time.Clock()
WIDTH = 1000
HEIGHT = 800
running = True
wood = 0
mousepos = pygame.mouse.get_pos()

cube_size = 80
cube_x = random.randint(0, WIDTH - cube_size)
cube_y = random.randint(0, HEIGHT - cube_size)

class Thing:
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
    def draw(self, screen):
        screen.blit(pygame.transform.scale(self.image, (self.width, self.height)), (self.x, self.y))

    def get_center(self):
         return self.x + self.width / 2, self.y + self.height / 2
          

     
class Object:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(randint(0, 800), randint(0, 800), 32, 32)
        self.color = (59, 82, 61)
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    

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
        self.width = 32
        self.height = 32
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

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
    def get_center(self):
         return self.x + self.width / 2, self.y + self.height / 2
    def update(self):
         self.x += self.velX
         self.y += self.velY
         self.draw(screen)
    
target = Thing(0, 0, 50, 50, pygame.image.load('C:\\Users\\Robert\\Downloads\\Cursor.png'))

class Nature:
    def __init__(self, x, y, width, height, color):
        
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, width, height)
        self.color = color
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

tree = Nature(random.randint(0, WIDTH - 32), random.randint(0, HEIGHT - 32), 32, 32, (71, 46, 12))
nature = []
player = Player(WIDTH/2, HEIGHT/2)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        
    if running:
        
        if player.rect.colliderect(object.rect):
            object.rect.x, object.rect.y = randint(0, 800), randint(0, 800)
            wood += 1
            print(wood)
        if event.type == pygame.MOUSEBUTTONDOWN:
                print("Mouse clicked")

                for tree in nature:
                    if tree.rect.collidepoint(mousepos):
                        print('treemove')
                        nature.remove(tree)
        

        if object.rect.x < player.x:
                object.rect.x += 2
        elif object.rect.x > player.x:
                object.rect.x -= 2

        if object.rect.y < player.y:
                object.rect.y += 2
        elif object.rect.y > player.y:
                object.rect.y -= 2

        pygame.mouse.set_visible(False)
        player.input()
        screen.fill((48, 48, 48))  
        player.draw(screen)
        object.draw(screen)
        tree.draw(screen)
        random.randint(0, WIDTH - cube_size)
        mousePos = pygame.mouse.get_pos()
        target.x = mousePos[0] - target.width / 2
        target.y = mousePos[1] - target.height / 2
        screen.blit(pygame.image.load('C:\\Users\\Robert\\Downloads\\Cursor.png'), (target.x , target.y))
        if event.type == pygame.MOUSEBUTTONDOWN and wood >= 5:
            cube_x = mousePos[0] - target.width / 2
            cube_y = mousePos[1] - target.height / 2
            wood -= 5
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            pygame.draw.rect(screen, (255, 0, 0), (player.rect.centerx - cube_size/2 , player.rect.centery - cube_size/2, cube_size, cube_size), 2)

        pygame.display.update()
        pygame.display.flip()

        clock.tick(60)
