import pygame
from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import AsteroidField
import sys
from shot import Shot
from scorepopup import ScorePopup


def game_loop(screen):
    score = 0
    clock = pygame.time.Clock() # add clock
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    score_popups = pygame.sprite.Group()

    Player.containers = (updatable,drawable) 
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable,drawable,shots)
    ScorePopup.containers = (updatable,drawable,score_popups)


    player = Player(SCREEN_WIDTH /2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print(f"Game over!\nPlayer score: {score}")
                sys.exit()

            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()
                    points = 0
                    if asteroid.radius > ASTEROID_MIN_RADIUS *2:
                        points += 20
                    elif asteroid.radius > ASTEROID_MIN_RADIUS:
                        points += 50
                    else:
                        points += 100
                    ScorePopup(asteroid.position.x,asteroid.position.y,points)
                    score += points
                    asteroid.split()


        screen.fill((0,0,0))

        for obj in drawable:
            obj.draw(screen)


        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        score_rect = score_text.get_rect()
        score_rect.topright = (SCREEN_WIDTH - 10, 10)  # Position score in top-right corner
        screen.blit(score_text, score_rect)
        pygame.display.flip()
        dt = clock.tick(FRAME_RATE) / 1000  # FRAME_RATE = 60

        



def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.init()
    game_loop(screen)



if __name__=="__main__":
    main()





