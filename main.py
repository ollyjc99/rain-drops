import pygame
from random import randint
import time
from threading import Thread
import atexit
from clouds import *


class Ground(pygame.sprite.Sprite):
    def __init__(self, win):
        w, h = win.get_size()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((win.get_width(), 40))
        self.image.fill((50, 150, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (w // 2, h-20)


def main():
    win = pygame.display.set_mode((800, 600))

    ground = Ground(win)
    all_ground = pygame.sprite.Group()
    all_ground.add(ground)

    rain = pygame.sprite.Group()
    splash = pygame.sprite.Group()
    clouds = pygame.sprite.Group()

    cloud_gen = CloudGen(win, clouds)
    running = True
    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False

            # Game Render
            win.fill((122, 160, 147))

            clouds.update(rain)
            rain.update(win, all_ground, splash)
            splash.update()

            all_ground.draw(win)
            splash.draw(win)
            rain.draw(win)
            clouds.draw(win)

            pygame.display.update()

    except KeyboardInterrupt:
        print('Keyboard Interrupt')

    except pygame.error:
        print('PyGame Error')

    finally:
        cloud_gen.running = False


if __name__ == '__main__':
    time_start = time.perf_counter()
    pygame.init()
    main()
    pygame.quit()
    time_finish = time.perf_counter()
    print(f'Finished in {round(time_finish - time_start, 3)} second(s)')