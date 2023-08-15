import pygame, sys
from settings import *
from level import Level
from gamedata import level_0
from map_data_level_0 import level_0_terrain

#pygame setup
pygame.init()
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height ))
pygame.display.set_caption('gme.0.0.1')
level = Level(level_0, screen)


#game data
class World():
    def __init__(self, data):
        self.tile_list = []
#load images





run = True
while run:


    clock.tick(FPS)

 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    

    screen.fill('black')
    level.run()


    pygame.display.update()

pygame.quit()