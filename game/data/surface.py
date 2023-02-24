import pygame

from game.config import Config

class Surface():
    config = Config()
    window = pygame.display.set_mode(config.WINDOW)
    
    def __init__(self) -> None:
        pass

    def get_font(self, size,) -> pygame.font.Font:
        return pygame.font.Font(self.config.FONT_STYLE_PATH, size)

    def fill_window(self, color) -> None:
        self.window.fill(color)

    def fill_background(self) -> None:
        self.window.blit(pygame.image.load(self.config.mockup), (0,0))
