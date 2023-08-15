import pygame
from pygame.locals import *

pygame.init()

#define screen variables
screen_width = 1024
screen_height = 736
tile_size = 16
#display and caption
screen = pygame.display.set_mode((screen_width, screen_height))

#class world for the grass layer
class World_Grass_Layer():
    def __init__(self, data):
        self.tile_list = []
        #load images
        block_2 = pygame.image.load('Map/levels/images/blocks/grass_blocks/2.png').convert_alpha()
        block_3 = pygame.image.load('Map/levels/images/blocks/grass_blocks/3.png').convert_alpha()
        block_4 =pygame.image.load('Map/levels/images/blocks/grass_blocks/4.png').convert_alpha()
        block_26 =pygame.image.load('Map/levels/images/blocks/grass_blocks/26.png').convert_alpha()
        block_28 =pygame.image.load('Map/levels/images/blocks/grass_blocks/28.png').convert_alpha()
        block_30 =pygame.image.load('Map/levels/images/blocks/grass_blocks/30.png').convert_alpha()
        block_51 =pygame.image.load('Map/levels/images/blocks/grass_blocks/51.png').convert_alpha()
        block_53 =pygame.image.load('Map/levels/images/blocks/grass_blocks/53.png').convert_alpha()
        block_55 =pygame.image.load('Map/levels/images/blocks/grass_blocks/55.png').convert_alpha()
        block_76 =pygame.image.load('Map/levels/images/blocks/grass_blocks/76.png').convert_alpha()
        block_80 =pygame.image.load('Map/levels/images/blocks/grass_blocks/80.png').convert_alpha()
        block_103 =pygame.image.load('Map/levels/images/blocks/grass_blocks/103.png').convert_alpha()
        #go through the mega list and place ablock where the block id is equal to the number 
        row_count = 0
        for row in data:
            #counts where about on the mega list the tile is supposed to be, and that is then the x coordinate
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(block_2,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(block_3,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    img = pygame.transform.scale(block_4,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 5:
                    img = pygame.transform.scale(block_26,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 7:
                    img = pygame.transform.scale(block_28,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 9:
                    img = pygame.transform.scale(block_30,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 10:
                    img = pygame.transform.scale(block_51,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 11:
                    img = pygame.transform.scale(block_28,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 12:
                    img = pygame.transform.scale(block_53,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 13:
                    img = pygame.transform.scale(block_28,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 14:
                    img = pygame.transform.scale(block_55,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 15:
                    img = pygame.transform.scale(block_76,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img and rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 16:
                    img = pygame.transform.scale(block_28,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 17:
                    img = pygame.transform.scale(block_28,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 18:
                    img = pygame.transform.scale(block_28,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 19:
                    img = pygame.transform.scale(block_80,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 21:
                    img = pygame.transform.scale(block_76,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 22:
                    img = pygame.transform.scale(block_103,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 23:
                    img = pygame.transform.scale(block_80,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 6:
                    img = pygame.transform.scale(block_28,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 8:
                    img = pygame.transform.scale(block_28,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

class World_Plants_Layer():
    def __init__(self, data):
        self.tile_list = []
        #load images
        block_0 = pygame.image.load('Map/levels/images/blocks/plants/block_0_0.png').convert_alpha()
        block_1 = pygame.image.load('Map/levels/images/blocks/plants/block_0_1.png').convert_alpha()
        block_2 = pygame.image.load('Map/levels/images/blocks/plants/block_0_2.png').convert_alpha()
        block_3 = pygame.image.load('Map/levels/images/blocks/plants/block_0_3.png').convert_alpha()
        block_4 = pygame.image.load('Map/levels/images/blocks/plants/block_0_4.png').convert_alpha()
        block_12 = pygame.image.load('Map/levels/images/blocks/plants/block_1_0.png').convert_alpha()
        block_13 = pygame.image.load('Map/levels/images/blocks/plants/block_1_1.png').convert_alpha()
        block_14 = pygame.image.load('Map/levels/images/blocks/plants/block_1_2.png').convert_alpha()
        block_15 = pygame.image.load('Map/levels/images/blocks/plants/block_1_3.png').convert_alpha()
        block_16 = pygame.image.load('Map/levels/images/blocks/plants/block_1_4.png').convert_alpha()
        block_24 = pygame.image.load('Map/levels/images/blocks/plants/block_2_0.png').convert_alpha()
        block_25 = pygame.image.load('Map/levels/images/blocks/plants/block_2_1.png').convert_alpha()
        block_26 = pygame.image.load('Map/levels/images/blocks/plants/block_2_2.png').convert_alpha()
        block_28 = pygame.image.load('Map/levels/images/blocks/plants/block_2_4.png').convert_alpha()
        block_29 = pygame.image.load('Map/levels/images/blocks/plants/block_2_5.png').convert_alpha()
        block_40 = pygame.image.load('Map/levels/images/blocks/plants/block_3_4.png').convert_alpha()
        block_49 = pygame.image.load('Map/levels/images/blocks/plants/block_4_1.png').convert_alpha()
        #go through the mega list and place ablock where the block id is equal to the number 
        row_count = 0
        for row in data:
            #counts where about on the mega list the tile is supposed to be, and that is then the x coordinate
            col_count = 0
            for tile in row:
                if tile == 0:
                    img = pygame.transform.scale(block_0,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 1:
                    img = pygame.transform.scale(block_1,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(block_2,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    img = pygame.transform.scale(block_3,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 4:
                    img = pygame.transform.scale(block_4,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 12:
                    img = pygame.transform.scale(block_12,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 13:
                    img = pygame.transform.scale(block_13,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 14:
                    img = pygame.transform.scale(block_14,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 15:
                    img = pygame.transform.scale(block_15,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 16:
                    img = pygame.transform.scale(block_16,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 24:
                    img = pygame.transform.scale(block_24,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 25:
                    img = pygame.transform.scale(block_25,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 26:
                    img = pygame.transform.scale(block_26,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 28:
                    img = pygame.transform.scale(block_28,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 29:
                    img = pygame.transform.scale(block_29,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 40:
                    img = pygame.transform.scale(block_40,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 49:
                    img = pygame.transform.scale(block_49,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


class World_Spike_Layer():
    def __init__(self, data):
        self.tile_list = []
        #load images
        block_3 = pygame.image.load('Map/levels/images/blocks/spike/211.png')
        block_50 = pygame.image.load('Map/levels/images/blocks/spike/115.png')
        block_51 = pygame.image.load('Map/levels/images/blocks/spike/116.png')
        block_52 = pygame.image.load('Map/levels/images/blocks/spike/117.png')
        #go through the mega list and place ablock where the block id is equal to the number 
        row_count = 0
        for row in data:
            #counts where about on the mega list the tile is supposed to be, and that is then the x coordinate
            col_count = 0
            for tile in row:
                if tile == 3:
                    img = pygame.transform.scale(block_3,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 50:
                    img = pygame.transform.scale(block_50,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 51:
                    img = pygame.transform.scale(block_51,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 52:
                    img = pygame.transform.scale(block_52,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size)
                    img_rect.y = (row_count * tile_size)
                    #takes img aand rectangle to be stored
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

            











