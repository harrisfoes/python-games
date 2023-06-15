import pygame
from sys import exit

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surf = text_font.render(f'Score: {int(current_time / 1000)}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return int(current_time / 1000)


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Hawis')
clock = pygame.time.Clock()
text_font = pygame.font.Font('00_tutorial_clearcode/font/Pixeltype.ttf', 50)
TEXTCOLOR = (111,196,169)
score = 0

game_active = False
start_time = 0

sky_surface = pygame.image.load('00_tutorial_clearcode/graphics/Sky.png').convert()
ground_surface = pygame.image.load('00_tutorial_clearcode/graphics/ground.png').convert()

#score_surf = text_font.render('My game', False, (64,64,64))
#score_rect = score_surf.get_rect(center = (400,50))

snail_surface = pygame.image.load('00_tutorial_clearcode/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))

player_surf = pygame.image.load('00_tutorial_clearcode/graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80,300))
player_gravity = 0

#Intro screen
player_stand = pygame.image.load('00_tutorial_clearcode/graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

title_surf = text_font.render('Running Game', False, TEXTCOLOR)
title_rect = title_surf.get_rect(center = (400,50))
instruction_surf = text_font.render('Press Space to start', False, TEXTCOLOR)
instruction_rect = instruction_surf.get_rect(center = (400,325))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()    
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:           
                if player_rect.collidepoint(event.pos) and event.button == 1:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN and player_rect.bottom == 300:
                if event.key == pygame.K_SPACE:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    snail_rect.x = 600
                    game_active = True
                    start_time = pygame.time.get_ticks()


    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))

        #pygame.draw.rect(screen,'#c0e8ec',score_rect)
        #pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
        #screen.blit(score_surf,score_rect)
        score = display_score()
        print(score)

        if snail_rect.right <= 0:
            snail_rect.left = 800
        snail_rect.x -= 6
        screen.blit(snail_surface,snail_rect)

        #Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom > 300 : 
            player_rect.bottom = 300 
        screen.blit(player_surf,player_rect)

        #collision
        if snail_rect.colliderect(player_rect):
            game_active = False
            
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        screen.blit(title_surf,title_rect)
        prevscore_surf = text_font.render(f'Score: {score}', False, TEXTCOLOR)
        prevscore_rect = prevscore_surf.get_rect(center = (400,325))

        if score == 0:
            screen.blit(instruction_surf,instruction_rect)
        else:
            screen.blit(prevscore_surf,prevscore_rect)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_state = True

    pygame.display.update()
    clock.tick(60)