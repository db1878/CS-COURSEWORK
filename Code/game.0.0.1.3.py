import pygame
from pygame.locals import *
import os
from map_data_level_0 import level_0_terrain
from loadimg import *


pygame.init()
#frames
FPS = 60
clock = pygame.time.Clock()
#variables
screen_width = 1024
screen_height = 736
tile_size = 16

#caption and display

screen = pygame.display.set_mode((screen_width, screen_height ))
pygame.display.set_caption('gme.0.0.0.1')

#define colours
GREEN = (144, 201, 120)
WHITE = (255, 255, 255)
RED = (200, 25 , 25)




    




       

world_data = level_0_terrain





        





        









run = True
while run:


    clock.tick(FPS)

    screen.fill(WHITE)

    




 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False






    

    pygame.display.update()

pygame.quit()