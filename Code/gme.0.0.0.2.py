import pygame
import os
from settings import *
from map_data_level_0 import level_0_terrain
from blocks import *

pygame.init()
#frames
FPS = 60
clock = pygame.time.Clock()
#caption and display
screen = pygame.display.set_mode((screen_width, screen_height ))
pygame.display.set_caption('gme.0.0.0.1')


#gaame variables
ROWS = 46
MAX_COLS = 192
TILE_TYPES = 625
scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 0.5

#load images
sky = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers_fullcolor/sky_fc.png').convert_alpha()
cloud1 = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers_fullcolor/clouds_front_fc.png').convert_alpha()
cloud2 = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers_fullcolor/clouds_mid_fc.png').convert_alpha()
mountains1  = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers_fullcolor/far_mountains_fc.png').convert_alpha()
mountains2 = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers_fullcolor/grassy_mountains_fc.png').convert_alpha()
#load all images 
#store tiles in a list
img_list = []
for x in range(104):
    img = pygame.image.load(f'Map/levels/images/blocks/need/terrain_used/placed in 0-94 or sum/{x}.png')
    img_list.append(img)





#define colours
GREEN = (144, 201, 120)
WHITE = (255, 255, 255)
RED = (200, 25 , 25)

#change height and width
sky_img = pygame.transform.scale(sky, (screen_width, screen_height))
cloud1_img = pygame.transform.scale(cloud1,  (screen_width, screen_height))
cloud2_img = pygame.transform.scale(cloud2, (screen_width, screen_height))
mountains1_img = pygame.transform.scale(mountains1, (screen_width, screen_height))
mountains2_img = pygame.transform.scale(mountains2, (screen_width, screen_height))

class World():
    def __init__(self):
        self.obstacle_list = []

    def proccess_data(self, data):
        #iterate through each value in data 
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    img = img_list[tile]
                    img_rect = img.get_rect()
                    img_rect.x = x * tile_size
                    img_rect.x = y * tile_size
                    tile_data = (img, img_rect)
                    if tile >= 0 and tile <= 104:
                        self.obstacle_list.append(tile_data)

    #def draw(self):
        #for tile in level_0_terrain:
            #screen.blit



        


#creatr function for background drawing
def draw_bg():
    screen.fill(GREEN)
    width = sky_img.get_width()
    for x in range(3):
        screen.blit(sky_img, ((x * width) -scroll * 0.5, 0))
        screen.blit(mountains1_img, ((x * width) -scroll * 0.6, 0))
        screen.blit(mountains2_img, ((x * width) -scroll * 0.7, 0))
        screen.blit(cloud2_img, ((x * width) -scroll * 0.8, 0))
        screen.blit(cloud1_img, ((x * width) -scroll * 0.9, 0))



#draw grid
def draw_grid():
    #verical lines
    for c in range(MAX_COLS + 1):
        pygame.draw.line(screen, WHITE, (c * tile_size -scroll , 0),(c * tile_size -scroll, screen_height))
    #horizontal lines
    for c in range(ROWS + 1):
        pygame.draw.line(screen, WHITE, (0, c * tile_size),(screen_width, c *tile_size))

#create empty tile list
#world =  World()


run = True
while run:


    clock.tick(FPS)

    #world.draw()
    draw_bg()
    draw_grid()
    #draw wrld



    #scroll the map
    if scroll_left == True and scroll > 0:
        scroll -= 5 * scroll_speed
    if scroll_right == True:
        scroll += 5 *scroll_speed

 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #keyboard presses
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            scroll_left = True
        if event.key == pygame.K_RIGHT:
            scroll_right = True
        if event.key == pygame.K_RSHIFT:
            scroll_speed = 5

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            scroll_left = False
        if event.key == pygame.K_RIGHT:
            scroll_right = False
        if event.key == pygame.K_RSHIFT:
            scroll_speed = 1



    pygame.display.update()

pygame.quit()