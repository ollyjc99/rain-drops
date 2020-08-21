from threading import Thread
import pygame
from random import randint
import time
from rain import *


class Cloud(pygame.sprite.Sprite):
    def __init__(self, win):
        w, h = win.get_size()
        pygame.sprite.Sprite.__init__(self)
        self.win = win
        self.rain = pygame.sprite.Group()
        self.image = pygame.transform.scale((pygame.image.load('img/cloud.png')), (220, 130))
        self.rect = self.image.get_rect()
        self.rect.centerx = randint(0, w)
        self.rect.centery = 0
        self.lifespan = randint(600, 600*5)

    def update(self, all_rain):
        self.lifespan -= 1
        if self.lifespan == 0:
            self.kill()
        if randint(6,30) > 10:
            all_rain.add(Rain(self.win, self.rect))
            self.rain.add(Rain(self.win, self.rect))

        DrawRain(self.win, self.rain)


class CloudGen(Thread):
    def __init__(self, win, clouds):
        Thread.__init__(self)
        self.win = win
        self.clouds = clouds
        self.running = True
        self.start()

    def run(self):
        while self.running:
            r = randint(0, 100)
            if r > 80:
                cloud = Cloud(self.win)
                self.clouds.add(cloud)
            time.sleep(1)
