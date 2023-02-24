import pygame

# Game imports
from game.data.surface import Surface

class Button(Surface):
    def __init__(
        self, text: str, font_size: int, 
        text_color, button_color, border_color = None,
        button_rect_center: int = None,
        button_border: int = 5
    ) -> None:

        super().__init__()
        self.text = text
        self.font_size = font_size
        self.text_color = text_color
        self.button_color = button_color
        self.border_color = border_color if border_color is not None else button_color
        self.button_border = button_border

        if button_rect_center is None:
            self.button_rect_center = button_rect_center
        else:
            self.button_rect_center = (super().window.get_width() // 2, super().window.get_height() // 2)
            
        self.button_text = super().get_font(self.font_size).render(self.text, 1, self.text_color)
        self.button_rect = self.button_text.get_rect(center = self.button_rect_center)
        self.button_base = pygame.Rect(
            self.button_rect.left - (self.button_border / 2),
            self.button_rect.top - (self.button_border / 2),
            self.button_rect.width + self.button_border,
            self.button_rect.height + self.button_border, )


    def __draw_button_text(self) -> None:
        super().window.blit(self.button_text, self.button_rect)

    def __draw_button_main(self) -> None:
        pygame.draw.rect(super().window, self.button_color, self.button_rect)

    def __draw_button_base(self) -> None:
        pygame.draw.rect(super().window, self.border_color, self.button_base)

    def draw_button(self) -> None:
        self.__draw_button_base()
        self.__draw_button_main()
        self.__draw_button_text()
        pygame.display.update()
