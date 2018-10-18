import pygame
from pygame.locals import *
from sys import exit

def playground():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), 0, 32)
    pygame.display.set_caption('myGame')
    screen.fill((0, 0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        pygame.display.update()
if __name__ == '__main__':
    playground()