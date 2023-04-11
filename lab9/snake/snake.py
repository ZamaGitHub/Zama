import pygame,random

pygame.init()

BLACK = (0,0,0)
LINE_COLOR = (50,50,50)
WIDTH = 400
HEIGHT = 400
PANEL = 100
BLOCK_SIZE = 20
FPS = 5
score = 0
level = 1 
points_for_new_level = 0
run1 = True
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 7000)

font = pygame.font.SysFont('Verdana', 20)
font1 = pygame.font.SysFont('Verdana', 60)
game_over = font1.render('Game End', True, (0,0,0))

screen = pygame.display.set_mode((WIDTH, HEIGHT + PANEL))
pygame.display.set_caption('snake')
CLOCK = pygame.time.Clock()
screen.fill(BLACK)

def reset_game(): #restart the game
    global level,score,FPS,points_for_new_level,wall
    snake.body = [Point(10,11)]
    snake.dx = 0
    snake.dy = 0
    level = 1
    score = 0
    FPS = 5
    snake.level = 1
    points_for_new_level = 0
    wall = Wall(snake.level)


class Point():
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

class Wall:
    def __init__(self, level):
        self.body = []
        try:
            f = open('levels\level{}.txt'.format(level), 'r') #levels
            for y in range(HEIGHT // BLOCK_SIZE + 1):
                for x in range(WIDTH // BLOCK_SIZE + 1):
                    if f.read(1) == '#':
                        self.body.append(Point(x,y))
        except:
            reset_game()
    
    def draw(self):
        for point in self.body:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, (226,135,67), rect)


class Food():
    def __init__(self):
        self.location = Point(random.randint(1,19),random.randint(1,19))
        self.last_generated_food = 0
        self.food_timer = 3000
    
    def draw(self):
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE,BLOCK_SIZE)
        pygame.draw.rect(screen, (0,255,0), rect)
    
    

def DrawGrid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x,y,BLOCK_SIZE,BLOCK_SIZE)
            pygame.draw.rect(screen, LINE_COLOR, rect, 1)

class Snake:
    def __init__(self):
        self.body = [Point(10,11)]
        self.dx = 0
        self.dy = 0
        self.level = 1
    
    def move(self):
        global run1, run, score, level
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y
        
        self.body[0].x += self.dx
        self.body[0].y += self.dy

        if self.body[0].x * BLOCK_SIZE >= WIDTH: #check border collision 
            run1 = False

        if self.body[0].y * BLOCK_SIZE >= HEIGHT: #check border collision
            run1 = False
        
        if self.body[0].x < 0: #check border collision
            run1 = False
        
        if self.body[0].y < 0: #check border collision
            run1 = False
        
        if run1 == False:
            reset_game()
            run1 = True
        
    def draw(self):
        point = self.body[0]
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(screen, (255,0,0), rect)

        for point in self.body[1:]:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, (0, 255, 0), rect)

    def check_collision(self,food): #check if snake eats food
        global score,points_for_new_level, FPS,level,wall
        if self.body[0].x == food.location.x:
            if self.body[0].y == food.location.y:
                self.body.append(Point(food.location.x, food.location.y)) #increase the length of body
                f = random.randint(1,3) #weight of food 
                score += f #score
                points_for_new_level += f #count points to go to the next level
                if points_for_new_level >= 5:
                    snake.level += 1
                    FPS += 2 #increase speed
                    level += 1 #new level
                    points_for_new_level = 0
                    wall = Wall(snake.level)
                food.location = Point(random.randint(1,19),random.randint(1,19)) #random loacation of food
    def eat_itself(self): #collide with itself
        global run1
        for i in self.body[1:]:
            if self.body[0].x == i.x:
                if self.body[0].y == i.y:
                    run1 = False
    
    def collision_with_board(self): #collision with board of levels
        global run1
        for i in wall.body:
            if self.body[0].x == i.x:
                if self.body[0].y == i.y:
                    run1 = False

snake = Snake()
food = Food()
wall = Wall(snake.level)

run = True
while run:
    
    
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            food.location = Point(random.randint(1,19),random.randint(1,19))
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx != -1:
                snake.dx = 1
                snake.dy = 0
            if event.key == pygame.K_LEFT and snake.dx != 1:
                snake.dx = -1
                snake.dy = 0
            if event.key == pygame.K_UP and snake.dy != 1:
                snake.dx = 0
                snake.dy = -1
            if event.key == pygame.K_DOWN and snake.dy != -1:
                snake.dx = 0
                snake.dy = 1

    snake.move()
    snake.eat_itself()
    snake.check_collision(food)
    snake.collision_with_board()
    
    
    
    screen.fill(BLACK)

    snake.draw()
    food.draw()
    wall.draw()

    DrawGrid()
    scores = font.render(f'Score {score}', True, (255,0,0)) 
    levels = font.render(f'Level {level}', True, (255,0,0)) 
    screen.blit(scores, (20, HEIGHT + 30))  #show score
    screen.blit(levels, (250, HEIGHT + 30)) #show level
    pygame.display.update()
    CLOCK.tick(FPS)
pygame.quit()
