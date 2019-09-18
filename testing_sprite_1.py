#!usr/bin/env python
import os
import pygame
from Misc_function import *
from sprite import *

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (300,50)

#--To load all images in image directory--
all_images = load_images('images')
#----------------


def main():
   clock = pygame.time.Clock()
   game = True
   pygame.init()
   screen = pygame.display.set_mode((560, 600))
   #                         ID   x,  y,  width, height,  active_frames,                                                                                          frame_speed
   ex = Sprite_object_basic('ex', 150, 200, 300, 100, [('flicker', [all_images['Menu_button_2'], all_images['Menu_button_1']]), ('idle', [all_images['Menu_button_1']])], 5)
   ex_2 = Sprite_object_basic('ex_2', 150, 400, 300, 100, [('flicker', [all_images['Menu_button_2'], all_images['Menu_button_1']]), ('idle', [all_images['Menu_button_1']])], 30)

   i = 0
   while game:
      screen.fill((0, 0, 0))
      for e in pygame.event.get():
         if e.type == pygame.QUIT:
            game = False
      keys = pygame.key.get_pressed()
      mouse_x, mouse_y = pygame.mouse.get_pos()
      ex.cycle()
      ex_2.cycle()

      if ex.collision(screen, mouse_x, mouse_y) == True:
         ex.display_animation(screen, 'flicker')
      else:
         ex.display_animation(screen, 'idle')

      if ex_2.collision(screen, mouse_x, mouse_y) == True:
         ex_2.display_animation(screen, 'flicker')
      else:
         ex_2.display_animation(screen, 'idle')

      pygame.time.delay(30)
      pygame.display.update()

if __name__ == '__main__':
   main()
quit()
