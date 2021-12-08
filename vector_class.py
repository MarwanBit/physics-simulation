import pygame

import math


class Vector():
  '''
  Creates a vector class which has both visual information on the vector,
  and it also holds all of the position information needed...
  '''

  def __init__(self, coords, pos):
    '''
    generates a vector object taking the following arguments..

    inputs:
      coords (a tuple of 2d coordinates for our vector)
    '''
    
    self.sprite_image = pygame.image.load('vector.png')
    self.pos = pos
    self.rect = self.sprite_image.get_rect(center = self.pos)

    #inherits from the Vector class given by pymunk
    self.vector = (coords[0], coords[1])


  def get_angle(self):
    '''
    Returns the angle of the vector

    inputs:
      self the vector obj
    '''

    #aslong as the y component isn't zero we just do acos(x/y)
    if self.vector[0] != 0:
      return math.atan(self.vector[1]/self.vector[0]) * (180/math.pi)
    else:
      return 0


  def update_rect(self):
    '''
    Updates the rect after we do the rotation.......
    '''

    self.rect = self.sprite_image.get_rect(center = self.pos)


  def rotate(self):
    '''
    Rotates the sprite image using some pygame functions

    inputs:
      self the vector obj...
    '''

    self.sprite_image = pygame.transform.rotozoom(self.sprite_image,
        self.get_angle(), 1)
    self.update_rect()
