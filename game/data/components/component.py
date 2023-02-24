import pygame

# Game imports
from game.data.surface import Surface

class Component(Surface):
    def __init__(self, image_path: str, position_topleft: tuple) -> None:
        super().__init__()
        self.image_path = image_path
        self.surface = pygame.image.load(self.image_path).convert_alpha()
        self.rect = self.surface.get_rect()
        self.position_topleft = position_topleft

    def display_component(self) -> None:
        self.rect.topleft = self.position_topleft
        super().window.blit(self.surface, self.rect)


