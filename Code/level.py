import pygame
from support import import_csv_layout, import_cut_graphic
from settings import tile_size
from tiles import Tile
class Level:
    def __init__(self, level_data, surface):
        #general setup
        self.display_surface = surface
        self.world_shift = 0

        #terrain setup
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprite = self.create_tile_group(terrain_layout, 'terrain')

    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()
        

        for row_index, row in enumerate(layout):
            print(row_index)
            print(row)
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size


                    #if type == 'terrain':
                        #terrain_tile_list = import_cut_graphic("C:/Users/decla/OneDrive/Desktop/PythonGameProject/Map/levels/images/Tiles/Assets/Assets.png")
                        #sprite = Tile(tile_size, x, y)
                        #sprite_group.add(sprite)

        return sprite_group








    def run(self):
        #run whole game level
        self.terrain_sprite.draw(self.display_surface)
        self.terrain_sprite.update(self.world_shift)