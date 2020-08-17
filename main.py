import pygame
from random import randint
import time
from threading import Thread
import atexit


class Ground(pygame.sprite.Sprite):
    def __init__(self, win):
        w, h = win.get_size()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((win.get_width(), 40))
        self.image.fill((50, 150, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (w // 2, h-20)


class Rain(pygame.sprite.Sprite):
    def __init__(self, win, rect):
        pygame.sprite.Sprite.__init__(self)
        self.win = win
        self.image = pygame.Surface((5,5))
        self.image.fill((0,100,225))
        self.cloud = rect
        self.rect = self.image.get_rect(centerx=randint(self.cloud.x, self.cloud.x+self.cloud.width), bottom=self.cloud.bottom)

    def update(self, win, ground, splash):
        self.rect.y += 3
        if pygame.sprite.spritecollideany(self, ground):
            for pos in splashfx((self.rect.x, self.rect.y)):
                SplashGen(win, pos, splash)
            self.kill()


class Splash(pygame.sprite.Sprite):
    def __init__(self, win, pos):
        pygame.sprite.Sprite.__init__(self)
        self.win = win
        self.lifespan = 5
        self.image = pygame.Surface((3, 3))
        self.image.fill((0,100,225))
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        self.lifespan -= 1
        if self.lifespan <= 0:
            self.kill()


class Cloud(pygame.sprite.Sprite):
    def __init__(self, win):
        w, h = win.get_size()
        pygame.sprite.Sprite.__init__(self)
        self.win = win
        self.image = pygame.transform.scale((pygame.image.load('img/cloud.png')), (180, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = randint(0, w)
        self.lifespan = randint(600, 600*10)

    def update(self, rain):
        self.lifespan -= 1
        if self.lifespan == 0:
            self.kill()
        if randint(6,30) > 25:
            rain.add(Rain(self.win, self.rect))


class CloudGen(Thread):
    def __init__(self, win, clouds):
        Thread.__init__(self)
        self.win = win
        self.clouds = clouds
        self.running = True
        self.start()

    def run(self):
        while self.running:
            print('Running')
            r = randint(0, 1000)
            if r > 700:
                cloud = Cloud(self.win)
                self.clouds.add(cloud)
            time.sleep(1)


class SplashGen(Thread):
    def __init__(self, win, pos, splash):
        Thread.__init__(self)
        self.daemon = True
        self.win = win
        self.pos = pos
        self.splash = splash
        self.start()

    def run(self):
        self.splash.add(Splash(self.win, self.pos))


def splashfx(pos):
    x, y = pos
    return [
        (x-4, y-1),
        (x-1.5, y+1),
        (x, y+1),
        (x+1.5, y+1),
        (x+4, y-1)
    ]


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