#!/usr/bin/env python
import pygame
import os

pygame.mixer.init()

def load_images(directory):
   #--To load all images in image directory and store them in a dictionary--
   directory_images = {}

   for image in os.listdir(directory):
      try:
         directory_images[image.split('.')[0]] = pygame.image.load('{}/{}'.format(directory, image))
      except:
         pass

   return directory_images
      #--the name of the file(without the file extension) return to the loaded image itself e.g all_images[name] will return the loaded image of name.png--

def load_sounds(directory):
   #--To load all images in image directory and store them in a dictionary--
   directory_sounds = {}

   for sound in os.listdir(directory):
      try:
         directory_sounds[sound.split('.')[0]] = pygame.mixer.Sound('{}/{}'.format(directory, sound))
      except:
         pass

   return directory_sounds

def play_sound(file_name, dictionary, channel=0):
   pygame.mixer.Channel(channel).play(dictionary[file_name])

