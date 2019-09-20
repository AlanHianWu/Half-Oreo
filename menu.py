#!/usr/bin/env python
import pygame
import threading
import time
import winsound
import os



def display_text(font, s, window, colour, co_ordinates):
   #--displays text on specified surface--
   text = font.render(s, False, colour) 
   return window.blit(text, co_ordinates)

def display_image(s, window, co_ordinates, width_height):
   #--displays image at specified surface--
   transform_im = pygame.transform.scale(s, (width_height))
   return window.blit(transform_im, co_ordinates)

def redraw(array):
   #--function is to redraw everything on the screen--
   #--in the array, there are tuple, the first element of that tuple defining what it is. And the second element of the tuple being passed to the function--
   #--e.g if tuple[0] == image, then display_image(tuple[1]) where tuple[1] has all the parameters for display_image()--
   for element in array:
      if element[0] is 'image':
         display_image(element[1][0], element[1][1], element[1][2], element[1][3])
      elif element[0] is 'text':
         display_text(element[1][0], element[1][1], element[1][2], element[1][3], element[1][4])
      else:
         pass

def fade_in(fade_colour, main_window, width, height, speed, array=None):
   fade = pygame.Surface((560, 600))
   fade.fill(fade_colour)
   #--function is to fade in the screen, the 'array' local variable refers to everything that is on the screen, see redraw func for more info--
   i = 255
   while i >= 0:
      for event in pygame.event.get():
         if event.type == pygame.MOUSEBUTTONDOWN:
            return 1
      fade.set_alpha(i)
      if array is None:
         pass
      else:
         redraw(array)
      main_window.blit(fade, (0, 0))
      pygame.display.update()
      pygame.time.delay(speed)
      i -= 1
   return 0


def fade_out(fade_colour, main_window, width, height, speed, array=None):
   fade = pygame.Surface((560, 600))
   fade.fill(fade_colour)
   #--function is to fade out the screen, the 'array' local variable refers to everything that is on the screen, see redraw func for more info--
   for alpha in range(0, 255):
      for event in pygame.event.get():
         if event.type == pygame.MOUSEBUTTONDOWN:
            return 1
      fade.set_alpha(alpha)
      if array is None:
         pass
      else:
         redraw(array)
      main_window.blit(fade, (0, 0))
      pygame.display.update()
      pygame.time.delay(speed)
   return 0
