# #Kunal Rai
# import pygame
# import sys
#
#
# # initializing the constructor
# pygame.init()
#
# # screen resolution
# res = (900,900)
#
# # opens up a window
# screen = pygame.display.set_mode(res)
#
# # white color
# color = (255,255,255)
#
# # light shade of the button
# color_light = (170,170,170)
#
# # dark shade of the button
# color_dark = (100,100,100)
#
# # stores the width of the
# # screen into a variable
# width = screen.get_width()
#
# # stores the height of the
# # screen into a variable
# height = screen.get_height()
#
# # defining a font
# smallfont = pygame.font.SysFont('Corbel',35)
#
# # rendering a text written in
# # this font
# text = smallfont.render('quit' , True , color)
#
# while True:
#
#     for ev in pygame.event.get():
#
#         if ev.type == pygame.QUIT:
#             pygame.quit()
#
#         #checks if a mouse is clicked
#         if ev.type == pygame.MOUSEBUTTONDOWN:
#
#             #if the mouse is clicked on the
#             # button the game is terminated
#             if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
#                 pygame.quit()
# text2 = smallfont.render('Instructions' , True, color_light)
#
# while True:
#     for ev in pygame.event.get():
#
#         if ev.type == pygame.MOUSEBUTTONDOWN:
#             if width/2 <= mouse[0] <= width/2+160 and height/2 <= mouse[1] <= height/2+80:
#                 Print('welcome')
#
#
#
#     # fills the screen with a color
#     screen.fill((60,25,60))
#
#     # stores the (x,y) coordinates into
#     # the variable as a tuple
#     mouse = pygame.mouse.get_pos()
#
#     # if mouse is hovered on a button it
#     # changes to lighter shade
#     if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
#         pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])
#
#     else:
#         pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])
#
#
#     # superimposing the text onto our button
#     screen.blit(text , (width/2+50,height/2))
#
#     # updates the frames of the game
#     pygame.display.update()
# import pygame
# import sys
# global win
# pygame.init()
# pygame.window.blit(bg, (0,0))
#
# def menu():
#     button1 = pygame.rect(100,100,100,100)
#     button2 = pygame.rect(200,200,200,200)
#     button3 = pygame.rect(300,300,300,300)
#     button4 = pygame.rect(400,400,400,400)
#     pygame.draw.rect(win,(0,102,0), button1)
#     pygame.draw.rect(win,(0,102,0), button2)
#     pygame.draw.rect(win,(0,102,0), button3)
#     pygame.draw.rect(win,(0,102,0), button4)
#     text= TITLE_FONT.render("MAN", 1, (0,0,0))
#     win.blit(text, (WIDTH/2 - text.get_width()/2, 20))
#     text2= TITLE_FONT2.render("PLAY", 1, (0,0,0))
#     win.blit(text2, (WIDTH/2 - text.get_width()/4, 75))
#
#     text3= TITLE_FONT.render("INSTRUCTIONS", 1, (0,0,0))
#     win.blit(text3, (WIDTH/2 - text.get_width()/2, 480))
#
#     text4= TITLE_FONT.render("EASY", 1, (0,0,0))
#     win.blit(text4, (160,555))
#
#     text5= TITLE_FONT.render("MEDIUM", 1, (0,0,0))
#     win.blit(text5, (140,630))
#
#     text6= TITLE_FONT.render("HARD", 1, (0,0,0))
#     win.blit(text6, (160, 705))
import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 800

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

# block_color = (53,115,255)
#
# car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Fire Man')
clock = pygame.time.Clock()
#
# carImg = pygame.image.load('background.png')
#
#
# def things_dodged(count):
#     font = pygame.font.SysFont(None, 25)
#     text = font.render("Dodged: "+str(count), True, black)
#     gameDisplay.blit(text,(0,0))
#
# def things(thingx, thingy, thingw, thingh, color):
#     pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
#
# def car(x,y):
#     gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
#
# def message_display(text):
#     largeText = pygame.font.Font('freesansbold.ttf',115)
#     TextSurf, TextRect = text_objects(text, largeText)
#     TextRect.center = ((display_width/2),(display_height/2))
#     gameDisplay.blit(TextSurf, TextRect)
#
#     pygame.display.update()
#
#     time.sleep(2)
#
#     game_loop()
#


# def crash():
#     message_display('You Crashed')

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Fire Man", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,(0,200,0),(0,255,0),game_loop)
        button("Quit",550,450,100,50,(200,0,0),(255,0,0),pygame.quit())

        pygame.display.update()
        clock.tick(15)



def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)

        things(thing_startx, thing_starty, thing_width, thing_height, block_color)



        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        if y < thing_starty+thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(60)

game_intro()
pygame.quit()
