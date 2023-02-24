import os

class Config():
    WINDOW_HEIGHT = 1024
    WINDOW_WIDTH = 576
    WINDOW = (WINDOW_HEIGHT, WINDOW_WIDTH)

    ASSETS_IMAGE_MAIN_PATH = 'game/data/assets/image/main'
    ASSETS_FONT_PATH = 'game/data/assets/font'
    ASSETS_CSV_PATH = 'game/data/assets/csv'

    PRIMARY_COLOR = '#101527'
    SECONDARY_COLOR = '#191919'
    TERTIARY_COLOR = '#47506b'
    
    FONT_STYLE_PATH = os.path.join(ASSETS_FONT_PATH, 'MinimalPixel v2.ttf')

    QUESTION_ANSWER_CSV_PATH = os.path.join(ASSETS_CSV_PATH, 'dummy.csv')

    UI_MAIN_PLAYER_PROFILE_IMAGE_PATH = os.path.join(ASSETS_IMAGE_MAIN_PATH, 'player_profile.png')
    UI_MAIN_PAUSE_BUTTON_IMAGE_PATH = os.path.join(ASSETS_IMAGE_MAIN_PATH, 'pause_button.png')
    UI_MAIN_QUESTIONBOX_IMAGE_PATH = os.path.join(ASSETS_IMAGE_MAIN_PATH, 'questionbox.png')
    UI_MAIN_GAME_TITLE_IMAGE_PATH = os.path.join(ASSETS_IMAGE_MAIN_PATH, 'game_title.png')

    UI_MAIN_ANSWER_OPTION_BUTTON_1_ENABLED_IMAGE_PATH = os.path.join(ASSETS_IMAGE_MAIN_PATH, 'answer_option_button_1_enabled.png')
    UI_MAIN_ANSWER_OPTION_BUTTON_2_ENABLED_IMAGE_PATH = os.path.join(ASSETS_IMAGE_MAIN_PATH, 'answer_option_button_2_enabled.png')
    UI_MAIN_ANSWER_OPTION_BUTTON_3_ENABLED_IMAGE_PATH = os.path.join(ASSETS_IMAGE_MAIN_PATH, 'answer_option_button_3_enabled.png')
    UI_MAIN_ANSWER_OPTION_BUTTON_4_ENABLED_IMAGE_PATH = os.path.join(ASSETS_IMAGE_MAIN_PATH, 'answer_option_button_4_enabled.png')
    UI_MAIN_ANSWER_OPTION_BUTTON_1_DISABLED_IMAGE_PATH = os.path.join(ASSETS_IMAGE_MAIN_PATH, 'answer_option_button_1_disabled.png')
    UI_MAIN_ANSWER_OPTION_BUTTON_2_DISABLED_IMAGE_PATH = os.path.join(ASSETS_IMAGE_MAIN_PATH, 'answer_option_button_2_disabled.png')
    UI_MAIN_ANSWER_OPTION_BUTTON_3_DISABLED_IMAGE_PATH = os.path.join(ASSETS_IMAGE_MAIN_PATH, 'answer_option_button_3_disabled.png')
    UI_MAIN_ANSWER_OPTION_BUTTON_4_DISABLED_IMAGE_PATH = os.path.join(ASSETS_IMAGE_MAIN_PATH, 'answer_option_button_4_disabled.png')

    UI_MAIN_SKILL_1_ENABLED_IMAGE_PATH = os.path.join(ASSETS_IMAGE_MAIN_PATH, 'skill_1_enabled.png')
    UI_MAIN_SKILL_2_ENABLED_IMAGE_PATH = os.path.join(ASSETS_IMAGE_MAIN_PATH, 'skill_2_enabled.png')
    UI_MAIN_SKILL_3_ENABLED_IMAGE_PATH = os.path.join(ASSETS_IMAGE_MAIN_PATH, 'skill_3_enabled.png')
    UI_MAIN_SKILL_1_DISABLED_IMAGE_PATH = os.path.join(ASSETS_IMAGE_MAIN_PATH, 'skill_1_disabled.png')
    UI_MAIN_SKILL_2_DISABLED_IMAGE_PATH = os.path.join(ASSETS_IMAGE_MAIN_PATH, 'skill_2_disabled.png')
    UI_MAIN_SKILL_3_DISABLED_IMAGE_PATH = os.path.join(ASSETS_IMAGE_MAIN_PATH, 'skill_3_disabled.png')

    POINT_LIST_FONT_SIZE = 20
    POINT_LIST_FONT_SIZE_SAFE_HAVEN = 25
    POINT_LIST = [
        100, 200, 300, 500, 1_000, 2_000, 
        4_000, 8_000, 16_000, 25_000, 50_000, 
        100_000, 250_000, 500_000, 1_000_000]

    ANSWER_OPTION_TEXT_FONT_SIZE = 15
    ANSWER_OPTION_TEXT_FONT_COLOR = '#ffffff'
    QUESTION_TEXT_FONT_SIZE = 20
    QUESTION_TEXT_FONT_COLOR = PRIMARY_COLOR

    mockup = os.path.join('look', 'Artboard_1.png')