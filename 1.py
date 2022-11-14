import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 800))
screen.fill((255, 255, 255))


circle(screen, (0, 0, 0), (200, 200), 100)
circle(screen, (255, 255, 255), (270, 180), 100)
circle(screen, (0, 0, 0), (600, 200), 100)
circle(screen, (255, 255, 255), (530, 180), 100)

circle(screen, (139, 0, 255), (400, 400), 300)

circle(screen, (0, 0, 0), (400, 360), 200)
circle(screen, (139, 0, 255), (400, 340), 200)

polygon(screen, (0, 0, 0), ([510, 510], [580, 550], [560, 470]))
polygon(screen, (0, 0, 0), ([800-510, 510], [800-580, 550], [800-560, 470]))

polygon(screen, (0, 0, 0), ([250, 200], [350, 300], [340, 310], [240, 210]))
polygon(screen, (0, 0, 0), ([800-250, 200], [800-350, 300], [800-340, 310], [800-240, 210]))

x = 579
y = 578
r = 16
d = 100
for i in range(2):
    circle(screen, (255, 0, 0), (x, y+d*i), r)
    polygon(screen, (255, 0, 0), ([x-r/2**0.5, y-r/2**0.5+d*i], [x, y-30+d*i], [x+r/2**0.5, y-r/2**0.5+d*i]))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit().quit()