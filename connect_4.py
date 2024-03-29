#!/usr/bin/env python
import pygame
import os
from misc_function import *
from Chip import *
from Board import *
from menu import *
from sprite import *
from music_player import *
from menu_button import *

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (300,50)

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()

#--images--
all_images = load_images('images')
#----------

#--sounds--
all_sounds = load_sounds('audio/fx')
#----------

##--Menu buttons--
local_sprite = Sprite_object_basic('local', 130, 300, 300, 80, 300, 80, [('flicker', [all_images['Menu_button_2'], all_images['Menu_button_1']]),
                                                                ('idle', [all_images['Menu_button_1']])], 20)

local_button = Menu_button(local_sprite, pygame.MOUSEBUTTONDOWN, 'beep', 'select')

multiplayer_sprite = Sprite_object_basic('local', 130, 400, 300, 80, 300, 80, [('flicker', [all_images['Menu_button_2'], all_images['Menu_button_1']]),
                                                                      ('idle', [all_images['Menu_button_1']])], 20)

multiplayer_button = Menu_button(multiplayer_sprite, pygame.MOUSEBUTTONDOWN, 'beep', 'select')
#----------

#--music--
intro_songs = Song_player('intro_songs', ['audio/intro_part_1.mp3', 'audio/intro_part_2.mp3'], 0.6)
game_music = Song_player('game_music', ['audio/Summer loverr.mp3', 'audio/Rebound.mp3', 'audio/Walkin home.mp3', 'audio/Every day.mp3'], 0.6)
#--------

#--fonts--
font_1 = pygame.font.SysFont(None, 50)
#--------

#--misc--
screen = pygame.display.set_mode((560, 600))

game_on = True

menu = True

cutscene = 0
#------------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------- INTRO SEQUENCE ----------------------------------------------------------
intro_songs.play_song('audio/intro_part_1.mp3', -1)

flag = False
while cutscene < 3 and menu == True:
   pygame.time.delay(15)
   screen.fill((0, 0, 0))

   if cutscene < 1:
      fade_in((0, 0, 0), screen, 560, 600, 150, [('text', (font_1, 'POWERED', screen, (255, 255, 255), (200, 200))), 
                                               ('text', (font_1, 'BY', screen, (255, 255, 255), (250, 260))),
                                               ('text', (font_1, 'PYGAME', screen, (255, 255, 255), (205, 320)))])

      fade_out((0, 0, 0), screen, 560, 600, 130, [('text', (font_1, 'POWERED', screen, (255, 255, 255), (200, 200))), 
                                                ('text', (font_1, 'BY', screen, (255, 255, 255), (250, 260))),
                                                ('text', (font_1, 'PYGAME', screen, (255, 255, 255), (205, 320)))])
      cutscene = 1

   if cutscene < 2:
      fade_in((0, 0, 0), screen, 560, 600, 110, [('image', (all_images['half_oreo'], screen, (110, 60), (330, 350))),
                                               ('text', (font_1, 'Production', screen, (255, 255, 255), (190, 400)))])

      fade_out((0, 0, 0), screen, 560, 600, 150, [('image', (all_images['half_oreo'], screen, (110, 60), (330, 350))),
                                                ('text', (font_1, 'Production', screen, (255, 255, 255), (190, 400)))])
      cutscene = 2

   if cutscene < 3:
      fade_out((255, 255, 255), screen, 560, 600, 120)
      break


#--Did The play skip any fade ins?--

intro_songs.play_song('audio/intro_part_2.mp3', -1)
#-------------------------------------------------------------------

#-------------------------------------------------------------------

#---------------------------------------------------------------------- Menu ----------------------------------------------------------

while game_on == True and menu == True:
   screen.fill((0, 0, 0))
   local_button.redraw(screen)
   multiplayer_button.redraw(screen)

   redraw([('text', [font_1, 'Local', screen, (0, 0, 0), (230, 325)]),
           ('text', [font_1, 'Multiplayer', screen, (0, 0, 0), (180, 425)]),
           ('image', [all_images['connect_4'], screen, (30, 30), (480, 190)])])

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         game_on = False
      if local_button.is_clicked(event):
         intro_songs.stop()
         fade_out((255, 255, 255), screen, 560, 600, 110)
         menu = False
      multiplayer_button.is_clicked(event)

   clock.tick(140)
   pygame.display.update()

#--------------------------------------------------------

#--------------------------------------------------------

#---------------------------------------------------------------------- Main game ----------------------------------------------------------

#--The board--
im = pygame.transform.scale(pygame.image.load('images/block.png'), (80, 80))
board = Board(im, 0, 80)
#^-Every square which makes up the board is 80 x 80 units-^

#--ground
floor = Sprite_object_basic('floor', 0, 560, 560, 40, 560, 40)
#--------

#--The first chip--
chip = Chip(0, 1, (255, 255, 0), 0, 0, 80, 80, 1, all_images['chip_red'], False)
#-------

#--Music--
game_music = Song_player('game_music', ['audio/Summer loverr.mp3', 'audio/Rebound.mp3', 'audio/Walkin home.mp3', 'audio/Every day.mp3'], 0.6)
#--------

#--misc--
current_player = 1
i = 1
#-------

while game_on:
   screen.fill((0, 0, 0))
   pygame.time.delay(20)

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         game_on = False

      if event.type == pygame.MOUSEBUTTONDOWN and chip.is_falling is False:
         chip.is_falling = True

   mx, my = pygame.mouse.get_pos()

   #--To check if a piece is falling and if so, check who the current player is then switch player if a piece has landed--
   if chip.is_falling is True:
      fall = chip.gravity(floor)
      if fall is 1 and current_player is 1:
         chip = Chip(i, current_player + 1, (255, 0, 0), mx, 0, 80, 80, 1, image=all_images['chip_yellow'], is_falling=False)
         chip.move(mx)
         i += 1
         current_player = 2

      elif fall is 1 and current_player is 2:
         chip = Chip(i, current_player - 1, (255, 255, 0), mx, 0, 80, 80, 1, image=all_images['chip_red'], is_falling=False)
         chip.move(mx)
         i += 1
         current_player = 1

   else:
      chip.move(mx)

   Chip.draw_chips(screen)
   board.draw_board(screen, "Player {} GO".format(current_player))
   game_music.play_list(20, 5)

   pygame.display.update()

#--the chip isn't too important. But I want to show that the circle can pass underneath the board--
quit()