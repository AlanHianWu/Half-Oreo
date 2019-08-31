#!/usr/bin/env python

import pygame

class Board(object):
   def __init__(self, image, x=0, y=0):
      self.image = image
      self.x = x
      self.y = y

   def print_board(self, insert_text):

      #--multiplies the board piece accordingly--
      for x in range(0, 560, 80):
         for y in range(0, 480, 80):
            win.blit(im, (self.x + x, self.y + y))

      #--box at the bottom pf the screen--
      win.blit(pygame.transform.scale(pygame.image.load('player.png'), (560, 40)), (0, 560))

      #--The text in the box--
      font = pygame.font.Font(None, 36)
      text = font.render(insert_text, 1, (0, 0, 0))
      text_position = text.get_rect()
      win.blit(text, (225, 570))

#-----------------------------------------------------------------

class Chip(object):
   #--make sure you keep all the init variables(ID, owner, colour, is_falling), class variables, print_chips(), and the return values for gravity(). They'll be needed for the main loop-- 
   all_chips = {}
   def __init__(self, ID, owner, colour, x, y, width, vel, is_falling=False):
      self.ID = ID
      self.owner = owner
      self.colour = colour
      self.x = x
      self.y = y
      self.width = width
      self.vel = vel
      self.is_falling = is_falling
      Chip.all_chips[self.ID] = self

   def  move(self, mouse_pos):
      #--checking and adjusting chip's position--
      if mouse_pos < 80:
         self.x = 0
      if mouse_pos > 80 and mouse_pos < 160:
         self.x = 80
      if mouse_pos > 160 and mouse_pos < 240:
         self.x = 160
      if mouse_pos > 240 and mouse_pos < 320:
         self.x = 240
      if mouse_pos > 320 and mouse_pos < 400:
         self.x = 320
      if mouse_pos > 400 and mouse_pos < 480:
         self.x = 400
      if mouse_pos > 480 :
         self.x = 480

   def gravity(self, limit):
      #gravity changes chips y then return wether it's y has hit the limit
      if self.y < limit:
         self.y += self.vel
         self.vel += 1
         return 0
      else:
         self.y = limit
         return 1

   @classmethod
   def print_chips(cls):
      for chip in cls.all_chips.values():
         pygame.draw.circle(win, chip.colour, (chip.x + 40, chip.y), chip.width)


#---------------------------------------------------------------------------------


#----------------------------------------------------------------------------------

#--game start--

pygame.init()

win = pygame.display.set_mode((560, 600))

#--The board--
im = pygame.transform.scale(pygame.image.load('block.png'), (80, 80))
board = Board(im, 0, 80)
#^-Every square which makes up the board is 80 x 80 units-^

#--The first chip--
chip = Chip(0, 1, (255, 255, 0), 0, 40, 40, 1, False)
#-------

#--misc--
game_on = True
current_player = 1
i = 1
#-------

while game_on:
   win.fill((0, 0, 0))
   pygame.time.delay(30)

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         game_on = False

      #--to track the mouse position and see if mouse is clicked--
      mx, my = pygame.mouse.get_pos()

      if event.type == pygame.MOUSEBUTTONDOWN and chip.is_falling is False:
         chip.is_falling = True

   #--To check if a piece is falling and if so, check who the current player is then switch player if a piece has landed--
   if chip.is_falling is True:
      fall = chip.gravity(480 + 40)
      if fall is 1 and current_player is 1:
         chip = Chip(i, current_player + 1, (255, 0, 0), mx, 40, 40, 1, False)
         chip.move(mx)
         i += 1
         current_player = 2

      elif fall is 1 and current_player is 2:
         chip = Chip(i, current_player - 1, (255, 255, 0), mx, 40, 40, 1, False)
         chip.move(mx)
         i += 1
         current_player = 1

   else:
      chip.move(mx)

   Chip.print_chips()
   board.print_board("Player {} GO".format(current_player))

   pygame.display.update()

#--the chip isn't too important. But I want to show that the circle can pass underneath the board--