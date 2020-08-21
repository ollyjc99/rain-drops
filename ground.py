import pygame
from trees import *


class TreeGen(Thread):
    def __init__(self, ground, trees):
        Thread.__init__(self)
        self.daemon = True
        self.ground = ground
        self.trees = trees
        self.start()

    def run(self):
        for i in range(randint(20, 40)):
            self.trees.add(Tree((randint(self.ground.rect.x, self.ground.rect.width), self.ground.rect.top)))


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
