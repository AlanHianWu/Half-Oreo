#!/usr/bin/env python

import pygame

class Board_piece(object):
   def __init__(self, image, x=0, y=0):
      self.image = image
      self.x = x
      self.y = y

   def make_board(self, insert_text):
      #--multiplis the board piece accordingly--
      for x in range(0, 560, 80):
         for y in range(0, 480, 80):
            win.blit(im, (self.x + x, self.y + y))

      #--box at the bottom pf the screen--
      win.blit(pygame.transform.scale(pygame.image.load('player.png'), (560, 40)), (0, 560))

      #--The text in the box--
      font = pygame.font.Font(None, 36)
      text = font.render(insert_text, 1, (255, 0, 0))
      text_position = text.get_rect()
      win.blit(text, (225, 570))

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

pygame.init()

win = pygame.display.set_mode((560, 600))

font = pygame.font.Font(None, 36)
text = font.render("Connect 4", 1, (255, 0, 10))
text_position = text.get_rect()

#--The board--
im = pygame.transform.scale(pygame.image.load('block.png'), (80, 80))
board = Board_piece(im, 0, 80)
#--Every square which makes up the board is 80 x 80 units--

#--The velocity of the chip--
chip = Chip(50, 50, 25, 1)
#-------

game_on = True

while game_on:
   win.fill((0, 0, 0))
   pygame.time.delay(40)

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         game_on = False

   #--Everythime the loop comes around,the circle is placed then the board is put on top--
   chip.move()
   board.make_board("insert_text")
   chip.gravity(330)
   pygame.display.update()

#--the chip isn't too important. But I want to show that the circle can pass underneath the board--