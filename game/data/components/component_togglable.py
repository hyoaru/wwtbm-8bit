import pygame

# Game imports
from game.data.surface import Surface

class ComponentTogglable(Surface):
    def __init__(
        self, image_path_enabled_state: str, 
        image_path_disabled_state: str, position_topleft: tuple
    ) -> None:
        super().__init__()
        self.image_path_enabled_state = image_path_enabled_state
        self.surface_enabled_state = pygame.image.load(self.image_path_enabled_state).convert_alpha()
        self.rect_enabled_state = self.surface_enabled_state.get_rect()

        self.image_path_disabled_state = image_path_disabled_state
        self.surface_disabled_state = pygame.image.load(self.image_path_disabled_state).convert_alpha()
        self.rect_disabled_state = self.surface_disabled_state.get_rect()

        self.position_topleft = position_topleft

    def __display_component(self, surface: pygame.Surface, rect: pygame.Rect) -> None:
        rect.topleft = self.position_topleft
        super().window.blit(surface, rect)

    def display_component_enabled(self) -> None:
        self.__display_component(surface = self.surface_enabled_state, rect = self.rect_enabled_state)

    def display_component_disabled(self) -> None:
        self.__display_component(surface = self.surface_disabled_state, rect = self.rect_disabled_state)