class Setting:
    DEBUG = 0

    if DEBUG:
        ACTION_FIELD_WIDTH = 7
        ACTION_FIELD_HEIGHT = 10
    else:
        ACTION_FIELD_WIDTH = 10
        ACTION_FIELD_HEIGHT = 10

    GUI_SCALE = 100

    SCREEN_WIDTH = ACTION_FIELD_WIDTH * GUI_SCALE
    SCREEN_HEIGHT = ACTION_FIELD_HEIGHT * GUI_SCALE
