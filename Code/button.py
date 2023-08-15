import pygame

pygame.init()

#scrn
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('button')

#load button images
img_list = []
for x in range(18):
    img = pygame.image.load(f'Map/Background IMG/Dirt/{x}.png.png').convert_alpha()
    #img = pygame.transorm.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)


#button class
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.iamgee.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        #draw button on screen
        screen.blit(self.image(self.rect.x, self.rect.y))

#button instances
    


#game loop
run = True
while run:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.display.update()


pygame.quit()