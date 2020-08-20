import pygame
from random import randint
import time
from threading import Thread
from clouds import *
from trees import *
from ground import *


def main():
    win = pygame.display.set_mode((800, 600))

    ground = pygame.sprite.Group()
    rain = pygame.sprite.Group()
    splash = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    trees = pygame.sprite.Group()

    ground = Ground(win)
    clock = pygame.time.Clock()
    TreeGen(ground, trees)
    cloud_gen = CloudGen(win, clouds)

    running = True
    try:
        while running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False

            # Game Render
            win.fill((122, 160, 147))

            clouds.update(rain)
            rain.update(win, ground, splash)
            splash.update()

            ground.draw()
            trees.draw(win)
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