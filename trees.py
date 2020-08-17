import pygame
from threading import Thread


class Tree(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite(self)
        self.image = pygame.image.load('img/pine-tree.png')