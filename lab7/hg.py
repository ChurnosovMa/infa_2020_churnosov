import os
import pygame as pg
from pygame.draw import *
import random as rnd
from random import randint
import sys

pg.init()
font = pg.font.Font(None, 50)
FPS = 30
size = width, height = 1100, 600
screen = pg.display.set_mode(size)
dt = 0.01
kof = 100000
a_x = 5.5
a_y = 9.8

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
colors = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]  # the "colors" array


class Ball:
    '''
    Start of class "Ball".A circle having coordinates x, y, speed "v", radius "r", color "color".
    Displayed on the surface. Moves and is reflected when it collides with the walls of the screen.
    '''

    def __init__(self, surface, v, tau, time):
        '''
        x, y - coordinates which are set at random. r - radius which set at random.
        color - color of the ball which is set randomly from the "colors" array.
        :param surface: set the surface
        :param v: "v_x", "v_y" - speeds in horizontal and vertical direction of the screen,
        which are randomly set within the range (-v, v).
        :param tau: life time
        :param time: current time
        '''
        self.surface = surface
        self.x = randint(100, width - 100)
        self.y = randint(100, height - 100)
        self.r = randint(10, 70)
        self.color = colors[randint(0, 5)]
        self.tau = tau
        self.v = v
        self.v_x = randint(-1 * v, v)
        self.v_y = randint(-1 * v, v)
        self.time = time

    def draw(self):
        ''':return: ball in the current position.'''
        circle(self.surface, BLACK, (int(self.x), int(self.y)), int(1.1 * self.r))
        circle(self.surface, self.color, (int(self.x), int(self.y)), self.r)

    def kill(self, time):
        '''
        Kill the ball.
        :param time: current time
        '''
        self.__init__(self.surface, self.v, self.tau, self.time)
        self.time += time

    def check(self, time):
        '''
        If current time is longer than life time, function kill the ball.
        :param time: current time
        '''
        self.draw()
        self.move()
        if time > self.tau:
            self.kill(self.tau)

    def move(self):
        '''Moves the ball.'''
        self.x += self.v_x * dt
        self.y += self.v_y * dt
        if (self.x + self.r > width) or (self.x - self.r < 0):
            self.v_x *= -1
        if (self.y + self.r > height) or (self.y - self.r < 0):
            self.v_y *= -1

    def check_click(self, time, score, ball_up):
        '''
        :param time: current time
        :param score: current score
        :param ball_up: number of points for one ball
        :return: score
        '''
        x, y = pg.mouse.get_pos()
        if ((self.x - x) ** 2 + (self.y - y) ** 2 < self.r ** 2):
            self.kill(time)
            score += ball_up
        return score

    def check_collide(self, ball1):
        '''
        :param ball1: the ball has already been called
        '''
        if not ((self.x == ball1.x) and (self.y == ball1.y)):
            return ((self.x - ball1.x) ** 2 + (self.y - ball1.y) ** 2 <= (self.r + ball1.r + 5) ** 2)

    def collide(self, ball1):
        '''
        Reflects the ball from the ball1
        :param ball1: the ball has already been called
        '''
        if not ((self.x == ball1.x) or (self.y == ball1.y)):
            dx = self.x - ball1.x
            dy = self.y - ball1.y
            k = dy / dx
            self.v_x += kof / (dx ** 2 + dy ** 2) * abs(dx) / dx / ((1 + k ** 2) ** (0.5))
            self.v_y += kof / (dx ** 2 + dy ** 2) * abs(dy) / dy / ((1 + k ** 2) ** (0.5)) * abs(k)

    def exit(self):
        '''Does not allow the speed to be too high'''
        if abs(self.v_x) > 130 or abs(self.v_y) > 130:
            return True
        else:
            return False


class M_ball(Ball):
    '''
    Super Ball, which is a subclass of the ball but gives more points, shorter life time and random appearance.
    '''

    def draw(self):
        ''':return: ball in the current position.'''
        circle(self.surface, BLACK, (int(self.x), int(self.y)), int(1.1 * self.r))
        circle(self.surface, self.color, (int(self.x), int(self.y)), self.r)
        circle(self.surface, WHITE, (int(self.x), int(self.y)), int(0.5 * self.r))
        circle(self.surface, BLACK, (int(self.x), int(self.y)), int(0.3 * self.r))
        circle(self.surface, self.color, (int(self.x), int(self.y)), int(0.2 * self.r))
        circle(self.surface, WHITE, (int(self.x), int(self.y)), int(0.1 * self.r))

    def kill(self, tau):
        '''
        Kill the ball.
        :param tau: life time
        '''
        self.__init__(self.surface, self.v, self.tau, self.time)
        self.r = 0

    def M_brane(self, time):
        '''
        :param time: current time
        :return: new M_ball with propapility 0.01
        '''
        if (self.r == 0) and (randint(1, 100) == 11):
            self.__init__(self.surface, self.v, self.tau, self.time)
            self.time += time

    def move(self):
        '''Moves the M_ball.'''
        self.x += self.v_x * dt
        self.y += self.v_y * dt
        self.v_x += a_x * dt
        self.v_y += a_y * dt
        if (self.x + self.r > width) or (self.x - self.r < 0):
            self.v_x *= -0.8
        if (self.y + self.r > height) or (self.y - self.r < 0):
            self.v_y *= -0.8


class Buttons(object):
    '''Creates a button on the surface, with the color of the "color", with the text "text"'''

    def __init__(self, surface, rect, color, text):
        '''
        :param surface: the surface on which it is displayed
        :param color: button's color
        :param rect: the rectangle in which button is inscribed
        :param text: the text on the button
        '''
        self.surface = surface
        self.rect = rect
        self.color = color
        self.text = text

    def check_click(self):
        '''Ñhecks if the button is pressed'''
        x, y = pg.mouse.get_pos()
        (x_0, y_0, delta_x, delta_y) = self.rect
        return ((x > x_0) and (x < x_0 + delta_x) and (y > y_0) and (y < y_0 + delta_y))

    def draw(self):
        ''':return: button'''
        (x_0, y_0, delta_x, delta_y) = self.rect
        rect(self.surface, self.color, self.rect)
        if self.check_click():
            rect(self.surface, GREEN, self.rect)
        marvel_font = font.render(self.text, False, CYAN)
        s = pg.Surface(marvel_font.get_size(), pg.SRCALPHA)
        s_s = pg.Surface((delta_x, delta_y), pg.SRCALPHA)
        s.blit(marvel_font, (0, 0))
        pg.transform.smoothscale(s, (delta_x, delta_y), s_s)
        self.surface.blit(s_s, (x_0, y_0))


def leaders(surface):
    """
    To see the list of leaders, click on the corresponding button on the screen.
    :param surface: leaderboard output surface
    :return: displays the leaderboard on the "surface"
    """
    finish = False
    l_list = open('leaders.txt', 'r')
    inp = l_list.readlines()
    liders = []
    for i in inp:
        i = i.split()
        i[1] = int(i[1])
        liders.append([i[0], i[1]])

    def keyiii(arr):
        return arr[1]

    liders = sorted(liders, key=keyiii)
    l_list.close()
    while not finish:
        for event in pg.event.get():
            if (event.type == pg.QUIT) or (
                    event.type == pg.MOUSEBUTTONDOWN):
                finish = True
        a = 0
        for i in liders[::-1]:
            a = a + 1
            marvel_font = font.render(str(a) + '. ' + i[0] + ' ' + str(i[1]), False, (0, 0, 0))
            surface.blit(marvel_font, (400, 10 + 40 * a))
        pg.display.update()
        clock.tick(FPS)
        surface.fill(RED)


def save_player(name, score):
    '''
    :param name: player's name
    :param score: player's score
    :return: saves players and their points in a file
    '''
    l_list = open('leaders.txt', 'a')
    print(name + ': ' + str(score), file=l_list)
    l_list.close()


pg.display.update()
clock = pg.time.Clock()
finished = False
score = 0
time = 0
g = randint(8, 11)
balls = [Ball(screen, 100, randint(5, 15), time) for i in range(g)]
m_th = M_ball(screen, 180, 3, time)
m_th.kill(time)
bot = Buttons(screen, (20, 130, 150, 30), BLUE, "Leaders: ")
name = input('Your name: ') # You have to enter a name!
while not finished:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            for i in balls:
                score = i.check_click(time, score, 1)
                if i.exit == True:
                    finished = True
                    save_player(name, score)
            score = m_th.check_click(time, score, 10)
            if bot.check_click():
                leaders(screen)
    for i in balls:
        for j in balls:
            if i.check_collide(j):
                i.collide(j)
    for i in balls:
        i.check(time)
    time += dt
    m_th.check(time)
    m_th.M_brane(time)
    marvel_font = font.render(name + ': ' + str(score), False, (0, 0, 0))
    screen.blit(marvel_font, (0, 0))
    bot.draw()
    pg.display.update()
    clock.tick(FPS)
    screen.fill(WHITE)

pg.quit()