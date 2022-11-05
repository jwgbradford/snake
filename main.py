import pygame
from pygame.locals import *

WIDTH = 400
HEIGHT = 600

class Game():
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('DigiLocal Snake')

    def screen_reset(self):
        self.screen.fill((153, 51, 0))
        pygame.draw.rect(
            self.screen,
            (204, 102, 0),
            Rect(
                (10, 10),
                (WIDTH - 20, HEIGHT - 20)
            )
        )
    
    def run(self):
        while True:
            self.screen_reset()
            pygame.display.update()

if __name__ == '__main__':
    my_game = Game()
    my_game.run()