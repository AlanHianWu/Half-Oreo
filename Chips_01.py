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

    World = []

    def __init__(self, x, y, height, width, screen, image):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.times = 1
        self.location = ()
        self.centre = x, y
        self.y_limit = ()
        self.x_limit = ()

    #acc the accration due to gravity, floor is where it will stop.
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

    #New collison dectection, only based off of rectanagles and squares for now
    def collisions(self):
        #retangle or square
        #(top_left, top_right, bottom_right, bottom_left)
        top_left = (self.x - (self.width / 2)), (self.y - (self.height / 2))
        top_right = (self.x + (self.width / 2)), (self.y - (self.height / 2))
        bottom_left = (self.x - (self.width / 2)), (self.y + (self.height / 2))
        bottom_right = (self.x + (self.width / 2)), (self.y + (self.height / 2))
        self.location = (top_left, top_right, bottom_right, bottom_left)
        Chip.World.append(self.location)
        self.y_limit = top_left[1], bottom_right[1]
        self.x_limit = bottom_left[0], top_right[0]
        #print('my_conner_points: {}\nmy coordinates: {},{}'.format(self.location, self.x, self.y))

    def connection_line(self, other):
        m = (other.y - self.y) / (other.x - self.x)
        print('DRAW: DRAW')
        for x in range(self.x, other.x):
            y = ((m * x) - (m * self.x)) + self.y
            if (self.x_limit[0] <= x and x <= self.x_limit[1]) and (self.y_limit[0] <= y and y <= self.y_limit[1]):
                print('mymymy: ', (x, y))
            elif (other.x_limit[0] <= x and x <= other.x_limit[1]) and (other.y_limit[0] <= y and y <= other.y_limit[1]):
                print('ititit: ', (x, y))
            else:
                print('void_void: ', (x, y))


    #update the new location and blit it on screen
    def update(self):
        Chip.World.remove(self.location)
        return self.screen.blit(pygame.transform.scale(self.image, (self.width, self.height)), (self.x, self.y))

#================================================================
