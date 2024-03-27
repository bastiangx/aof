import SimpleGUICS2Pygame.simpleguics2pygame as sg
from config import CANVAS_WIDTH, CANVAS_HEIGHT


from user_input import Keyboard
from gameplay import Gameplay
from jukebox import Jukebox
from mouse import Mouse

# menus
from wasted_menu import WastedMenu
from main_menu import MainMenu
from splash import Splash
from guide import Guide
from title import Title

import sys

"""
Main app launcher
Loads the dependencies and launches the app
simplegui API calls
"""

# global input handlers
mouse = Mouse()
kbd = Keyboard()

# Game states
STATE_APP: bool = True   # app launcher/ always True unless quitting app

STATE_SPLASH = 0   # before everything
STATE_TITLE = 1   # after splash, before gameplay
STATE_MAIN_MENU = 2   # after launch, before gameplay, after game over
STATE_GUIDE = 3   # after main menu, before gameplay
STATE_GAMEPLAY = 4   # during gameplay
STATE_WASTED = 5   # after gameplay

STATE_EXITING = 6  # closing app

# flag variables
guide_shown = False

# start app at SPLASH
state = STATE_SPLASH

guide = Guide()
title = Title()
splash = Splash()
main_menu = MainMenu()
wasted = WastedMenu()
gameplay = Gameplay()

jukebox = Jukebox()


# state machine
def app_draw(canvas: object) -> state:
    global state, guide_shown

    # Splash screen
    if state == STATE_SPLASH:
        mouse.disable()
        splash.render(canvas)

        splash_event = splash.count_down()
        if splash_event == 'continue':
            state = STATE_TITLE
        else:
            state = STATE_SPLASH

    # Title screen
    if state == STATE_TITLE:
        # render title screen
        title.render(canvas)

        # if any click is detected, switch to the main menu
        title_event = title.handler(mouse)
        if title_event == 'continue':
            state = STATE_MAIN_MENU
            mouse.update()

        elif title_event == 'stay':
            state = STATE_TITLE

    # Main menu loop
    if state == STATE_MAIN_MENU:
        # Render main menu
        main_menu.render(canvas)
        main_menu_event = main_menu.handler(mouse)

        if main_menu_event == 'play':
            gameplay.reset()

            if not guide_shown:
                state = STATE_GUIDE
                guide_shown = True
            else:
                state = STATE_GAMEPLAY

        if main_menu_event == 'exit':
            app_quit()

    # Guide loop
    if state == STATE_GUIDE:
        guide.render(canvas)
        mouse.disable()

        guide_event = guide.count_down(canvas)
        if guide_event == 'continue':
            state = STATE_GAMEPLAY

    # Gameplay loop
    if state == STATE_GAMEPLAY:
        gameplay.render(canvas, kbd, mouse)

        game_event = gameplay.handler(mouse, canvas)
        if game_event == 'wasted':
            state = STATE_WASTED
            gameplay.reset()

        if game_event == 'main_menu':
            state = STATE_MAIN_MENU

        elif game_event == 'exit':
            app_quit()

    elif state == STATE_WASTED:
        wasted.render(canvas)
        gameplay.reset()

        wasted_event = wasted.handler(mouse)
        if wasted_event == 'play':
            state = STATE_GAMEPLAY

        if wasted_event == 'mm':
            state = STATE_MAIN_MENU

        if wasted_event == 'exit':
            app_quit()

    return state


# main launcher (simplegui API calls)
def main(kbd: object, mouse: object) -> None:
    frame = sg.create_frame('AoF', CANVAS_WIDTH, CANVAS_HEIGHT, 0)
    frame.set_draw_handler(app_draw)
    frame.set_canvas_background('black')

    jukebox.play()


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
