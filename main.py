import pygame
from random import randint


class Ground(pygame.sprite.Sprite):
    def __init__(self, win):
        w, h = win.get_size()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((win.get_width(), 40))
        self.image.fill((50, 150, 50))
        self.rect = self.image.get_rect()
        print(h)
        self.rect.center = (w // 2, h-20)


class Cloud(pygame.sprite.Sprite):
    def __init__(self, win):
        w, h = win.get_size()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale((pygame.image.load('img/cloud.png')), (180, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = randint(self.image.get_width(), w-self.image.get_width())


def main():
    win = pygame.display.set_mode((800, 600))

    ground = Ground(win)
    cloud = Cloud(win)
    all_ground = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    all_ground.add(ground)
    clouds.add(cloud)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

        # Game Render
        win.fill((122, 160, 147))
        all_ground.draw(win)
        clouds.draw(win)
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    main()
