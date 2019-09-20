#!/usr/bin/env python
import pygame
from sprite import *
from misc_function import *

class Menu_button(object):
   all_sounds = load_sounds('audio/fx')
   def __init__(self, sprite, interact, audio_hover=None, audio_select=None):
      self.sprite = sprite
      self.mouse_pos = pygame.mouse.get_pos()
      self.interact = interact
      self.audio_hover = audio_hover
      self.audio_select = audio_select
      self.flag = False

   def is_clicked(self, event):
      #--check if self is clicked on--
      if self.sprite.collision(self.mouse_pos[0], self.mouse_pos[1]) == True and event.type == self.interact:
         if self.audio_select != None:
            play_sound(self.audio_select, Menu_button.all_sounds, 0)
         return True
      else:
         return False

   def is_hover_over(self):
      #--check is mouse is hovering over self--
      if self.sprite.collision(self.mouse_pos[0], self.mouse_pos[1]) and self.flag == False:
         self.flag = True
         if self.audio_hover != None:
            play_sound(self.audio_hover, Menu_button.all_sounds, 0)
      else:
         pass

      if self.sprite.collision(self.mouse_pos[0], self.mouse_pos[1]) == False:
         self.flag = False


   def redraw(self, screen):
      #--updates the menu button
      self.sprite.cycle()
      self.is_hover_over()
      self.mouse_pos = pygame.mouse.get_pos()
      if self.sprite.collision(self.mouse_pos[0], self.mouse_pos[1]) == True:
         self.sprite.display_animation(screen, 'flicker')
      else:
         self.sprite.display_animation(screen, 'idle')