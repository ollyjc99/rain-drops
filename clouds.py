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
        self.image = pygame.transform.scale((pygame.image.load('img/cloud.png')), (180, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = randint(0, w)
        self.lifespan = randint(600, 600*10)

    def update(self, rain):
        self.lifespan -= 1
        if self.lifespan == 0:
            self.kill()
        if randint(6,30) > 20:
            rain.add(Rain(self.win, self.rect))


class CloudGen(Thread):
    def __init__(self, win, clouds):
        Thread.__init__(self)
        self.win = win
        self.clouds = clouds
        self.running = True
        self.start()

    def run(self):
        while self.running:
            r = randint(0, 1000)
            if r > 700:
                cloud = Cloud(self.win)
                self.clouds.add(cloud)
            time.sleep(1)
