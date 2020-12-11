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
