#!/usr/bin/env python
import pygame
import threading
import time
import winsound
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (300,50)

#--To load all images in image directory and store them in a dictionary--
all_images = {}

for image in os.listdir('images'):
   all_images[image.split('.')[0]] = pygame.image.load('images/{}'.format(image))
   #--the name of the file(without the file type) return to the loaded image itself--
#------------------------

pygame.font.init()

font_1 = pygame.font.SysFont('Comic Sans MS', 40)

window = pygame.display.set_mode((560, 600))

game = True


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
            return None
      fade.set_alpha(i)
      if array is None:
         pass
      else:
         redraw(array)
      main_window.blit(fade, (0, 0))
      pygame.display.update()
      pygame.time.delay(5)
      i -= 1


def fade_out(fade_colour, main_window, width, height, speed, array=None):
   fade = pygame.Surface((560, 600))
   fade.fill(fade_colour)
   #--function is to fade out the screen, the 'array' local variable refers to everything that is on the screen, see redraw func for more info--
   for alpha in range(0, 255):
      for event in pygame.event.get():
         if event.type == pygame.MOUSEBUTTONDOWN:
            return None
      fade.set_alpha(alpha)
      if array is None:
         pass
      else:
         redraw(array)
      main_window.blit(fade, (0, 0))
      pygame.display.update()
      pygame.time.delay(5)

cutscene = 0

while game:
   pygame.time.delay(15)
   window.fill((0, 0, 0))
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         game = False
   if cutscene < 1:
      fade_in((0, 0, 0), window, 560, 600, 8, [('text', (font_1, 'POWERED', window, (255, 255, 255), (200, 200))), 
                                               ('text', (font_1, 'BY', window, (255, 255, 255), (250, 260))),
                                               ('text', (font_1, 'PYGAME', window, (255, 255, 255), (205, 320)))])

      fade_out((0, 0, 0), window, 560, 600, 5, [('text', (font_1, 'POWERED', window, (255, 255, 255), (200, 200))), 
                                               ('text', (font_1, 'BY', window, (255, 255, 255), (250, 260))),
                                               ('text', (font_1, 'PYGAME', window, (255, 255, 255), (205, 320)))])
      cutscene = 1

   if cutscene < 2:
      fade_in((0, 0, 0), window, 560, 600, 3, [('image', (all_images['half_oreo'], window, (100, 100), (310, 300))),
                                               ('text', (font_1, 'Production', window, (255, 255, 255), (180, 400)))])

      fade_out((0, 0, 0), window, 560, 600, 5, [('image', (all_images['half_oreo'], window, (100, 100), (310, 300))),
                                                ('text', (font_1, 'Production', window, (255, 255, 255), (180, 400)))])
      cutscene = 2

   if cutscene < 3:
      cutscene = 3

   #--the three 'if' statements above are the cutscenes, they're not yet done though, after this the menu should show up

   pygame.display.update()
