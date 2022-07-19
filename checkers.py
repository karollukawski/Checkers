import pygame
from checkers.constans import WIDTH, HEIGHT

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Checkers')

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        pass