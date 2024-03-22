import SimpleGUICS2Pygame.simpleguics2pygame as sg

from config import CANVAS_WIDTH, CANVAS_HEIGHT

from user_input import Keyboard
from gameplay import Gameplay
from mouse import Mouse

from main_menu import MainMenu
import sys

"""
Main app launcher
Loads the dependencies and launches the app
simplegui API calls
"""

# global input handlers
mouse = Mouse()
kbd = Keyboard()

# global instances
main_menu = MainMenu()
gameplay = Gameplay()

# Game states
STATE_APP: bool = True   # app launcher/ always True unless quitting app
STATE_MAIN_MENU = 1   # after launch, before gameplay, after game over
STATE_GAMEPLAY = 2   # during gameplay
STATE_PAUSED = 3   # during gameplay, after pause button is clicked
STATE_GAME_OVER = 4   # after gameplay

# flag variables
game_reset = False

# always start at the main menu
state = STATE_MAIN_MENU

# state machine
def app_draw(canvas: object) -> None:
    global state, game_reset
    # Main menu loop
    if state == STATE_MAIN_MENU:

        # Render main menu
        main_menu.render(canvas)

        # if play is clicked, switch to the gameplay
        main_menu_event = main_menu.handler(mouse)
        if main_menu_event == 'play':
            state = STATE_GAMEPLAY
            game_reset = True

        if main_menu_event == 'exit':
            app_quit()

    # Gameplay loop
    elif state == STATE_GAMEPLAY:
        gameplay.render(canvas, kbd, mouse)


# flags reset
if game_reset:
    gameplay.reset()
    game_reset = False

# main launcher (simplegui API calls)
def main(kbd: object, mouse: object) -> None:
    frame = sg.create_frame('AoF', CANVAS_WIDTH, CANVAS_HEIGHT, 0)
    frame.set_draw_handler(app_draw)
    frame.set_canvas_background('rgba(38, 64, 69, 1)')

    frame.set_keydown_handler(kbd.keydown)
    frame.set_keyup_handler(kbd.keyup)
    frame.set_mouseclick_handler(mouse.click_handler)
    frame.start()


def app_quit() -> None:
    global STATE_APP
    print('Thanks for playing AoF!')
    STATE_APP = False
    sys.exit()


# main loop (simplegui API calls)
while STATE_APP:
    main(kbd, mouse)

    # close app/ break loop
    app_quit()
    break
