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

    '''This World class varible keeps tracks of the location 
       of all instances of a chip by keeping four points of the 
       conners of the hit box, the order is from top left then
       clockrise until bottom left, each time the update method is
       excuted the World gets refreshed, SO FAR NOT IN USE.'''
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

    #plan to use this to generate momentum for the chips
    def momentum(self, vector):
        self.x = self.x + vector

    #Collision dectection, a very basic collision dectection method
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

    #A range function but for float numbers, since the built in range does not work with float numbers
    @staticmethod
    def float_range(start, finish, steps=None):
        i = start
        if steps is None:
            steps = 1
        while i < finish:
            yield i
            i += steps

    #Uses the straight line equation to generate a line from the centre point of this chip to another so far limited to just comparing two chips at a time
    def connection_line(self, other):
        try:
            m = (other.y - self.y) / (other.x - self.x)
            print('\nDRAWING Line From This Box To Next Box Now\n')
            print(self.x, self.y, other.x, other.y)
            if other.x < self.x:
                for x in Chip.float_range(other.x, self.x):
                    y = ((m * x) - (m * self.x)) + self.y
                    if (self.x_limit[0] <= x and x <= self.x_limit[1]) and (self.y_limit[0] <= y and y <= self.y_limit[1]):
                        print('Line Inside My Hit BOX: ', (x, y))
                    elif (other.x_limit[0] <= x and x <= other.x_limit[1]) and (other.y_limit[0] <= y and y <= other.y_limit[1]):
                        print('Line Inside Other Box : ', (x, y))
                    else:
                        print('Line In Void          : ', (x, y))
            else:
                for x in Chip.float_range(self.x, other.x):
                    y = ((m * x) - (m * self.x)) + self.y
                    if (self.x_limit[0] <= x and x <= self.x_limit[1]) and (self.y_limit[0] <= y and y <= self.y_limit[1]):
                        print('Line Inside My Hit BOX: ', (x, y))
                    elif (other.x_limit[0] <= x and x <= other.x_limit[1]) and (other.y_limit[0] <= y and y <= other.y_limit[1]):
                        print('Line Inside Other Box : ', (x, y))
                    else:
                        print('Line In Void          : ', (x, y))
        except ZeroDivisionError:
            print('y=',self.y)


    #update the new location and blit it on screen
    def update(self):
        Chip.World.remove(self.location)
        return self.screen.blit(pygame.transform.scale(self.image, (self.width, self.height)), (self.x, self.y))

#================================================================
