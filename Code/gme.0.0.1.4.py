import pygame
from pygame.locals import *
from world_class import *
from playerclass import Player
from level_map_data import *

pygame.init()

#define screen variables
screen_width = 1024
screen_height = 736
#display and caption
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('gme.0.0.1.4')
#define game variables
tile_size = 16
FPS = 60
clock = pygame.time.Clock()
#define colours 
GREEN = (144, 201, 120)
WHITE = (255, 255, 255)
RED = (200, 25 , 25)
#load images
sky = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers_fullcolor/sky_fc.png').convert_alpha()
cloud1 = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers_fullcolor/clouds_front_fc.png').convert_alpha()
cloud2 = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers_fullcolor/clouds_mid_fc.png').convert_alpha()
mountains1  = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers_fullcolor/far_mountains_fc.png').convert_alpha()
mountains2 = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers_fullcolor/grassy_mountains_fc.png').convert_alpha()
#change height and width
sky_img = pygame.transform.scale(sky, (screen_width, screen_height))
cloud1_img = pygame.transform.scale(cloud1,  (screen_width, screen_height))
cloud2_img = pygame.transform.scale(cloud2, (screen_width, screen_height))
mountains1_img = pygame.transform.scale(mountains1, (screen_width, screen_height))
mountains2_img = pygame.transform.scale(mountains2, (screen_width, screen_height))
#class player

player = Player(32, screen_height - 128)
#player is drawn on the coordinates (tile_size * 2, screen_height - 16* 7 ) because it is the second block across and 7 blocks up from the bottom
world_grass = World_Grass_Layer(grass_layer_world_data)
world_plants = World_Plants_Layer(plants_layer_world_data)
world_spike = World_Spike_Layer(spike_world_data)


#game loop
run = True
while run:
    clock.tick(FPS)

    screen.blit(sky_img,(0, 0))
    screen.blit(mountains1_img,(0, 0))
    screen.blit(mountains2_img,(0, 0))
    screen.blit(cloud1_img,(0, 0))
    screen.blit(cloud2_img,(0, 0))

    
    world_grass.draw()
    world_plants.draw()
    world_spike.draw()
    player.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()