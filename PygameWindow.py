# import pygame
# import sys, time
# pygame.init()
# width = (1000)
# height = (1000)
# color = input('What color will the window be? ')
# if color == 'red':
#     screen.fill(255,0,0)
# screen = pygame.display.set_mode((width, height))
# screen.fill(color)
# pygame.display.flip()
import pygame, sys
pygame.init()
screen = pygame.display.set_mode([800,600])
white = [255, 255, 255]
red = [255, 0, 0]
screen.fill(white)
pygame.display.set_caption("My program")
pygame.display.flip()



background = input("What color would you like?: ")
if background == "red":
    screen.fill(red)
