#!/usr/bin/env python
import pygame
from Misc_function import *
from sprite import *

pygame.init()
pygame.font.init()
pygame.mixer.init()

pygame.mixer.set_num_channels(8)

def move(character, keys, direction):
   if keys[pygame.K_RIGHT]:
      direction = True
      character.x += 4
      return direction
   elif keys[pygame.K_LEFT]:
      direction = False
      character.x -= 4
      return direction

   else:
      return direction

def display_character(character, keys, screen, direction):
   if keys[pygame.K_RIGHT]:
      character.display_animation(screen, 'right')
   elif keys[pygame.K_LEFT]:
      character.display_animation(screen, 'left')
   else:
      if direction == True:
         character.display_animation(screen, 'idle_{}'.format('right'))   
      if direction == False:
         character.display_animation(screen, 'idle_{}'.format('left'))  

select = pygame.mixer.Sound('audio/select.wav')

song = pygame.mixer.music.load('audio/Devils_pit.mp3')

all_images = load_images('images')

all_sounds = load_sounds('audio')


megaman_right = [all_images['2'], all_images['1'], all_images['2'], all_images['3']]
megaman_left = [pygame.transform.flip(all_images['2'], True, False), pygame.transform.flip(all_images['1'], True, False), pygame.transform.flip(all_images['2'], True, False), pygame.transform.flip(all_images['3'], True, False)]
megaman_idle_right = [all_images['0']]
megaman_idle_left = [pygame.transform.flip(all_images['0'], True, False)]

megaman = Sprite_object_basic('megaman', 300, 300, 80, 80, [('right', megaman_right),
                                                              ('left', megaman_left),
                                                              ('idle_right', megaman_idle_right),
                                                              ('idle_left', megaman_idle_left)], 30)

screen = pygame.display.set_mode((560, 600))

game_on = True

pygame.mixer.music.play()

megaman_direction = True

while game_on:
   screen.fill((200, 255, 255))
   for e in pygame.event.get():
      if e.type == pygame.QUIT:
         game_on = False

   k = pygame.key.get_pressed()
   megaman_direction = move(megaman, k, megaman_direction)
   megaman.cycle()
   display_character(megaman, k, screen, megaman_direction)

   pygame.time.delay(20)
   pygame.display.update()
