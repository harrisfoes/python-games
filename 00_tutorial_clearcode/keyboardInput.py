import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Hawis')
clock = pygame.time.Clock()
text_font = pygame.font.Font('00_tutorial_clearcode/font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('00_tutorial_clearcode/graphics/Sky.png').convert()
ground_surface = pygame.image.load('00_tutorial_clearcode/graphics/ground.png').convert()

score_surf = text_font.render('My game', False, (64,64,64))
score_rect = score_surf.get_rect(center = (400,50))

snail_surface = pygame.image.load('00_tutorial_clearcode/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))

player_surf = pygame.image.load('00_tutorial_clearcode/graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            print(event.pos)    
        # if event.type == pygame.MOUSEMOTION:
        #    if player_rect.collidepoint(event.pos):
        #        print('Don touch me')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('jump')
        if event.type == pygame.KEYUP:
            print('keyup')


    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    pygame.draw.rect(screen,'#c0e8ec',score_rect)
    pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
    #pygame.draw.line(screen,'Gold',(0,0),pygame.mouse.get_pos(), 5)
    #pygame.draw.ellipse(screen,'Brown',pygame.Rect(50,200,100,200))
    screen.blit(score_surf,score_rect)

    if snail_rect.right == 0:
        snail_rect.left = 800

    snail_rect.x -= 4

    screen.blit(snail_surface,snail_rect)
    screen.blit(player_surf,player_rect)

    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_SPACE]:
    #    print('jump')

    # returns 0 or 1
    # if player_rect.colliderect(snail_rect):
    #     print('collision')
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print('collision')
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)