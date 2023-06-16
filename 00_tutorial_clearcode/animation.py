import pygame
from sys import exit
from random import randint

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surf = text_font.render(f'Score: {int(current_time / 1000)}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return int(current_time / 1000)

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf,obstacle_rect)
            else:
                screen.blit(fly_surf,obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        
        return obstacle_list
    else: return []

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True

def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 300:
       player_surf = player_jump 
    else:
        player_index += 0.1
        if player_index >= len(player_walk):player_index = 0
        player_surf = player_walk[int(player_index)]
    # play walking animation if the player is on floor
    # display the jump surface when player is not on floor
    # how you ask? by changing the player_surf depending on the status of player

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

#Obstacles
snail_frame_1 = pygame.image.load('00_tutorial_clearcode/graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('00_tutorial_clearcode/graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]


fly_frame_1 = pygame.image.load('00_tutorial_clearcode/graphics/fly/fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('00_tutorial_clearcode/graphics/fly/fly2.png').convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]

obstacle_rect_list = []

player_walk_1 = pygame.image.load('00_tutorial_clearcode/graphics/player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('00_tutorial_clearcode/graphics/player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1,player_walk_2]
player_index = 0
player_jump = pygame.image.load('00_tutorial_clearcode/graphics/player/jump.png').convert_alpha()

player_surf = player_walk[player_index]
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

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer,500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer,200)

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
                    game_active = True
                    start_time = pygame.time.get_ticks()

        if game_active:
            if event.type == obstacle_timer:
                if randint(0,2):    
                    obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900,1100),300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100),210)))
            if event.type == snail_animation_timer:
                if snail_frame_index == 0: snail_frame_index = 1
                else: snail_frame_index = 0
                snail_surf = snail_frames[snail_frame_index]
            if event.type == fly_animation_timer:
                if fly_frame_index == 0: fly_frame_index = 1
                else: fly_frame_index = 0
                fly_surf = fly_frames[fly_frame_index]

    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))

        #pygame.draw.rect(screen,'#c0e8ec',score_rect)
        #pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
        #screen.blit(score_surf,score_rect)
        score = display_score()

        #if snail_rect.right <= 0:
        #    snail_rect.left = 800
        #snail_rect.x -= 6
        #screen.blit(snail_surface,snail_rect)

        #Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom > 300 : 
            player_rect.bottom = 300 
        player_animation()
        screen.blit(player_surf,player_rect)

        #Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        game_active = collisions(player_rect,obstacle_rect_list) 
            
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        screen.blit(title_surf,title_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,300)
        player_gravity = 0

        prevscore_surf = text_font.render(f'Score: {score}', False, TEXTCOLOR)
        prevscore_rect = prevscore_surf.get_rect(center = (400,325))

        if score == 0:
            screen.blit(instruction_surf,instruction_rect)
        else:
            screen.blit(prevscore_surf,prevscore_rect)

    pygame.display.update()
    clock.tick(60)