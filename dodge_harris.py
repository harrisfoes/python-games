#make window - done
#make player display - done
    #make player move - done
#make baddies appear
    #make baddies move
    #handle creation and deletion of baddies
#keep score based on clock
#When badies and player collide, end game
#figure out game loop

import pygame,random,sys
from pygame.locals import *

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
FPS = 40
PLAYERMOVESPEED = 5
BACKGROUNDCOLOR = (0,0,0)
BADDIESIZE = 40
ADDBADDIERATE = 5

pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Dodger harris version')
#pygame.mouse.set_visible(False)

playerImage = pygame.image.load('player.png')
playerRect = playerImage.get_rect()
baddieImage = pygame.image.load('baddie.png')

moveUp = moveLeft = moveRight = moveDown = False
baddies = [];
baddieAddCounter = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT:
                moveRight = True
                moveLeft = False
            if event.key ==  K_UP:
                moveUp = True
                moveDown = False
            if event.key == K_DOWN:
                moveDown = True
                moveUp = False

    #update
    if moveLeft and playerRect.left > 0:
        playerRect.move_ip(-1 * PLAYERMOVESPEED, 0)
    if moveRight and playerRect.right < WINDOWWIDTH:
        playerRect.move_ip(PLAYERMOVESPEED, 0)
    if moveUp and playerRect.top > 0:
        playerRect.move_ip(0,-1 * PLAYERMOVESPEED)
    if moveDown and playerRect.bottom < WINDOWHEIGHT:
        playerRect.move_ip(0, PLAYERMOVESPEED)

    #spawn baddies
    baddieAddCounter += 1;
    if baddieAddCounter == ADDBADDIERATE:
        baddieAddCounter = 0
        newBaddie = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH-BADDIESIZE), 0 - BADDIESIZE, BADDIESIZE, BADDIESIZE),
                    'speed': 5,
                    'surface': pygame.transform.scale(baddieImage,(BADDIESIZE,BADDIESIZE))
                    }
        baddies.append(newBaddie)

    for i in baddies:
        i['rect'].move_ip(0, i['speed'])

    for b in baddies[:]:
        if b['rect'].top > WINDOWHEIGHT:
            baddies.remove(b)
    
    #draw
    windowSurface.fill(BACKGROUNDCOLOR)
    windowSurface.blit(playerImage, playerRect)

    for b in baddies:
        windowSurface.blit(b['surface'], b['rect'])

    pygame.display.update()
    mainClock.tick(FPS)
