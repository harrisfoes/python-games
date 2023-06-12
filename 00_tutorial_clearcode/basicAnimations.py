import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Hawis')
clock = pygame.time.Clock()
text_font = pygame.font.Font('00_tutorial_clearcode/font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('00_tutorial_clearcode/graphics/Sky.png')
ground_surface = pygame.image.load('00_tutorial_clearcode/graphics/ground.png')
text_surface = text_font.render('My game', False, 'Black')

snail_surface = pygame.image.load('00_tutorial_clearcode/graphics/snail/snail1.png')
snail_x_pos = 600

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))

    if snail_x_pos <= 0:
        snail_x_pos = 800
        
    snail_x_pos -= 4
    screen.blit(snail_surface,(snail_x_pos,250))

    pygame.display.update()
    clock.tick(60)