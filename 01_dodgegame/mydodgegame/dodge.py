import pygame, sys, random

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 480
CREAM = '#f8e3c4'
MAGENTA = '#cc3495'
PURP = '#6b1fb1'
BLUCK = '#0b0630' 
MOVERATE = 5
BGCOLOR = (94,129,162)
BADDIEMINSIZE = 25
BADDIEMAXSIZE = 50
BADDIEMINSPEED = 3
BADDIEMAXSPEED = 8
BADDIEFREQ = 5

pygame.init()
screen = pygame.display.set_mode((600,480))
pygame.display.set_caption('This is my playground')
clock = pygame.time.Clock()

moving_up = moving_down = moving_right = moving_left = False
score = 0

player_surf = pygame.image.load('graphics/player.png').convert_alpha()
player_surf = pygame.transform.scale(player_surf, (34,42))
player_rect = player_surf.get_rect(midbottom = (300,400))

baddie_surf = pygame.image.load('graphics/baddie.png').convert_alpha()
baddie_list = []
baddieAddCounter = 0

#gameOverSound = pygame.mixer.Sound('broop.mp3')
pygame.mixer.music.load('audio/broop.mp3')

#score_surf = font.render(f"Score: {score}", False, BLUCK)
#score_rect = score_surf.get_rect(bottomleft = (5,WINDOW_HEIGHT - 30))

def welcome_screen():
    screen.fill(MAGENTA)
    font = pygame.font.Font('fonts/Pixeltype.ttf',50)
    welcome_surf = font.render("It's raining baddies!", False, CREAM)
    welcome_rect = welcome_surf.get_rect(midbottom=(300,100)) 
    inst_surf = font.render("Press space.", False, CREAM)
    inst_rect = welcome_surf.get_rect(midbottom=(300,200))
    screen.blit(welcome_surf,welcome_rect);
    screen.blit(inst_surf,inst_rect)

def player_collide(player,baddie_list):
    for baddie in baddie_list:
        if player.colliderect(baddie['rect']):
            return True
    return False


game_active = False 
pygame.mixer.music.play(-1, 0.0)

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
                if event.key == pygame.K_a:
                    moving_left = True
                    moving_right = False
                if event.key == pygame.K_s:
                    moving_down = True
                    moving_up = False
                if event.key == pygame.K_d:
                    moving_right = True
                    moving_left = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    moving_up = False
                if event.key == pygame.K_a:
                    moving_left = False
                if event.key == pygame.K_s:
                    moving_down = False
                if event.key == pygame.K_d:
                    moving_right = False
        else:
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                game_active = True
                score = 0
                pygame.mixer.music.rewind()


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

        score += 1
        baddieAddCounter += 1

        if baddieAddCounter == BADDIEFREQ:
            baddieAddCounter = 0
            baddie_size = random.randint(BADDIEMINSIZE,BADDIEMAXSIZE)
            new_baddie = {'rect' : baddie_surf.get_rect(topleft = (random.randint(1,WINDOW_WIDTH - BADDIEMAXSIZE),0)),
                        'surf' : pygame.transform.scale(baddie_surf, (baddie_size,baddie_size)),
                        'speed' : random.randint(BADDIEMINSPEED,BADDIEMAXSPEED)}
            baddie_list.append(new_baddie)
        
        for baddies in baddie_list:
            #print(len(baddie_list))
            if baddies['rect'].top > WINDOW_HEIGHT:
                baddie_list.remove(baddies)
            else:
                baddies['rect'].move_ip(0, baddies['speed'])

        if player_collide(player_rect, baddie_list):
            game_active = False
            baddie_list.clear()
            pygame.mixer.music.rewind()
            
    #draw functions
    font = pygame.font.Font('fonts/Pixeltype.ttf',30)
    score_surf = font.render(f"Score: {score}", False, CREAM)
    score_rect = score_surf.get_rect(bottomleft = (5,WINDOW_HEIGHT - 30))

    if game_active:
        screen.fill(BGCOLOR)
        screen.blit(player_surf,player_rect)
        
        for baddies in baddie_list[:]:
            screen.blit(baddies['surf'],baddies['rect'])

        screen.blit(score_surf,score_rect)
    else:
        welcome_screen()
        if score > 0:
            screen.blit(score_surf,score_surf.get_rect(midbottom = (300, 300)))

    
    pygame.display.update()
    clock.tick(60)