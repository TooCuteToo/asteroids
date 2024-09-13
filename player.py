import pygame
import circleshape
import constants
import shot

class Player(circleshape.CircleShape):
    def __init__(self, x, y, lives):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 180
        self.shot_cooldown = 0
        self.lives = lives 

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def move(self, dt):
        fwd = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += fwd * constants.PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(dt * -1)

        self.shot_cooldown -= dt

        if keys[pygame.K_SPACE] and self.shot_cooldown <= 0:
            self.shot()

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def shot(self):
        bullet = shot.Shot(self.position.x, self.position.y, constants.SHOT_RADIUS)
        bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * constants.PLAYER_SHOT_SPEED
        self.shot_cooldown = constants.PLAYER_SHOT_COOLDOWN

    def respawn(self):
        self.lives -= 1
        self.position = pygame.Vector2(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    def draw_lives(self, screen):
        font = pygame.font.Font(None, 36)
        text = font.render(str(self.lives), True, "red")
        screen.blit(text, (50, 10))
        
