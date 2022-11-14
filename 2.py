import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 2

screenWidth = 1800
screenHeight = 900
screen = pygame.display.set_mode((screenWidth, screenHeight))

GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, YELLOW, GREEN]


c = [[0, 0, 0] for i in range(4)]
cCount = 0
def new_ball():
    '''рисует новый шарик'''

    overlay = True
    cIndex = cCount % 4
    x = randint(200, screenWidth - 200)
    y = randint(200, screenHeight - 200)
    while overlay == True:
        for i in range(4):
            if ((x - c[i][0])**2 + (y - c[i][1])**2)**0.5 > 300:
                overlay = False
            else:
                overlay = True
                x = randint(200, screenWidth - 200)
                y = randint(200, screenHeight - 200)
                break
    c[cIndex][0] = x
    c[cIndex][1] = y
    cType = randint(0, 2)
    color = COLORS[cType]
    c[cIndex][2] = (cType + 1) * 50
    circle(screen, color, (c[cIndex][0], c[cIndex][1]), c[cIndex][2])
    if cIndex != 3:
        circle(screen, BLACK, (c[cIndex+1][0], c[cIndex+1][1]), c[cIndex+1][2])
    else:
        circle(screen, BLACK, (c[0][0], c[0][1]), c[0][2])

def mouseClick():
    '''обрабатывает нажатие мыши'''
    global score
    for i in range(4):
        if ((event.pos[0] - c[i][0]) ** 2 + (event.pos[1] - c[i][1]) ** 2) ** 0.5 < c[i][2]:
            text1 = f1.render(str(score), True, BLACK)
            screen.blit(text1, (100, 50))
            if c[i][2] == 150:
                score = score + 1
            if c[i][2] == 100:
                score = score + 2
            if c[i][2] ==   50:
                score = score + 3
            text1 = f1.render(str(score), True, WHITE)
            screen.blit(text1, (100, 50))
            circle(screen, BLACK, (c[i][0], c[i][1]), c[i][2])
            c[i][0] = 0
            c[i][1] = 0
            c[i][2] = 0
score = 0
pygame.display.update()
clock = pygame.time.Clock()
finished = False
cCount = 0

def timer():
    '''считает время'''
    global cCount
    global f1
    text4 = f1.render(str(cCount // 2), True, BLACK)
    screen.blit(text4, (100, 80))
    cCount = cCount + 1
    text4 = f1.render(str(cCount // 2), True, WHITE)
    screen.blit(text4, (100, 80))

def initialDisplay():
    '''начальные надписи на экране'''
    global f1
    global score
    f1 = pygame.font.Font(None, 36)
    text2 = f1.render('score : ', True, WHITE)
    screen.blit(text2, (10, 50))
    text3 = f1.render('time : ', True, WHITE)
    screen.blit(text3, (10, 80))
    score = 0
    pygame.display.update()

initialDisplay()
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouseClick()
    new_ball()
    pygame.display.update()
    timer()