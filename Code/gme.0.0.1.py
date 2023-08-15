import pygame

pygame.init()


FPS = 60
clock = pygame.time.Clock()


#scrn variBALES
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = int(1024 * 0.71875)
#1024x736

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT ))
pygame.display.set_caption('gme.0.0.1')

#define player variables
moving_left = False
moving_right = False


class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        img = pygame.image.load('Map/Characters/Sprites/4-idle/20.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), (int(img.get_height() *scale))))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self, moving_left, moving_right):
        #reset movement variables (change in y and change in x (dy/dx))
        dx = 0
        dy = 0

        #assign movement variables if moving left or roght
        if moving_left == True:
            dx = -self.speed
        if moving_right == True:
            dx = self.speed

        #update rectangle pos
        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        screen.blit(self.image, self.rect)


player = Character(200, 200, 2, 5)



#load images
sky = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers_fullcolor/sky_fc.png').convert_alpha()
cloud1 = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers_fullcolor/clouds_front_fc.png').convert_alpha()
cloud2 = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers_fullcolor/clouds_mid_fc.png').convert_alpha()
mountains1  = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers_fullcolor/far_mountains_fc.png').convert_alpha()
mountains2 = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers_fullcolor/grassy_mountains_fc.png').convert_alpha()
#mountains3 = pygame.image.load('Map/Background IMG/mountains/Grassy_Mountains_Parallax_Background-vnitti/Grassy_Mountains_Parallax_Background-vnitti/layers_fullcolor/hill.png').convert_alpha()








run = True
while run:


    clock.tick(FPS)

    
    player.draw()

    player.move(moving_left, moving_right)

    
    

    
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #keyboard presses
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            moving_left = True
        if event.key == pygame.K_d:
            moving_right = True
        if event.key == pygame.K_ESCAPE:
            run = False
    #keyboard up
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a:
            moving_left = False
        if event.key == pygame.K_d:
            moving_right = False



    pygame.display.update()

pygame.quit()