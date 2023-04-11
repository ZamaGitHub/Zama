import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640,480))
baselayer = pygame.Surface((640,480))
pygame.display.set_caption('Paint')
clock = pygame.time.Clock()
FPS = 60

screen.fill((0,0,0))
functions = 1 #1 pen, 2 rectangle, 3 circle, 4 erase, 5 square, 6 triangle, 7 equilateral triangle, 8 rhombus

length = 100
isMouseDown = False
prevX = -1
prevY = -1
height = 200
colors = 'white'
colors1 = (200,200,200)

def calculateRect(x1,y1,x2,y2): #for rectangle
    return pygame.Rect(min(x1,x2),min(y1,y2), abs(x1 - x2), abs(y1 - y2))
def calculateSquare(x1,y1,x2,y2): #for square
    return pygame.Rect(min(x1,x2),min(y1,y2), abs(x1 - x2), abs(x1 - x2)) 


run = True
while run:

    key = pygame.key.get_pressed()
    if colors == 'white': #change the color
        colors1 = (200,200,200)
    if colors == 'red':
        colors1 = (255,0,0)
    if colors == 'blue':
        colors1 = (0,0,255)
    if colors == 'green':
        colors1 = (0,255,0) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_1:
                functions = 1
            elif event.key == K_2:
                functions = 2
            elif event.key == K_3:
                functions = 3
            elif event.key == K_4:
                functions = 4
            elif event.key == K_5:
                functions = 5
            elif event.key == K_6:
                functions = 6
            elif event.key == K_d: #move the point of triangle to the right
                length += 10
            elif event.key == K_a: #move the point of triangle to the left
                length -= 10
            elif event.key == K_w: #move the point of triangle to the up
                height += 10
            elif event.key == K_s: #move the point of triangle to the down
                height -= 10
            elif event.key == K_7:
                functions = 7
            elif event.key == K_8:
                functions = 8
            if event.key == K_r: #color section
                colors = 'red'
            if event.key == K_b:
                colors = 'blue'
            if event.key == K_g:
                colors = 'green'
            if event.key == K_f:
                colors = 'white'     
        if functions == 1: #pen
            currentX = prevX
            currentY = prevY
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    isMouseDown = True
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    isMouseDown = False
                    baselayer.blit(screen, (0,0))
            
            if event.type == pygame.MOUSEMOTION:
                currentX = event.pos[0]
                currentY = event.pos[1]
            if isMouseDown:
                pygame.draw.aaline(screen, colors1, (prevX,prevY),(currentX,currentY))
            prevX = currentX
            prevY = currentY  
        elif functions == 2: #rectangle
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    isMouseDown = True
                    currentX = event.pos[0]
                    currentY = event.pos[1]
                    prevX = event.pos[0]
                    prevY = event.pos[1]
            
            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baselayer.blit(screen, (0,0))
            
            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX = event.pos[0]
                    currentY = event.pos[1]
            if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                screen.blit(baselayer,(0,0))
                r = calculateRect(prevX,prevY,currentX,currentY)
                pygame.draw.rect(screen,colors1,pygame.Rect(r), 1)

        elif functions == 3: #circle
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    isMouseDown = True
                    currentX = event.pos[0]
                    currentY = event.pos[1]
                    prevX = event.pos[0]
                    prevY = event.pos[1]
            
            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baselayer.blit(screen, (0,0))
            
            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX = event.pos[0]
                    currentY = event.pos[1]
        
            if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                screen.blit(baselayer,(0,0))
                
                pygame.draw.circle(screen,colors1, (prevX,prevY), abs(prevX - currentX), 1)
        elif functions == 4: #erase
            currentX = prevX
            currentY = prevY
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    isMouseDown = True
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    isMouseDown = False
                    baselayer.blit(screen, (0,0))
            
            if event.type == pygame.MOUSEMOTION:
                currentX = event.pos[0]
                currentY = event.pos[1]
            if isMouseDown:
                pygame.draw.line(screen, (0,0,0), (prevX,prevY),(currentX,currentY), 20)
            prevX = currentX
            prevY = currentY
        elif functions == 5: #square
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    isMouseDown = True
                    currentX = event.pos[0]
                    currentY = event.pos[1]
                    prevX = event.pos[0]
                    prevY = event.pos[1]
            
            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baselayer.blit(screen, (0,0))
            
            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX = event.pos[0]
                    currentY = event.pos[1]
            if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                screen.blit(baselayer,(0,0))
                r = calculateSquare(prevX,prevY,currentX,currentY)
                pygame.draw.rect(screen,colors1,pygame.Rect(r), 1)
        elif functions == 6: #triangle
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    isMouseDown = True
                    currentX = event.pos[0]
                    currentY = event.pos[1]
                    prevX = event.pos[0]
                    prevY = event.pos[1]
            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baselayer.blit(screen, (0,0))
            
            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX = event.pos[0]
                    currentY = event.pos[1]
            if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                screen.blit(baselayer,(0,0))
                pygame.draw.polygon(screen, colors1, [[prevX, prevY], [prevX + length, prevY - height],[currentX,currentY]],1)
        elif functions == 7: #equilateral triangle
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    isMouseDown = True
                    currentX = event.pos[0]
                    currentY = event.pos[1]
                    prevX = event.pos[0]
                    prevY = event.pos[1]
            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baselayer.blit(screen, (0,0))
            
            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX = event.pos[0]
                    currentY = event.pos[1]
            if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                screen.blit(baselayer,(0,0))
                pygame.draw.polygon(screen,colors1,[[currentX - (length / 2),prevY], [currentX - length, currentY], [currentX, currentY]],1)

        elif functions == 8: #rhombus
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    isMouseDown = True
                    currentX = event.pos[0]
                    currentY = event.pos[1]
                    prevX = event.pos[0]
                    prevY = event.pos[1]
            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baselayer.blit(screen, (0,0))
            
            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX = event.pos[0]
                    currentY = event.pos[1]
            if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                screen.blit(baselayer,(0,0))
                pygame.draw.polygon(screen,colors1,[[currentX,currentY], [currentX - length, currentY - length], [currentX, currentY - height], [currentX + length, currentY - length]],1)


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
