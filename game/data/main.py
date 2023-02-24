import pygame

# Game imports
from game.data.surface import Surface
from game.data.components.component import Component
from game.data.components.component_togglable import ComponentTogglable
from game.data.components.point_text_togglable import PointTextTogglable
from game.data.components.answer_option_button import AnswerOptionButton
from game.data.components.question_box import QuestionBox

class Main(Surface):
    def __init__(self) -> None:
        super().__init__()

        self.point_list = super().config.POINT_LIST

        self.questionbox = QuestionBox(
            question_text = "asdasdasdasdasdsadasdasdsakdfnaksdjnfaksldnfa",
            image_path = super().config.UI_MAIN_QUESTIONBOX_IMAGE_PATH,
            position_topleft = (70, 340), )

        self.player_profile = Component(
            image_path = super().config.UI_MAIN_PLAYER_PROFILE_IMAGE_PATH,
            position_topleft = (46, 40), )

        self.pause_button = Component(
            image_path = super().config.UI_MAIN_PAUSE_BUTTON_IMAGE_PATH,
            position_topleft = (615, 40), )

        self.game_title = Component(
            image_path = super().config.UI_MAIN_GAME_TITLE_IMAGE_PATH,
            position_topleft = (120, 165), )

        self.answerbox_1 = AnswerOptionButton(
            answer_option_text = "",
            image_path_enabled_state = super().config.UI_MAIN_ANSWER_OPTION_BUTTON_1_ENABLED_IMAGE_PATH,
            image_path_disabled_state = super().config.UI_MAIN_ANSWER_OPTION_BUTTON_1_DISABLED_IMAGE_PATH,
            position_topleft = (45, 445), )

        self.answerbox_2 = AnswerOptionButton(
            answer_option_text = "",
            image_path_enabled_state = super().config.UI_MAIN_ANSWER_OPTION_BUTTON_2_ENABLED_IMAGE_PATH,
            image_path_disabled_state = super().config.UI_MAIN_ANSWER_OPTION_BUTTON_2_DISABLED_IMAGE_PATH,
            position_topleft = (405, 445), )

        self.answerbox_3 = AnswerOptionButton(
            answer_option_text = "",
            image_path_enabled_state = super().config.UI_MAIN_ANSWER_OPTION_BUTTON_3_ENABLED_IMAGE_PATH,
            image_path_disabled_state = super().config.UI_MAIN_ANSWER_OPTION_BUTTON_3_DISABLED_IMAGE_PATH,
            position_topleft = (70, 495), )

        self.answerbox_4 = AnswerOptionButton(
            answer_option_text = "",
            image_path_enabled_state = super().config.UI_MAIN_ANSWER_OPTION_BUTTON_4_ENABLED_IMAGE_PATH,
            image_path_disabled_state = super().config.UI_MAIN_ANSWER_OPTION_BUTTON_4_DISABLED_IMAGE_PATH,
            position_topleft = (380, 495), )

        self.skill_1 = ComponentTogglable(
            image_path_enabled_state = super().config.UI_MAIN_SKILL_1_ENABLED_IMAGE_PATH,
            image_path_disabled_state = super().config.UI_MAIN_SKILL_1_DISABLED_IMAGE_PATH,
            position_topleft = (233, 288), )

        self.skill_2 = ComponentTogglable(
            image_path_enabled_state = super().config.UI_MAIN_SKILL_2_ENABLED_IMAGE_PATH,
            image_path_disabled_state = super().config.UI_MAIN_SKILL_2_DISABLED_IMAGE_PATH,
            position_topleft = (233 + 100, 288), )

        self.skill_3 = ComponentTogglable(
            image_path_enabled_state = super().config.UI_MAIN_SKILL_3_ENABLED_IMAGE_PATH,
            image_path_disabled_state = super().config.UI_MAIN_SKILL_3_DISABLED_IMAGE_PATH,
            position_topleft = (233 + 200, 288), )

        self.point_text_togglable_list = []
        self.__point_text_list_to_point_text_togglable_list_reversed()

        self.component_list = [
            self.questionbox, self.player_profile, self.pause_button, 
            self.game_title, ]

        self.component_togglable_list = [
            self.answerbox_1, self.answerbox_2, self.answerbox_3, 
            self.answerbox_4, self.skill_1, self.skill_2, self.skill_3]

    def display_initial_components(self) -> None:
        for component in self.component_list:
            component.display_component()

        for component in self.component_togglable_list:
            component.display_component_enabled()

        for point_text_togglable in self.point_text_togglable_list:
            point_text_togglable.display_inactive()

    def display_test_text(self, position_topleft: tuple) -> None:
        rect = self.test_text_surface.get_rect(topleft = position_topleft)
        super().window.blit(self.test_text_surface, rect)

    def __point_text_list_to_point_text_togglable_list(self) -> None:
        x_pos, y_pos_last = 770, 40, 
        y_pos_increment, y_pos_increment_sh = 30, 40

        for number, value in enumerate(self.point_list):
            number += 1
            _y_pos_increment = y_pos_increment if number not in [4, 5, 9, 10, 14, 15] else y_pos_increment_sh
            self.point_text_togglable_list.append(
                PointTextTogglable(value = value, number = number, position_topleft = (x_pos, y_pos_last)))
            y_pos_last += _y_pos_increment

    def __point_text_list_to_point_text_togglable_list_reversed(self) -> None:
        x_pos, y_pos_last = 770, 40, 
        y_pos_increment, y_pos_increment_sh = 30, 40
        number = 0
        numbers = [x for x in range(1, len(self.point_list)+1)[::-1]]
        for value in self.point_list[::-1]:
            _y_pos_increment = y_pos_increment if numbers[number] not in [5, 6, 10, 11, 15] else y_pos_increment_sh
            self.point_text_togglable_list.append(
                PointTextTogglable(value = value, number = numbers[number], position_topleft = (x_pos, y_pos_last)))
            y_pos_last += _y_pos_increment
            number += 1
    