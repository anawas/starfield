import pygame
import numpy as np
import random
from game_objects import RadialStar

WIDTH = 800
HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MAX_STARS = 400

starfield = []

def event_handler(event_queue):
    for event in event_queue:
        if event.type == pygame.QUIT:
            return False
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
    return True

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    for _ in range(MAX_STARS):
        starfield.append(RadialStar(screen))

    pygame.display.set_caption("PyGame")

    clock = pygame.time.Clock()
    
    running = True
    while running:
        clock.tick(30)
        screen.fill(BLACK)

        running = event_handler(pygame.event.get())
        create_stars(screen)
        for star in starfield:
            star.update()

        pygame.display.flip()

def create_stars(screen):
    for i in range(0, MAX_STARS):
        if starfield[i].done():
            del starfield[i]
            starfield.append(RadialStar(screen))


if __name__ == "__main__":
    main()