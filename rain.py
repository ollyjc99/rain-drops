import pygame
from random import randint
from splash import *


class Rain(pygame.sprite.Sprite):
    def __init__(self, win, rect):
        pygame.sprite.Sprite.__init__(self)
        self.win = win
        self.image = pygame.Surface((5,5))
        self.image.fill((0,100,225))
        self.cloud = rect
        self.rect = self.image.get_rect(centerx=randint(self.cloud.x, self.cloud.x+self.cloud.width), bottom=self.cloud.bottom)

    def update(self, win, ground, splash):
        self.rect.y += 8
        if pygame.sprite.spritecollideany(self, ground):
            for pos in splashfx((self.rect.x, self.rect.y)):
                SplashGen(win, pos, splash)
            self.kill()