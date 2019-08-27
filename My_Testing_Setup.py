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
    chip = Chip(50, 50, 50, 50, screen, 'chip.png')
    chip_2 = Chip(275, 100, 50, 50, screen, 'chip.png')
    chip_3 = Chip(400, 150, 50, 50, screen, 'chip.png')

    while True:
        background.blit(text, text_position)
        screen.blit(background, (0, 0))

        pygame.time.delay(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        chip_3.gravity(9.81, 500)
        chip_3.update()
        chip_2.gravity(0.5, 600)
        chip_2.update()
        chip.gravity(5, 400)
        chip.update()
        pygame.display.flip()
        #pygame.display.update()
#--------------------------------------------------------------

#================================================================

if __name__ == '__main__':
    main()
