import pygame

# Game imports
from game.data.surface import Surface

class PointTextTogglable(Surface):
    def __init__(self, value: int, number: int, position_topleft: tuple) -> None:
        super().__init__()
        self.value = value
        self.number = number
        self.text = f"{number}: {self.value: ,}"
        self.font = super().get_font(super().config.POINT_LIST_FONT_SIZE)
        self.font_safe_haven = super().get_font(super().config.POINT_LIST_FONT_SIZE_SAFE_HAVEN)
        self.font_color_active = super().config.PRIMARY_COLOR
        self.font_color_inactive = super().config.TERTIARY_COLOR
        self.position_topleft = position_topleft
        
        self.text_surface_active = self.font.render(self.text, 1, self.font_color_active)
        self.text_surface_inactive = self.font.render(self.text, 1, self.font_color_inactive)
        self.text_surface_safe_haven_active = self.font_safe_haven.render(self.text, 1, self.font_color_active)
        self.text_surface_safe_haven_inactive = self.font_safe_haven.render(self.text, 1, self.font_color_inactive)
        self.text_rect_active = self.text_surface_active.get_rect(topleft = position_topleft)
        self.text_rect_inactive = self.text_surface_inactive.get_rect(topleft = position_topleft)
        self.text_rect_safe_haven_active = self.text_surface_safe_haven_active.get_rect(topleft = position_topleft)
        self.text_rect_safe_haven_inactive = self.text_surface_safe_haven_inactive.get_rect(topleft = position_topleft)

    def __display(self, surface, rect) -> None:
        super().window.blit(surface, rect)

    def display_active(self) -> None:
        if self.number not in [5, 10 ,15]:
            self.__display(surface = self.text_surface_active, rect = self.text_rect_active)
        else:
            self.__display(surface = self.text_surface_safe_haven_active, rect = self.text_rect_safe_haven_active)

    def display_inactive(self) -> None:
        if self.number not in [5, 10, 15]:
            self.__display(surface = self.text_surface_inactive, rect = self.text_rect_inactive)
        else:
            self.__display(surface = self.text_surface_safe_haven_inactive, rect = self.text_rect_safe_haven_inactive)


    
