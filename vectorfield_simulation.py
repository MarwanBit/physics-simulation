import pymunk
 
import pygame

from vector_class import Vector

from sympy import symbols, diff

import game_functions as gf

from spinning_circle_class import SpinningCircle

import math


#create the space for which we do physics calculations
space = pymunk.Space()

#create the visual space using pygame...
pygame.init()
clock = pygame.time.Clock()

#the screen is created....
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
caption = "Physics Vector Field Simulation"
pygame.display.set_caption(caption)

#Create the background which we will draw everything onto....
background = pygame.Surface(screen_size)
#set the color of the background
background_color = (255, 255, 255) 

#deltat/ other constant declaration...
t = 0.1
delta_t = 0.1

#Now create the vector field function
x, y = symbols('x y', real=True)
#component functions f_1 and f_2 of the vectorfield...
f_1 = 2*y*y
f_2 = -1*x
vector_field = (f_1, f_2)

#Initialize the vector field by generating a list of vectors on R^2...
vector_list = []
#Create spinning circles in 50x50 sized grids....
for x_pos in range(0,screen_size[0], screen_size[0]//10):
  for y_pos in range(0, screen_size[1], screen_size[1]//10):
    #Create the vector and evaluate it....
    vector = Vector(
      gf.evaluate_vector_field(vector_field, x_pos, y_pos), 
      (x_pos,y_pos)
      )
    vector.rotate()
    vector_list.append(vector)

#create a bunch of spinning circles....
spinning_circle_list = []
#Create spinning circles in 50X50 sized grids...
for x_pos in range(0, screen_size[0], screen_size[0]//5):
  for y_pos in range(0, screen_size[1], screen_size[1]//5):
    spinning_circle_list.append(SpinningCircle((x_pos, y_pos)))


#Set simulation active...
simulation_active = True 

#This creates the main loop for the program...
while simulation_active:
  #iterate through the event loop....
  for event in pygame.event.get():
    #handles what happens when we click the exit button...
    if event.type == pygame.QUIT:
      #End the game if we click on the exit button..
      simulation_active = False
  
  #Now update the screen...
  background.fill(background_color)
  #Now we update the background

  #Draw 
  for vector in vector_list:
    background.blit(vector.sprite_image, vector.pos)

  #Draw the spinning circles and update them...
  for spinning_circle in spinning_circle_list:
    rotated_tuple = spinning_circle.return_rotated_version(t,
        vector_field)
    background.blit(rotated_tuple[0], rotated_tuple[1])

  #Update the current time...
  t = t + delta_t

  screen.blit(background, (0,0)) #draw the background onto the screen
  pygame.display.flip()
  clock.tick(60)

