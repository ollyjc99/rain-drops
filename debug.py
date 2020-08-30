import pygame
from trees import *


class Player(pygame.sprite.Sprite):
    def __init__(self, win):
        pygame.sprite.Sprite.__init__(self)
        w, h = win.get_size()
        self.image = pygame.Surface((50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (w // 2 - 25, h // 2 - 25)


class Surface(object):
    def __init__(self):
        self.surface = pygame.Surface((1000, 600))
        self.surface.fill((0,255,0))
        self.destx = 0

    def update(self, win):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.destx -= 5
        if keys[pygame.K_LEFT]:
            self.destx += 5


if __name__ == '__main__':
    win = pygame.display.set_mode((800, 600))
    surface = Surface()
    sprites = pygame.sprite.Group()
    player = Player(win)
    sprites.add(player)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        win.fill((255,0,0))
        surface.update(win)
        win.blit(surface.surface, (surface.destx, 0))
        sprites.draw(win)
        pygame.display.update()