import pygame 
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from scoreboard import ScoreBoard
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Shot.containers = (shots, updatable, drawable)

    score_board = ScoreBoard(screen) 

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 

        screen.fill("black")
        score_board.draw(screen)

        for item in updatable:
            item.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game Over!")
                return

            for bullet in shots:
                if asteroid.check_collision(bullet):
                    bullet.kill()
                    asteroid.split()
                    score_board.update_score()

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
