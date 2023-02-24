import pygame
pygame.init()

# Game imports
from game.data.surface import Surface
from game.data.components.button import Button
from game.data.main import Main

surface = Surface()
main = Main()
test_button = Button(
    text = "test", font_size = 30, text_color = "White",
    button_color = "Black", button_rect_center = (25, 250),
    button_border = 10)

def run_game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                print(event.pos)

        surface.fill_window('#ffffff')
        # surface.fill_background()
        main.display_initial_components()
        pygame.display.update()
        


