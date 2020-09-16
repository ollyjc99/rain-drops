import pygame
from random import randint
from splash import *

rain = pygame.sprite.Group()
splash = pygame.sprite.Group()


class DrawRain(Thread):
    def __init__(self, *args):
        Thread.__init__(self)
        self.daemon = True
        self.win, self.rain = args
        self.start()

    def run(self):
        self.rain.draw(self.win)

    def __str__(self):
        return 'Process to draw rain sprites'


class Rain(pygame.sprite.Sprite):
    def __init__(self, win, rect):
        pygame.sprite.Sprite.__init__(self)
        self.win = win
        self.image = pygame.image.load('img/rain-drop.png')
        self.cloud = rect
        self.rect = self.image.get_rect(centerx=randint(self.cloud.x, self.cloud.x+self.cloud.width), bottom=self.cloud.centery)

    def update(self, win, ground, splash):
        self.rect.y += 8
        if self.rect.right <= 0 or self.rect.left >= win.get_width() or self.rect.top >= win.get_height():
            self.kill()
        if pygame.sprite.collide_rect(self, ground):
            for pos in splashfx((self.rect.x, self.rect.y)):
                SplashGen(win, pos, splash)
            self.kill()
