#coding=utf-8

import pygame
import math
from pygame.draw import *
from pygame.transform import *

pygame.init()

FPS = 30
x0 = 1100
y0 = 620
screen = pygame.display.set_mode((x0, y0))
surf = pygame.Surface((x0, y0))


GRAY=(108, 103, 82)
BLACK=(0, 0, 0)
WHITE=(255, 255, 254)
GREEN=(52,201,114)
base_color = (255, 255, 255)

rect(screen, (95,189,212), (0, 0, x0, y0))
rect(screen, GREEN, (0, 2*y0//5, x0, 3*y0//5))

#Функция, строящая забор
def wall(x1, x2, y1, y2):
    N = 19
    color = (0,0,0)
    rect(screen, (201,173,52), (x1, y1, x2 - x1, y2 - y1))
    h = (x2 - x1) // (N + 1)
    x = x1 + h
    for i in range(N + 1):
        line(screen, (color), (x, y1), (x, y2), 1)
        x += h

def dog(xdog, ydog, side, xbool): #Функция, рождающая собаку
    surf.fill(base_color)
    surf.set_colorkey(base_color)

    #Строим собаку
    ellipse(surf, GRAY, (xdog, ydog, side, side//2)) 
    ellipse(surf, GRAY, (xdog+(2*side)//3, ydog-side//8, 
                                   5*side//8, side//3)) 
    ellipse(surf, GRAY, (xdog + 15*side//14, ydog,  
                                   3*side//10, 3*side//8))
    ellipse(surf, GRAY, (xdog + 9*side//7, ydog + side//4,
                                   3*side//35, 3*side//8))
    ellipse(surf, GRAY, (xdog + 7*side//6, ydog + 9*side//15,
                                   3*side//16, 3*side//35))
    ellipse(surf, GRAY, (xdog + 30*side//31, ydog + side//9, 
                                   3*side//35, 3*side//8))
    ellipse(surf, GRAY, (xdog + 11*side//13, ydog + 7*side//15,
                                   3*side//16, 3*side//35))
    ellipse(surf, GRAY, (xdog - side//9, ydog + side//8,
                                   3*side//10, 5*side//8))
    ellipse(surf, GRAY, (xdog + side//3, ydog + 2*side//9,
                                   3*side//10, 5*side//8))
    ellipse(surf, GRAY, (xdog - side//5, ydog + 7*side//10,
                                   5*side//16, 5*side//35))
    ellipse(surf, GRAY, (xdog + 2*side//8, ydog + 8*side//10,
                                   5*side//16, 5*side//35))                    
    #Нарисуем ей морду
    rect(surf, GRAY, (xdog, ydog - side//6, 
                           side//2, side//2))    
    rect(surf, BLACK, (xdog, ydog - side//6, 
                           side//2, side//2), 1)
    circle(surf, GRAY, (xdog, ydog - side//12), side//10 )
    circle(surf, BLACK, (xdog, ydog - side//12), side//10, 1)
    circle(surf, GRAY, (xdog + side//2, ydog - side//12), side//10)
    circle(surf, BLACK, (xdog + side//2, ydog - side//12), side//10, 1)
    ellipse(surf, WHITE, (xdog + side//10, ydog, side//10, side//20) )
    ellipse(surf, WHITE, (xdog + 3*side//10, ydog, side//10, side//20) )    
    ellipse(surf, BLACK, (xdog + side//10, ydog, side//10, side//20), 2 )
    ellipse(surf, BLACK, (xdog + 3*side//10, ydog, side//10, side//20), 2 )    
    arc(surf, BLACK, (xdog+side//10, ydog + side//6, 3*side//10, side//6),
                           0, math.pi, 2)
    circle(surf, BLACK, (xdog + 3*side//20, ydog + side//40), 1)
    circle(surf, BLACK, (xdog + 21*side//60, ydog + side//40), 1 )
    #Зубы
    polygon(surf, WHITE,
                         ([xdog + 4*side//30, ydog + side/5], 
                          [xdog + 5*side//30, ydog + side//9],
                          [xdog + 7*side//40, ydog + 5*side//27],
                          ))
    polygon(surf, BLACK,
                         ([xdog + 4*side//30, ydog + side/5], 
                          [xdog + 5*side//30, ydog + side//9],
                          [xdog + 7*side//40, ydog + 5*side//27],
                          ), 1)                                                     
    polygon(surf, WHITE,
                         ([xdog + 4*side//30 + 14*side//60, ydog + side/5], 
                          [xdog + 5*side//30 + 1*side//6, ydog + side//9],
                          [xdog + 7*side//40 + 6*side//40, ydog + 5*side//27],
                          ))
    polygon(surf, BLACK,
                         ([xdog + 4*side//30 + 14*side//60, ydog + side/5], 
                          [xdog + 5*side//30 + 1*side//6 , ydog + side//9],
                          [xdog + 7*side//40 + 6*side//40, ydog + 5*side//27],
                          ), 1)       

    surface = flip(surf, xbool, False)
    screen.blit(surface, (0, 0))

wall(0, 1100, 150, 390) #Построили забор 

#Будка
polygon(screen, (201,173,52), ([4*x0//5, 20*y0//21], [4*x0//5, 4*y0//5],
                          [17*x0//25, 74*y0//105], [17*x0//25, 18*y0//21]))
polygon(screen, (201,173,52), ([4*x0//5, 4*y0//5], [5*x0//6, 2*y0//3],
                          [5*x0//6, 86*y0//105], [4*x0//5, 20*y0//21]))
polygon(screen, (255,228,13), ([4*x0//5, 4*y0//5], [17*x0//25, 74*y0//105], 
                          [37*x0//50, y0//2]))
polygon(screen, (255,228,13), ([37*x0//50, y0//2], [4*x0//5, 4*y0//5],
                          [5*x0//6, 2*y0//3], [48*x0//60, 15*y0//36]))
polygon(screen, (BLACK), ([4*x0//5, 20*y0//21], [4*x0//5, 4*y0//5],
                          [17*x0//25, 74*y0//105], [17*x0//25, 18*y0//21]), 2)
polygon(screen, (BLACK), ([4*x0//5, 4*y0//5], [5*x0//6, 2*y0//3],
                          [5*x0//6, 86*y0//105], [4*x0//5, 20*y0//21]), 2)
polygon(screen, (BLACK), ([4*x0//5, 4*y0//5], [17*x0//25, 74*y0//105], 
                          [37*x0//50, y0//2]), 2)
polygon(screen, (BLACK), ([37*x0//50, y0//2], [4*x0//5, 4*y0//5],
                          [5*x0//6, 2*y0//3], [48*x0//60, 15*y0//36]), 2)
circle(screen, (BLACK), (37*x0//50, 170*y0//205), y0//20)
#Цепь для будки
ellipse(screen, (BLACK), (71*x0//100, 175*y0//205, x0//60, y0//50), 2)
ellipse(screen, (BLACK), (70*x0//100, 176*y0//205, x0//60, y0//50), 2)
ellipse(screen, (BLACK), (70*x0//100, 177*y0//205, y0//50, x0//55), 2)
ellipse(screen, (BLACK), (70*x0//100, 181*y0//205, y0//50, x0//55), 2)
ellipse(screen, (BLACK), (70*x0//100, 186*y0//205, y0//40, x0//55), 2)
ellipse(screen, (BLACK), (69*x0//100, 190*y0//205, x0//55, y0//50), 2)
ellipse(screen, (BLACK), (67*x0//100, 191*y0//205, x0//45, y0//38), 2)
ellipse(screen, (BLACK), (65*x0//100, 192*y0//205, x0//50, y0//50), 2)
ellipse(screen, (BLACK), (65*x0//100, 194*y0//205, y0//50, x0//40), 2)
ellipse(screen, (BLACK), (65*x0//100, 201*y0//205, x0//65, y0//55), 2)


dog(100, 420, 200, 0)#Родили собаку


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()