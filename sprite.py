#!/usr/bin/env python
import threading
import pygame
import os

class Sprite_object_basic(object):
   #--This class is used to make sprite objects with multiple sets of animatios--
   #--for the purpose of connect 4 it will be used for the menu buttons--

   def __init__(self, ID, x, y, collision_width, collision_height, sprite_width, sprite_height, active_frames=None, frame_speed=1, current_frame=0):
      self.ID = ID
      self.x = x
      self.y = y
      self.collision_width = collision_width
      self.collision_height = collision_height
      self.sprite_width = sprite_width
      self.sprite_height = sprite_height
      #--make sure the active frames are in the order you want in a list--
      #--active_frames should contain a list of tuples. For each tuple, tuple[0] is the string name of the set of animations and tuple[1] are the images themselves--
      #--e.g active_frame = [('random_animation_1', [picture_1, picture_2, picture_3]), ('random_animation_2', [picture_4])]
      self.active_frames = active_frames
      if active_frames != None:
         self.all_frames = {}
         for frames in self.active_frames:
            self.all_frames[frames[0]] = frames[1]

         self.frame_speed = frame_speed
         self.current_frame = current_frame
         self.current_animation = self.active_frames[0][0]
         self.flag = 0

   def display_animation(self, window, frame_name):
      #--displays animations--
      #--frame_name refers to the keys in the dictionary all_frames. So if frame_name is string 'walk_right', it should refer to all_frames['walk_right']--
      if self.active_frames != None:
         if self.current_animation == frame_name:
            pass
         else:
            self.current_animation = frame_name
            self.current_frame = 0
         #--used to display images-
         frame = pygame.transform.scale(self.all_frames[frame_name][self.current_frame], (self.sprite_width, self.sprite_height))
         window.blit(frame, (self.x, self.y))
      else:
         print('you need "active_frames" to use display_animation()')

   def cycle(self):
      #used to cycle through the sprite's animations
      if self.active_frames != None:
         frame_per_update = self.frame_speed // len(self.all_frames[self.current_animation]) #This is the amount of times a single frame will be played per use of cycle()

         if self.flag > frame_per_update - 1:
            self.flag = 0
            self.current_frame += 1
         else:
            self.flag += 1

         if self.current_frame > len(self.all_frames[self.current_animation]) - 1:
            self.current_frame = 0
      else:
         print('you need "active_frames" to use cycle()')

   def collision(self, x, y):
      #--this checks if x and y is within the self and returns True or False--
      if x >= (self.x) and x <= (self.x + (self.collision_width)) and y >= (self.y) and y <= (self.y + (self.collision_height)):
         return True
      else:
         return False

   def collision_sprite(self, other):
      #--this checks if another sprite object is colliding with the self and returns True or False--
      if self.x >= other.x and self.x <= (other.x + other.collision_width) and self.y >= other.y and self.y <= (other.y + other.collision_height):
         return True
      elif self.x >= other.x and self.x <= (other.x + other.collision_width) and other.y >= self.y and other.y <= (self.y + self.collision_height):
         return True

      elif other.x >= self.x and other.x <= (self.x + self.collision_width) and other.y >= self.y and other.y <= (self.y + self.collision_height):
         return True
      elif other.x >= self.x and other.x <= (self.x + self.collision_width) and self.y >= other.y and self.y <= (other.y + other.collision_height):
         return True
      else:
         return False

#---------------------------------------------------