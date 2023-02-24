import pygame 

# Game imports
from game.data.components.component_togglable import ComponentTogglable

class AnswerOptionButton(ComponentTogglable):
    def __init__(
        self, image_path_enabled_state: str, 
        image_path_disabled_state: str, position_topleft: tuple,
        answer_option_text: str
    ) -> None:
        super().__init__(image_path_enabled_state, image_path_disabled_state, position_topleft)
        self.answer_option_text = answer_option_text
        self.answer_option_text_surface = (
            super().get_font(super().config.ANSWER_OPTION_TEXT_FONT_SIZE)
            .render(self.answer_option_text, 1, super().config.ANSWER_OPTION_TEXT_FONT_COLOR))
        self.answer_option_text_rect = self.answer_option_text_surface.get_rect()

    def display_component_enabled(self) -> None:
        super().display_component_enabled()
        self.answer_option_text_rect.center = self.rect_enabled_state.center
        super().window.blit(self.answer_option_text_surface, self.answer_option_text_rect)

    def display_component_disabled(self) -> None:
        super().display_component_disabled()
        self.answer_option_text_rect.center = self.rect_disabled_state.center
        super().window.blit(self.answer_option_text_surface, self.answer_option_text_rect)