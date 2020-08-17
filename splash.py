import pygame
from threading import Thread

class Splash(pygame.sprite.Sprite):
    def __init__(self, win, pos):
        pygame.sprite.Sprite.__init__(self)
        self.win = win
        self.lifespan = 5
        self.image = pygame.Surface((3, 3))
        self.image.fill((0,100,225))
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        self.lifespan -= 1
        if self.lifespan <= 0:
            self.kill()


class SplashGen(Thread):
    def __init__(self, win, pos, splash):
        Thread.__init__(self)
        self.daemon = True
        self.win = win
        self.pos = pos
        self.splash = splash
        self.start()

    def run(self):
        self.splash.add(Splash(self.win, self.pos))


def splashfx(pos):
    x, y = pos
    return [
        (x-4, y-1),
        (x-1.5, y+1),
        (x, y+1),
        (x+1.5, y+1),
        (x+4, y-1)
    ]

