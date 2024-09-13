import pygame

import constants

class ScoreBoard():
    def __init__(self, screen):
        self.font = pygame.font.Font(None, 32)
        self.scores = 10

    def draw(self, screen):
        text = self.font.render(str(self.scores), True, "red")
        textpos = text.get_rect(centerx=constants.SCREEN_WIDTH / 2, y=10)
        screen.blit(text, (10, 10))

    # def update(self):
    #     self.update_score()
    #     self.surface.fill("pink")
    #     text = self.font.render(str(self.scores), True, "pink")
    #     self.surface.blit(text, self.rect)
    #     print(self.scores)

    def update_score(self):
        self.scores += 1


