import pygame
pygame.init()
#define screen variables
screen_width = 1024
screen_height = 736
tile_size = 16
screen = pygame.display.set_mode((screen_width, screen_height))

class Player():
    def __init__(self, x ,y):
        #animation
        self.images_right = []
        self.index = 0
        self.counter = 0 
        for num in range(0,7):
            img_right = pygame.image.load(f'Map/levels/images/player/run_{num}.png')
            img_right = pygame.transform.scale(img_right,(32,32))
            self.images_right.append(img_right)
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = False
        #velocity of jump
    def update(self):
        dx = 0
        dy = 0
        walk_cooldown = 5
        #change in y and change in x

        #get keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx -= 5
            self.counter  += 1
        if key[pygame.K_d]:
            dx += 5
            self.counter += 1
        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y =- 12
            self.jumped = True
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        if key[pygame.K_a] == False and key[pygame.K_d] == False:
            self.counter = 0
            self.index = 0
            self.image = self.images_right[self.index]

        #animation handling 
        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 1 
            if self.index >= len(self.images_right):
                self.index = 0
            self.image = self.images_right[self.index]



        #add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        #check for collison

        #update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        #temporary check
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            dy = 0

        #draw player on the screen
        screen.blit(self.image, self.rect)