import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (255, 255, 255), (0, 0, 400, 400))
circle(screen, (255, 255, 0), (200, 200), 120)
circle(screen, (0, 0, 0), (150, 170), 10 )
circle(screen, (255, 0, 0), (150, 170), 30, 20 )
circle(screen, (0, 0, 0), (150, 170), 30, 1 )
circle(screen, (0, 0, 0), (260, 175), 10 )
circle(screen, (255, 0, 0), (260, 175), 23, 17 )
circle(screen, (0, 0, 0), (260, 175), 23, 1 )
rect(screen, (0, 0, 0), (120, 240, 175, 25))
polygon(screen, (0, 0, 0), [(80, 80), (170, 150), (179,143), (89, 73)])
polygon(screen, (0, 0, 0), [(240, 160), (350, 110), (341,102), (231,150)]) 
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit() 