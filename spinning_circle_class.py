import pygame 

from vector_class import Vector

from sympy import symbols, diff

import game_functions as gf


class SpinningCircle():
	'''
	Creates the spinning circle which we use for our simulation...
	'''

	def __init__(self, pos):
		'''
		Creates the SpinningCircle with a position

		inputs:
			pos (..)
		'''

		#Creates our position vector object...
		self.position_vector = Vector(pos, (0,0)) 
		self.sprite_image = pygame.image.load('spinning_circle.png')
		self.sprite_image_rect = self.sprite_image.get_rect(center = pos)


	def get_current_angular_velocity(self, vector_field):
		'''
		Gets the angular frequency at the SpinningCircle's position, 
		vectorfield is a tuple of functions (f_1(x,y), f_2(x,y))

		inputs:
			vector_field(...) [the vector_field function...]

		outputs:
			angular frequency.... 0.5 curlF ...
		'''

		x, y = symbols('x y', real=True)

		scalar_curl = diff(vector_field[1],x) - diff(vector_field[0], y)
		scalar_curl = scalar_curl.subs([(x, self.position_vector.vector[0]), (y, self.position_vector.vector[1])]).evalf()

		#Note that the units for this are in rads/sec
		return 0.5 * scalar_curl


	def return_rotated_version(self, t, vector_field):
		'''
		Now we make sure to rotate the spinning circle using some pygame functions....

		inputs:
			self (the SpinningCircle object...)
			delta_t (the thing we use to get our angular velocity...)
		'''

		rotated_surface = pygame.transform.rotozoom(self.sprite_image, -1*(self.get_current_angular_velocity(vector_field)*t), 1)
		rotated_rect = rotated_surface.get_rect(center = self.position_vector.vector)
		return (rotated_surface, rotated_rect)
