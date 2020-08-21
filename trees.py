import pygame
from random import randint
from threading import Thread


class DrawTrees(Thread):
    def __init__(self, *args):
        Thread.__init__(self)
        self.daemon = True
        self.win, self.trees = args
        self.start()

    def run(self):
        self.trees.draw(self.win)


class Tree(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(f'img/pine-tree-{randint(1,2)}.png'), (randint(240, 310), randint(320, 340)))
        x, y = pos
        self.rect = self.image.get_rect(centerx=x, bottom=y)

    def update(self):
        pass


class PineTree(Tree):
    def __str__(self):
        return f'Pine Tree'


class OakTree(Tree):
    def __str__(self):
        return f'Oak Tree'


class SycamoreTree(Tree):
    def __str__(self):
        return f'Sycamore Tree'
