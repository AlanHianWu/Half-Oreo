#!/usr/bin/env python
import pygame
import os
from Chip import *
from Board import *
from menu import *
from sprite import *

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (300,50)

def load_images():
   #--To load all images in image directory and store them in a dictionary--
   all_images = {}

   for image in os.listdir('images'):
      try:
         all_images[image.split('.')[0]] = pygame.image.load('images/{}'.format(image))
      except:
         pass

   return all_images
      #--the name of the file(without the file extension) return to the loaded image itself e.g all_images[name] will return the loaded image of name.png--

pygame.init()
pygame.font.init()

#--images--
all_images = load_images()
#----------

##--Menu buttons--
#                                  x,  y,  width, height, idle_frame,                active_frames,                                          frame_rate
local_button = Sprite_object_basic(130, 300, 300, 80, all_images['Menu_button_1'], [all_images['Menu_button_2'], all_images['Menu_button_1']], 10)
Multiplayer_button = Sprite_object_basic(130, 400, 300, 80, all_images['Menu_button_1'], [all_images['Menu_button_2'], all_images['Menu_button_1']], 10)
#----------

#--misc--
font_1 = pygame.font.SysFont(None, 50)

screen = pygame.display.set_mode((560, 600))

game_on = True

menu = True

cutscene = 0
#------------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------- INTRO SEQUENCE ----------------------------------------------------------
while cutscene < 3 and menu == True:
   pygame.time.delay(15)
   screen.fill((0, 0, 0))
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         game_on = False
   if cutscene < 1:
      fade_in((0, 0, 0), screen, 560, 600, 8, [('text', (font_1, 'POWERED', screen, (255, 255, 255), (200, 200))), 
                                               ('text', (font_1, 'BY', screen, (255, 255, 255), (250, 260))),
                                               ('text', (font_1, 'PYGAME', screen, (255, 255, 255), (205, 320)))])

      fade_out((0, 0, 0), screen, 560, 600, 5, [('text', (font_1, 'POWERED', screen, (255, 255, 255), (200, 200))), 
                                               ('text', (font_1, 'BY', screen, (255, 255, 255), (250, 260))),
                                               ('text', (font_1, 'PYGAME', screen, (255, 255, 255), (205, 320)))])
      cutscene = 1

   if cutscene < 2:
      fade_in((0, 0, 0), screen, 560, 600, 3, [('image', (all_images['half_oreo'], screen, (100, 100), (310, 300))),
                                               ('text', (font_1, 'Production', screen, (255, 255, 255), (170, 400)))])

      fade_out((0, 0, 0), screen, 560, 600, 5, [('image', (all_images['half_oreo'], screen, (100, 100), (310, 300))),
                                                ('text', (font_1, 'Production', screen, (255, 255, 255), (170, 400)))])
      cutscene = 2

   if cutscene < 3:
      break
      cutscene = 3

   #--the three 'if' statements above are the cutscenes, they're not yet done though, after this the menu should show up
   pygame.display.update()
#-------------------------------------------------------------------

#-------------------------------------------------------------------

#---------------------------------------------------------------------- Menu ----------------------------------------------------------
while game_on == True and menu == True:
   screen.fill((0, 0, 0))
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         game_on = False
      if event.type == pygame.MOUSEBUTTONDOWN and local_button.start_cycle == True:
         menu = False

   keys = pygame.key.get_pressed()
   mouse_x, mouse_y = pygame.mouse.get_pos()
   local_button.cycle()
   Multiplayer_button.cycle()

   if local_button.collision(screen, mouse_x, mouse_y) == True:
      local_button.display_animation(screen)
   else:
      local_button.display_idle(screen)

   if Multiplayer_button.collision(screen, mouse_x, mouse_y) == True:
      Multiplayer_button.display_animation(screen)
   else:
      Multiplayer_button.display_idle(screen)

   redraw([('text', [font_1, 'Local', screen, (0, 0, 0), (230, 325)]),
           ('text', [font_1, 'Multiplayer', screen, (0, 0, 0), (180, 425)])])
   pygame.time.delay(30)
   pygame.display.update()

#--------------------------------------------------------

#--------------------------------------------------------

#---------------------------------------------------------------------- Main game ----------------------------------------------------------

#--The board--
im = pygame.transform.scale(pygame.image.load('images/block.png'), (80, 80))
board = Board(im, 0, 80)
#^-Every square which makes up the board is 80 x 80 units-^

#--The first chip--
chip = Chip(0, 1, (255, 255, 0), 0, 40, 40, 1, False)
#-------

#--misc--
current_player = 1
i = 1
#-------

while game_on:
   screen.fill((0, 0, 0))
   pygame.time.delay(30)

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         game_on = False

      if event.type == pygame.MOUSEBUTTONDOWN and chip.is_falling is False:
         chip.is_falling = True

   mx, my = pygame.mouse.get_pos()

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

   Chip.draw_chips(screen)
   board.draw_board(screen, "Player {} GO".format(current_player))

   pygame.display.update()

#--the chip isn't too important. But I want to show that the circle can pass underneath the board--
quit()