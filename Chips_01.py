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
#Load image convert to bitmap and return image as object
#================================================================
'''def load_png(name):
    fullname = os.path.join(name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert()
    except pygame.error as message:
        print('Could not load image: {}'.format(message))
        raise SystemExit(message)
    return image'''
#================================================================
#Connect Chip; still working on it
#================================================================
class Chip(object):

    def __init__(self, x, y, height, width, screen, image, size):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.size = size
        self.times = 1

    #acc the accration due to gravity
    #floor is where it will stop
    def gravity(self, acc, floor):

        print(self.y)
        if self.size[1] < self.y and self.y < floor - (self.height) + (self.height / 10):
            self.y = self.height
            acc = 0

        elif self.y < self.size[1] and self.y < floor - (self.height) + (self.height / 10):
            self.y = self.y + acc * self.times
            self.times = self.times + 1

        else:
            self.y = floor - (self.height) + (self.height / 10)

    #update the new location and blit it on screen
    def update(self):
        return self.screen.blit(pygame.transform.scale(self.image, (self.width, self.height)), (self.x, self.y))

#================================================================
