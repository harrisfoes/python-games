import pygame, sys

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 480
CREAM = '#f8e3c4'
MAGENTA = '#cc3495'
PURP = '#6b1fb1'
BLUCK = '#0b0630'
MOVERATE = 5

pygame.init()
screen = pygame.display.set_mode((600,480))
pygame.display.set_caption('This is my playground')
clock = pygame.time.Clock()

moving_up = moving_down = moving_right = moving_left = False

player_surf = pygame.image.load('01_dodgegame/mydodgegame/graphics/player.png').convert_alpha()
player_surf = pygame.transform.scale(player_surf, (34,42))
player_rect = player_surf.get_rect(midbottom = (300,400))

def welcome_screen():
    screen.fill(BLUCK)
    font = pygame.font.Font('01_dodgegame/mydodgegame/fonts/Hack.ttf',25)
    welcome_surf = font.render("Hello Human, evade the baddies", False, CREAM)
    welcome_rect = welcome_surf.get_rect(midbottom=(300,100)) 
    inst_surf = font.render("Press space.", False, CREAM)
    inst_rect = welcome_surf.get_rect(midbottom=(300,200))
    screen.blit(welcome_surf,welcome_rect);
    screen.blit(inst_surf,inst_rect)

game_active = False 

while True:
    #check events/inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    moving_up = True
                    moving_down = False
                elif event.key == pygame.K_a:
                    moving_left = True
                    moving_right = False
                elif event.key == pygame.K_s:
                    moving_down = True
                    moving_up = False
                elif event.key == pygame.K_d:
                    moving_right = True
                    moving_left = False
        else:
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                game_active = True

    #update here
    if game_active:
        if moving_down and player_rect.bottom < WINDOW_HEIGHT:
            player_rect.move_ip(0, 1 * MOVERATE)
        if moving_up and player_rect.top > 0:
            player_rect.move_ip(0, -1 * MOVERATE)
        if moving_right and player_rect.right < WINDOW_WIDTH:
            player_rect.move_ip(1 * MOVERATE, 0)
        if moving_left and player_rect.left > 0:
            player_rect.move_ip(-1 * MOVERATE, 0)

    #draw functions
    if game_active:
        screen.fill(BLUCK)
        screen.blit(player_surf,player_rect)
    else:
        welcome_screen()

    
    pygame.display.update()
    clock.tick(60)