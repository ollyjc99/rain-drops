import pygame
from random import randint
import time
from threading import Thread


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
        self.image = pygame.Surface((8, 8))
        self.image.fill((0,25,200))
        self.cloud = rect
        self.rect = self.image.get_rect(x=randint(self.cloud.x, self.cloud.x+self.cloud.width), y=(randint(self.cloud.y*2, self.cloud.y+self.cloud.height)))

    def update(self, *args):
        self.rect.y += 1
        if self.rect.y >= self.win.get_height():
            self.kill()


class Cloud(pygame.sprite.Sprite):
    def __init__(self, win, rain):
        w, h = win.get_size()
        pygame.sprite.Sprite.__init__(self)
        self.win = win
        self.image = pygame.transform.scale((pygame.image.load('img/cloud.png')), (180, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = randint(0, w)
        self.lifespan = randint(600, 600*10)
        self.rain = rain

    def update(self):
        self.lifespan -= 1
        if self.lifespan == 0:
            self.kill()
        if randint(6,30) > 25:
            self.rain.add(Rain(self.win, self.rect))


class CloudGen(Thread):
    def __init__(self, win, clouds, rain):
        Thread.__init__(self)
        self.win = win
        self.clouds = clouds
        self.rain = rain
        self.deamon = True
        self.start()

    def run(self):
        while True:
            r = randint(0, 1000)
            if r > 750:
                cloud = Cloud(self.win, self.rain)
                self.clouds.add(cloud)
            time.sleep(1)


def main():
    win = pygame.display.set_mode((800, 600))

    ground = Ground(win)
    all_ground = pygame.sprite.Group()
    all_ground.add(ground)

    rain = pygame.sprite.Group()

    clouds = pygame.sprite.Group()
    CloudGen(win, clouds, rain)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

        # Game Render
        win.fill((122, 160, 147))
        all_ground.draw(win)
        clouds.update()
        rain.update()
        rain.draw(win)
        clouds.draw(win)
        pygame.display.update()


if __name__ == '__main__':
    time_start = time.perf_counter()
    pygame.init()
    main()
    pygame.quit()
    time_finish = time.perf_counter()
    print(f'Finished in {round(time_finish - time_start, 3)} second(s)')