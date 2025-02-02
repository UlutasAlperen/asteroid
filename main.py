import pygame
from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import AsteroidField



def game_loop(screen):
    clock = pygame.time.Clock() # add clock
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable,drawable) 
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = updatable

    player = Player(SCREEN_WIDTH /2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))

        updatable.update(dt)

        for obj in drawable:
            obj.draw(screen)

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





