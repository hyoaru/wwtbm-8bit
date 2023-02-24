import pygame

# Game imports
from game.data.components.component import Component

class QuestionBox(Component):
    def __init__(self, image_path: str, position_topleft: tuple, question_text: str) -> None:
        super().__init__(image_path, position_topleft)
        self.question_text = question_text
        self.question_text_surface = (
            super().get_font(super().config.QUESTION_TEXT_FONT_SIZE)
            .render(self.question_text, 1, super().config.QUESTION_TEXT_FONT_COLOR))
        self.question_text_rect = self.question_text_surface.get_rect()

    def display_component(self) -> None:
        super().display_component()
        self.question_text_rect.center = self.rect.center
        super().window.blit(self.question_text_surface, self.question_text_rect)