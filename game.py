import pygame


class Game:

    def __init__(self):
        pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pygamon Adventure")

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()
