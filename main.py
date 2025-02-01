import pygame
from constants import *

def game_loop(screen):
    clock = pygame.time.Clock() # add clock
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        pygame.display.flip()
        dt = clock.tick(FRAME_RATE) / 1000  # FRAME_RATE = 60




def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    game_loop(screen)



if __name__=="__main__":
    main()





