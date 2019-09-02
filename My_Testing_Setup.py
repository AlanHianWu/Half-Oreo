#!/usr/bin/env python

#================================================================
#mass import with exception handling
try:
    import sys, random, math, os, getopt, pygame
    from socket import *
    from pygame.locals import *
    from Chips_01 import Chip

except ImportError as err:
    print("\nCould not load {}".format(err))
    sys.exit(2)
#================================================================

#================================================================
def main():    
    # initialise screen
    pygame.init()
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Game engine")

    #Fill background
    background = pygame.Surface(screen.get_size()).convert()
    background.fill((250, 250, 250))

    #Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Game engine", 1, (200, 10, 10))
    text_position = text.get_rect()
    text_position.centerx = background.get_rect().centerx
    #background.blit(text, text_position)

#--------------------------------------------------------------
#Game Loop:
    #chip_1 = Chip(275, 50, 50, 50, screen, 'chip.png')
    chip_2 = Chip(200, 0, 50, 50, screen, 'chip.png')
    chip_3 = Chip(275, 150, 50, 50, screen, 'chip.png')

    while True:
        background.blit(text, text_position)
        screen.blit(background, (0, 0))

        pygame.time.delay(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        chip_3.gravity(0.1, 550)
        chip_2.gravity(2, 550)
        chip_2.momentum(0.1)
        #chip_1.gravity(0.1, 600)
        #print('chip_2.y:',chip_2.y )
        #chip_1.update()
        chip_2.collisions()
        chip_3.collisions()
        #print(chip_2.collision(chip_3))
        #print('World before: ', chip_2.World)
        chip_2.connection_line(chip_3)
        chip_3.update()
        chip_2.update()
        #print('World After: ',chip_2.World)

        #chip.gravity(5, 400)
        #chip.update()
        pygame.display.flip()
        #pygame.display.update()
#--------------------------------------------------------------

#================================================================

if __name__ == '__main__':
    main()
