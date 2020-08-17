import pygame
from random import randint
from threading import Thread


class Tree(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('img/pine-tree.png'), (randint(280, 350), randint(320, 420)))
        x, y = pos
        self.rect = self.image.get_rect(centerx=x, bottom=y)


class TreeGen(Thread):
    def __init__(self, ground, trees):
        Thread.__init__(self)
        self.daemon = True
        self.ground = ground
        self.trees = trees
        self.start()

    def run(self):
        for i in range(randint(25, 75)):
            self.trees.add(Tree((randint(self.ground.rect.x, self.ground.rect.width), self.ground.rect.top)))
