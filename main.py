import pygame
from random import randint
import time
from threading import Thread
from clouds import *
from trees import *
from terrain import *

clock = pygame.time.Clock()


def main():
    win = pygame.display.set_mode((800, 600))
    surf = Surface()

    all_sprites = pygame.sprite.Group()
    surface = pygame.sprite.Group()
    terrain = Ground(surf.image)
    surface.add(terrain)

    TreeGen(terrain, surface)
    cloud_gen = CloudGen(surf.image)

    running = True
    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False

            surf.update(win)
            surface.draw(surf.image)

            terrain.update()
            clouds.update(rain)
            rain.update(surf.image, terrain, splash)
            splash.update()

            all_sprites.add(*[clouds, splash])
            all_sprites.draw(surf.image)

            win.fill((0, 0, 0))
            win.blit(surf.image, surf.rect)
            pygame.display.update()
            clock.tick(60)

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
    time_finish = time.perf_counter()
    print(f'Finished in {round(time_finish - time_start, 3)} second(s)')
