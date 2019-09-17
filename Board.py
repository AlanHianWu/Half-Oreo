#!/usr/bin/env python
import pygame

class Board(object):
   def __init__(self, image, x=0, y=0):
      self.image = image
      self.x = x
      self.y = y

   def draw_board(self, screen, insert_text):

      #--multiplies the board piece accordingly--
      for x in range(0, 560, 80):
         for y in range(0, 480, 80):
            screen.blit(self.image, (self.x + x, self.y + y))

      #--box at the bottom pf the screen--
      screen.blit(pygame.transform.scale(pygame.image.load('images/player.png'), (560, 40)), (0, 560))

      #--The text in the box--
      font = pygame.font.Font(None, 36)
      text = font.render(insert_text, 1, (0, 0, 0))
      text_position = text.get_rect()
      screen.blit(text, (225, 570))
#-----------------------------------------------------------------
