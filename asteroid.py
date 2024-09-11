import circleshape
import pygame
import constants
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        spawn_angle = random.uniform(20, 50)
        spawn_velocity_one = self.velocity.rotate(spawn_angle)
        spawn_velocity_two = self.velocity.rotate(spawn_angle * -1)

        smaller_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(self.position.x, self.position.y, smaller_radius)
        asteroid_one.velocity = spawn_velocity_one * constants.ASTEROID_SPLIT_MULTIPLY_FACTOR 

        asteroid_two = Asteroid(self.position.x, self.position.y, smaller_radius)
        asteroid_two.velocity = spawn_velocity_two * constants.ASTEROID_SPLIT_MULTIPLY_FACTOR
        
