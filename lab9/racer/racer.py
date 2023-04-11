import pygame
import random
from pygame.locals import *

pygame.init()

fps = 60
clock = pygame.time.Clock()

width = 400
height = 600
speed = 5
score = 0
points_to_next_level = 0
score_coins = 0
game_over = False

font = pygame.font.SysFont('Verdana', 60)
small_font = pygame.font.SysFont('Verdana', 20)

restart_button = pygame.image.load('images\\restart.png')
bg = pygame.image.load('images\AnimatedStreet.png')

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('racer')


def reset_game(): # restart game
    global score,speed,score_coins,points_to_next_level
    P1.rect.center = (160,520)
    score = 0
    speed = 5
    score_coins = 0
    points_to_next_level = 0
    E1.rect.top = 0
    E1.rect.center = (random.randint(30, 370), 0)
    C1.rect.top = 0
    C1.rect.center = (random.randint(30, 370), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images\Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0,-5)
        if self.rect.bottom < height:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0,5)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < width:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
    

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images\Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)
    def move(self):
        global score
        if game_over == True:
            self.rect.top = 0
            self.rect.center = (150, 0)
        else:
            self.rect.move_ip(0, speed)
            if self.rect.bottom > height:
                score += 1
                self.rect.top = 0
                self.rect.center = (random.randint(30, 370), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images\coin.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)
    def move(self):
        global score_coins,points_to_next_level,speed
        if game_over == True:
            self.rect.top = 0
            self.rect.center = (150, 0)
        else:
            self.rect.move_ip(0, 5)
            if self.rect.bottom > height or pygame.sprite.spritecollideany(P1, coins):
                if pygame.sprite.spritecollideany(P1, coins):
                    f = random.randint(1,3) #weight of coin
                    score_coins += f
                    points_to_next_level += f
                self.rect.top = 0
                self.rect.center = (random.randint(30, 370), 0)
            
    
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    
    def draw(self):
        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
        
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

P1 = Player()
E1 = Enemy()
C1 = Coin()
coins = pygame.sprite.Group()
coins.add(C1)
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
button = Button(width // 2 - 50, height // 2 - 100, restart_button)



run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(bg, (0,0))
    scores = small_font.render(str(score), True, (0,0,0)) 
    score_of_coins = small_font.render(str(score_coins), True, (255,0,255)) 
    screen.blit(scores, (10,10)) #show score
    screen.blit(score_of_coins, (width - 50,10)) #show coins

    if points_to_next_level >= 5: #increase speed
        speed += 2
        points_to_next_level = 0

    for i in all_sprites:
        screen.blit(i.image, i.rect)
        i.move()
    
    
    if pygame.sprite.spritecollideany(P1, enemies): #collide with enemy
        game_over = True
    
    if game_over == True: #to restart game
        if button.draw() == True:
            game_over = False
            reset_game()
    pygame.display.update()
    clock.tick(fps)

pygame.quit()


