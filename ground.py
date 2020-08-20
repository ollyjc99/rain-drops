import pygame


class Ground(pygame.sprite.Sprite):
    def __init__(self, win):
        pygame.sprite.Sprite.__init__(self)
        self.win = win
        w, h = self.win.get_size()
        self.image = pygame.Surface((w, 40))
        self.image.fill((50, 150, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (w // 2, h-20)
