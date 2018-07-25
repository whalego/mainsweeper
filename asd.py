# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import random
import sys
import os
import time

SCREEN_SIZE = (180, 210)
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption(u'damage')

pict_off = pygame.image.load("pict/btn_off.bmp")
pict_on = pygame.image.load("pict/btn_on.bmp")

def main():

    btn_list = []
    flug = "on"
    while True:
        screen.fill((0, 0, 0))

        #screen.blit(pict, (0, 0))

        for x in range(10):
            for y in range(10):
                btn_list = BTN(x * 18, y * 18, flug)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                #change_pict(event.type)
                flug = "on"

            if event.type == MOUSEBUTTONUP:
                if event.button == 1: #left
                    #change_pict(event.type)
                    flug = "off"
                if event.button == 3: #Right
                    print(btn_list)


def change_pict(btnStatus):
    global pict
    if btnStatus == MOUSEBUTTONDOWN:
        pict = pygame.image.load("pict/btn_on.bmp")

    elif btnStatus == MOUSEBUTTONUP:
        pict = pygame.image.load("pict/btn_off.bmp")


class BTN(object):
    def __init__(self, x, y, flug):
        super().__init__()

        if flug == "on":
            screen.blit(pict_on, (x, y))
        else:
            screen.blit(pict_off, (x, y))

    def __str__(self):
        return ",".join(map(str, [self.blit.flag, self.blit.x, self.blit.y]))

if __name__ == '__main__':
    main()
