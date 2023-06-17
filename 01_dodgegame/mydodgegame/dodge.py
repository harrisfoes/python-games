import pygame, sys

pygame.init()
screen = pygame.display.set_mode((600,480))
pygame.display.set_caption('This is my playground')
clock = pygame.time.Clock()

player_surf = pygame.image.load('01_dodgegame/mydodgegame/graphics/player.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (300,200))

def welcome_screen():
    screen.fill((25,40,25))
    font = pygame.font.Font('01_dodgegame/mydodgegame/fonts/Hack.ttf',25)
    welcome_surf = font.render("Hello Human, evade the baddies", False, (200,200,200))
    welcome_rect = welcome_surf.get_rect(midbottom=(300,100)) 
    inst_surf = font.render("Press space.", False, (200,200,200))
    inst_rect = welcome_surf.get_rect(midbottom=(500,200))
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
            pass
        else:
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                game_active = True

    #update here

    #draw functions
    if game_active:
        screen.fill((0,0,0))
        screen.blit(player_surf,player_rect)
    else:
        welcome_screen()

    
    pygame.display.update()
    clock.tick(60)