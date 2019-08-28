#!/usr/bin/env python

#================================================================
#mass import with exception handling
try:
    import sys, pygame

except ImportError as err:
    print("\nCould not load {}".format(err))
    sys.exit(2)


#Connect Chip; still working on it
#================================================================
class Chip(object):


    def __init__(self, x, y, height, width, screen, image):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.times = 1
        self.rect = self.image.get_rect()

    #acc the accration due to gravity
    #floor is where it will stop
    def gravity(self, acc, floor):
        if self.y < floor - (self.height) + (self.height / 10):
            self.y = self.y + acc * self.times
            self.times = self.times + 1

        else:
            self.y = floor - (self.height) + (self.height / 10)

    #Collision dectection
    def collision(self, other):
        my_size = (self.y - (self.height / 2), self.y + (self.height / 2))
        other_size = (other.y - (other.height / 2), other.y + (other.height / 2))
        #print('my size   :{}\nother size:{}'.format(my_size, other_size))
        if (my_size[0] <= other_size[0] and other_size[0] <= my_size[1]) or (my_size[0] <= other_size[1] and other_size[0] <= my_size[0]):
            #print('Collide !!!')
            return True
        else:
            return False


    #update the new location and blit it on screen
    def update(self):
        return self.screen.blit(pygame.transform.scale(self.image, (self.width, self.height)), (self.x, self.y))

#================================================================
