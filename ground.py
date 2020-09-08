import pygame
from trees import *


class Surface(object):
    def __init__(self):
        self.image = pygame.Surface((1600, 600))
        self.image.fill((122, 160, 147))
        self.destx = 0

    def update(self, win):
        keys = pygame.key.get_pressed()
        rect = self.image.get_rect(x=self.destx)

        if keys[pygame.K_RIGHT]:
            if rect.right >= 0:
                self.destx -= 3

        if keys[pygame.K_LEFT]:
            if rect.left <= win.get_width():
                self.destx += 3
            

class TreeGen(Thread):
    def __init__(self, ground, trees):
        Thread.__init__(self)
        self.daemon = True
        self.ground = ground
        self.trees = trees
        self.start()

    def run(self):
        print(self.ground.rect)
        for i in range(randint(20, 40)):
            self.trees.add(Tree((randint(50, self.ground.rect.width-50), self.ground.rect.top)))


class Ground(pygame.sprite.Sprite):
    def __init__(self, win):
        pygame.sprite.Sprite.__init__(self)
        self.win = win
        w, h = self.win.get_size()
        self.trees = pygame.sprite.Group()
        self.image = pygame.Surface((w, 40))
        self.image.fill((50, 150, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (w // 2, h-20)

    def update(self, *args):
        DrawTrees(self.win, self.trees)
