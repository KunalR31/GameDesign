import pygame, time, sys
pygame.init()
pygame.time.delay(100)
screen=pygame.display.set_mode((1000,800))
white=[225,255,255]
red=[255,0,255]
black=[0,0,0]
screen.fill(white)
pygame.display.set_caption("My Shapes")
pygame.display.flip()
running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.quit:
            running = False
    pygame.time.delay(100)
    x=20
    y=20
    w=50
    h=100

    keyBoardKey=pygame.key.get_pressed()
    speed = 10   
    if keyBoardKey[pygame.K_LEFT]:
        x -= speed
    if keyBoardKey[pygame.K_RIGHT]:
        x += speed
    if keyBoardKey[pygame.K_UP]:
        y -= speed
    if keyBoardKey[pygame.K_DOWN]:
        y += speed
    screen.fill(white)
    pygame.draw.rect(screen,(10,123,10),(200,200, 50,100))
        # pygame.draw.circle(screen,(0, 120,129), (100,100),50, 4)
    pygame.display.update()
pygame.quit()
