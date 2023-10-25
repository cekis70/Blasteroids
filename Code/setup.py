import pygame, sys


class Ship(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load("C:\Repos\Blasteroids\Graphics\ship.png").convert_alpha()
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
    
    def input_position(self):
        self.rect.center = pygame.mouse.get_pos()

    def update(self):
        self.input_position()


class Laser(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.image = pygame.image.load("C:\Repos\Blasteroids\Graphics\laser.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)


pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT  = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("BLASTEROIDS")
clock = pygame.time.Clock()
background_surface = pygame.image.load("C:\Repos\Blasteroids\Graphics\\background.png").convert()

spaceship_group = pygame.sprite.Group()
laser_group = pygame.sprite.Group()
ship = Ship(spaceship_group)
laser = Laser(laser_group, (200, 200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dt = clock.tick() / 1000
    display_surface.blit(background_surface,(0,0))
    spaceship_group.update()
    spaceship_group.draw(display_surface)
    laser_group.draw(display_surface)
    
    pygame.display.update()

