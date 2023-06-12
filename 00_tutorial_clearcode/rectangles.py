import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Hawis')
clock = pygame.time.Clock()
text_font = pygame.font.Font('00_tutorial_clearcode/font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('00_tutorial_clearcode/graphics/Sky.png').convert()
ground_surface = pygame.image.load('00_tutorial_clearcode/graphics/ground.png').convert()
text_surface = text_font.render('My game', False, 'Black')

snail_surface = pygame.image.load('00_tutorial_clearcode/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))

player_surf = pygame.image.load('00_tutorial_clearcode/graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))

    if snail_rect.right == 0:
        snail_rect.left = 800

    snail_rect.x -= 4

    screen.blit(snail_surface,snail_rect)
    screen.blit(player_surf,player_rect)

    pygame.display.update()
    clock.tick(60)