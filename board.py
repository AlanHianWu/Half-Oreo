#!/usr/bin/env python

import pygame

class Board_piece(object):
   def __init__(self, image, x=0, y=0):
      self.image = image
      self.x = x
      self.y = y

   def make_board(self):
      #--multiplis the board piece accordingly--
      for i in range(0, 560, 80):
         for k in range(0, 480, 80):
            win.blit(im, (self.x + i, self.y + k))

#-----------------------------------------------------------------

class Chip(object):
   def __init__(self, x, y, width, vel):
      self.x = x
      self.y = y
      self.width = width
      self.vel = vel

   def gravity(self, limit):
      if chip.y <= limit:
         chip.y += chip.vel
         chip.vel += 1

   def  move(self):
      return pygame.draw.circle(win, (255, 0, 0), (self.x, self.y), (25))

#---------------------------------------------------------------------------------

win = pygame.display.set_mode((560, 600))

#--The board--
im = pygame.transform.scale(pygame.image.load('block.png'), (80, 80))
board = Board_piece(im, 0, 80)
#--For now I've only got a png 'block' with a transparent circle in the middle. The circle and block measurments are not exact, but later we'll get exact measurments--


game_on = True

#--The velocity of the chip--
chip = Chip(50, 50, 25, 1)
#-------

while game_on:
   win.fill((0, 0, 0))
   pygame.time.delay(40)

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         game_on = False

   #--Everythime the loop comes around,the circle is placed and the transparent image is put on top--
   chip.move()
   board.make_board()
   chip.gravity(330)

   pygame.display.update()

#--the chip isn't too important. But I want to show that the circle can pass underneath the board--