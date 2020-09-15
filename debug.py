import pygame


class Surface(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((800, 100))
        self.image.fill((50,99,0))
        self.rect = self.image.get_rect(y=500)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.centerx -= 5
        if keys[pygame.K_LEFT]:
            self.rect.centerx += 5


def main():
    clock = pygame.time.Clock()
    win = pygame.display.set_mode((800, 600))
    surface = Surface()
    sky_blue = 135, 206, 235
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

        surface.update()
        win.fill(sky_blue)
        win.blit(surface.image, (surface.rect.x, 550))
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
