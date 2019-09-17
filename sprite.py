#!/usr/bin/env python
import threading
import pygame
import os

class Sprite_object_basic(object):
   #--This class is used to make sprite objects(primarily for objects with one set of sprites)--
   #--for the purpose of connect 4 it will be used for the menu buttons--

   def __init__(self, x, y, witdh, height, idle_frame, active_frames, frame_speed, start_cycle=False, current_frame=0, is_alive=True):
      self.x = x
      self.y = y
      self.witdh = witdh
      self.height = height
      self.idle_frame = idle_frame
      #--make sure the active frames are in the order you want in a list
      self.active_frames = active_frames
      self.frame_speed = frame_speed
      self.start_cycle = start_cycle
      self.current_frame = current_frame
      self.flag = 0

   def display_animation(self, window, image=None):
      #--used to display images--
      frame = pygame.transform.scale(self.active_frames[self.current_frame], (self.witdh, self.height))
      window.blit(frame, (self.x, self.y))

   def display_idle(self, window):
      #--used for dsplaying idle animation--
      frame = pygame.transform.scale(self.idle_frame, (self.witdh, self.height))
      window.blit(frame, (self.x, self.y))

   def cycle(self):
      if self.start_cycle is True:
         frame_per_sec = self.frame_speed // len(self.active_frames)

         if self.flag > frame_per_sec - 1:
            self.flag = 0
            self.current_frame += 1
         else:
            self.flag += 1

         if self.current_frame > len(self.active_frames) - 1:
            self.current_frame = 0
      else:
         self.flag = 0
         self.current_frame = 0

   def collision(self, display, obj_x, obj_y):
      #--this checks if anything is colliding with the sprite and returns True or False--
      if obj_x >= (self.x) and obj_x < (self.x + (self.witdh)) and obj_y >= (self.y) and obj_y < (self.y + (self.height)):
         if self.start_cycle != True:
            self.start_cycle = True
         return True
      else:
         self.start_cycle = False
         return False

#---------------------------------------------------