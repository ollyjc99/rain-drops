import pygame

def main():
    win = pygame.display.set_mode((800, 600))
    win.fill((130,225,225))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    main()
