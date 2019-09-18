#!/usr/bin/env python
import threading
import pygame
import os

class Sprite_object_basic(object):
   #--This class is used to make sprite objects with multiple sets of sprites--
   #--for the purpose of connect 4 it will be used for the menu buttons--

   def __init__(self, ID, x, y, witdh, height, active_frames, frame_speed=1, current_frame=0):
      self.ID = ID
      self.x = x
      self.y = y
      self.witdh = witdh
      self.height = height
      self.all_frames = {}
      #--make sure the active frames are in the order you want in a list--
      #--active_frames should contain a list of tuples. In each tuple, tuple[0] is the name of the set of animation and tuple[1] are the images themselves--
      self.active_frames = active_frames
      for frames in self.active_frames:
         self.all_frames[frames[0]] = frames[1]
      self.frame_speed = frame_speed
      self.current_frame = current_frame
      self.current_animation = self.active_frames[0][0]
      self.flag = 0

   def display_animation(self, window, frame_name):
      #frame_name refers to the keys in the dictionary all_frames. So if frame_name is string 'walk_right', it should refer to all_frames['walk_right']
      if self.current_animation is frame_name:
         pass
      else:
         self.current_animation = frame_name
         self.current_frame = 0
      #--used to display images-
      frame = pygame.transform.scale(self.all_frames[frame_name][self.current_frame], (self.witdh, self.height))
      window.blit(frame, (self.x, self.y))

   def cycle(self):
      #used to cycle through the sprites
      frame_per_update = self.frame_speed // len(self.all_frames[self.current_animation]) #This is the amount of times a single frame will be played

      if self.flag > frame_per_update - 1:
         self.flag = 0
         self.current_frame += 1
      else:
         self.flag += 1

      if self.current_frame > len(self.all_frames[self.current_animation]) - 1:
         self.current_frame = 0

   def collision(self, display, obj_x, obj_y):
      #--this checks if anything is colliding with the sprite and returns True or False--
      if obj_x >= (self.x) and obj_x < (self.x + (self.witdh)) and obj_y >= (self.y) and obj_y < (self.y + (self.height)):
         return True
      else:
         return False

#---------------------------------------------------