#!/usr/bin/env python

#================================================================
#mass import with exception handling
try:
    import sys, random, math, os, getopt, pygame
    from socket import *
    from pygame.locals import *

except ImportError as err:
    print("\nCould not load {}".format(err))
    sys.exit(2)
#================================================================

#Load image and return image as object
#================================================================
def load_png(name):
    fullname = os.path.join(name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert()
    except pygame.error as message:
        print('\nCould not load image: {}'.format(message))
        raise SystemExit(message)
    return image, image.get_rect()
#================================================================

#Connect Chip; still working on it
#================================================================
class Chip(pygame.sprite.Sprite):

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('chip.png')
        screen = pygame.display.get_surface()
        self.vector = vector

    def update(self):
        newpos = self.calcnewpos(self.rect, self.vector)
        self.rect = newpos

    def calcnewpos(self, rect, vector):
        (angle, z) = vector
        (dx, dy) = (z * math.cos(angle), z * math.sin(angle))
        return rect.move(dx, dy)

#================================================================
