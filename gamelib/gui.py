import pygame
import config




class UI(object):
    def __init__(self, surface):
        self.surface = surface
        self.conf = config.Config().settings

    def make_button(self, text, position):
        font = pygame.font.Font('data/Vanadine Regular.ttf', 30)
        rect = pygame.draw.rect(self.surface, self.conf["colors"]["textcolor"], position, 3)
        text = font.render(text, False, self.conf["colors"]["textcolor"])
        text_rect = text.get_rect()
        text_rect.center = rect.center
        self.surface.blit(text, text_rect)
        return rect

