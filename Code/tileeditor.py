import pygame


pygame.init()

FPS = 60
clock = pygame.time.Clock()

#game window

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
LOWER_MARGIN = 100
SIDE_MARGIN = 300

screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.display.set_caption('level editor')

#gaame variables
ROWS = 16
MAX_COLS = 150
TILE_SIZE = SCREEN_HEIGHT // ROWS
TILE_TYPES = 18
scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1




#load images
sky = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers_fullcolor/sky_fc.png').convert_alpha()
cloud1 = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers_fullcolor/clouds_front_fc.png').convert_alpha()
cloud2 = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers_fullcolor/clouds_mid_fc.png').convert_alpha()
mountains1  = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers_fullcolor/far_mountains_fc.png').convert_alpha()
mountains2 = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers_fullcolor/grassy_mountains_fc.png').convert_alpha()
#mountains3 = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers_fullcolor/hill.png').convert_alpha()

#store tiles in a list
img_list = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f'Map/Background IMG/Dirt/{x}.png.png')
    img = pygame.transorm.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)



#define colours
GREEN = (144, 201, 120)
WHITE = (255, 255, 255)
RED = (200, 25 , 25)

#change height and width
sky_img = pygame.transform.scale(sky, (800, 600))
cloud1_img = pygame.transform.scale(cloud1, (800, 600))
cloud2_img = pygame.transform.scale(cloud2, (800, 600))
mountains1_img = pygame.transform.scale(mountains1, (800, 600))
mountains2_img = pygame.transform.scale(mountains2, (800, 600))
#mountains3_img = pygame.transform.scale(mountains3, (800, 600))

#creatr function for background drawing
def draw_bg():
    screen.fill(GREEN)
    width = sky_img.get_width()
    for x in range(4):
        screen.blit(sky_img, ((x * width) -scroll * 0.5, 0))
        screen.blit(mountains1_img, ((x * width) -scroll * 0.6, 0))
        screen.blit(mountains2_img, ((x * width) -scroll * 0.7, 0))
        screen.blit(cloud2_img, ((x * width) -scroll * 0.8, 0))
        screen.blit(cloud1_img, ((x * width) -scroll * 0.9, 0))
        #screen.blit(mountains3_img, ((x * width) -scroll, 0))


#draw grid
def draw_grid():
    #verical lines
    for c in range(MAX_COLS + 1):
        pygame.draw.line(screen, WHITE, (c * TILE_SIZE -scroll , 0),(c * TILE_SIZE -scroll, SCREEN_HEIGHT))
    #horizontal lines
    for c in range(ROWS + 1):
        pygame.draw.line(screen, WHITE, (0, c * TILE_SIZE),(SCREEN_WIDTH, c * TILE_SIZE))




run = True
while run:
    
    clock.tick(FPS)


    draw_bg()
    draw_grid()


  
  
  
  
  
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