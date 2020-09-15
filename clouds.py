from threading import Thread
import pygame
from random import randint
import time
from rain import *

clouds = pygame.sprite.Group()


class Cloud(pygame.sprite.Sprite):
    def __init__(self, win):
        w, h = win.get_size()
        pygame.sprite.Sprite.__init__(self)
        self.win = win
        self.rain = pygame.sprite.Group()
        self.image = pygame.transform.scale((pygame.image.load('img/cloud.png')), (220, 130))
        self.rect = self.image.get_rect()
        self.rect.center = randint(0, w), 0
        self.lifespan = randint(600, 600*5)

    def update(self, all_rain):
        self.rect.centerx += 1

        self.lifespan -= 1
        if self.lifespan == 0:
            self.kill()
        if randint(6,30) > 10:
            droplet = Rain(self.win, self.rect)
            all_rain.add(droplet)
            self.rain.add(droplet)
        DrawRain(self.win, self.rain)

        if self.rect.right < 0:
            self.rect.left = self.win.get_width()

        if self.rect.left > self.win.get_width():
            self.rect.right = 0


class CloudGen(Thread):
    def __init__(self, win):
        Thread.__init__(self)
        self.win = win
        self.running = True
        self.start()

    def run(self):
        while self.running:
            r = randint(0, 100)
            if r > 80:
                cloud = Cloud(self.win)
                clouds.add(cloud)
            time.sleep(1)
