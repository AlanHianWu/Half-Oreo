#!/usr/bin/env python
import pygame

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
   def draw_chips(cls, screen):
      for chip in cls.all_chips.values():
         pygame.draw.circle(screen, chip.colour, (chip.x + 40, chip.y), chip.width)