#Kunal Rai
#The game I decided to make was a Space Invaders type game. The first thing I did in the code
#was load all the images for the lasers and the ships. The second part I did was start coding
#the first parts of my game. After I coded the smaller parts I went on to code the main game. Once I coded the main game
#I coded a little more after then made the code for the menu.
import pygame
import os
import time
import random
from pygame.locals import *
import pygame_menu #https://pygame-menu.readthedocs.io/en/latest/ . This is the website for the pygame menu
pygame.font.init()
pygame.init()
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# This is where I load all the images
RED_SPACE_SHIP = pygame.image.load(os.path.join("Final Project Images", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("Final Project Images", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("Final Project Images", "pixel_ship_blue_small.png"))

# This is the players ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("Final Project Images", "pixel_ship_yellow.png"))

# These are the lasers that the enemies shoot
RED_LASER = pygame.image.load(os.path.join("Final Project Images", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("Final Project Images", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("Final Project Images", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("Final Project Images", "pixel_laser_yellow.png"))

# This is the background image
BG = pygame.transform.scale(pygame.image.load(os.path.join("Final Project Images", "background-black.png")), (WIDTH, HEIGHT))
#This is the laser's code
class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)

#This is code for a ship
class Ship:
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

#This is code for the players ship
class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))

#This is code for the ships that are attacking the players ship
class Enemy(Ship):
    COLOR_MAP = {
                "red": (RED_SPACE_SHIP, RED_LASER),
                "green": (GREEN_SPACE_SHIP, GREEN_LASER),
                "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
                }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

#This is code to detect collisions
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

#This is the code for the main game
def main():
    run = True
    FPS = 60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    enemies = []
    wave_length = 5
    enemy_vel = 1

    player_vel = 5
    laser_vel = 5

    player = Player(300, 630)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    def redraw_window():
        WIN.blit(BG, (0,0))
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255,255,255))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0: # left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: # right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0: # up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT: # down
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, 2*60) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_vel, enemies)
#This is the code for the instructions of the menu
def instructions():
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GRAY = (200, 200, 200)

    pygame.init()
    screen = pygame.display.set_mode((800, 800))

    sysfont = pygame.font.get_default_font()
    print('system font :', sysfont)

    t0 = time.time()
    font = pygame.font.SysFont(None, 48)
    print('time needed for Font creation :', time.time()-t0)

    img = font.render(sysfont, True, RED)
    # rect = img.get_rect()
    # pygame.draw.rect(img, BLUE, rect, 1)

    font1 = pygame.font.SysFont('freesansbold.ttf', 50)
    font3 = pygame.font.SysFont('freesansbold.ttf', 30)
    img1 = font1.render('WELCOME TO SPACE INVADERS.', True, BLUE)
    img3 = font3.render('THE GOAL OF THE GAME IS TO DESTROY ALL THE ENEMY SHIPS', True, BLUE)
    font2 = pygame.font.SysFont('didot.ttc', 30)
    img2 = font2.render('W = UP | A = LEFT | S = DOWN | D = RIGHT | SPACEBAR = SHOOT', True, BLACK)
    img4 = font2.render('PRESS THE X IN THE TOP RIGHT TO RETURN TO THE MENU', True, BLACK)

    fonts = pygame.font.get_fonts()
    print(len(fonts))
    for i in range(7):
        print(fonts[i])

    running = True
    background = GRAY
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        screen.fill(background)
        screen.blit(img1, (125,50))
        screen.blit(img2, (80, 120))
        screen.blit(img3, (80, 100))
        screen.blit(img4, (80, 140))
        pygame.display.update()
#This is the menu code. I used pygame menu a pygame module that helps create menus. https://pygame-menu.readthedocs.io/en/latest/
menu = pygame_menu.Menu(800,800, 'Space Invaders' ,theme=pygame_menu.themes.THEME_BLUE)
menu.add_button('Play', main)
menu.add_button('Instructions', instructions)
menu.add_button('Quit', pygame_menu.events.EXIT)

menu.mainloop(WIN)
