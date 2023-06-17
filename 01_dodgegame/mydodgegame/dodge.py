import pygame, sys

pygame.init()
screen = pygame.display.set_mode((600,480))
pygame.display.set_caption('This is my playground')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #update
    pygame.display.update()

    