# Attack on Farm

###### this branch: **has_loops**
---

## New: App (State Machine)
The game is now booted from 'app.py' file instead of game.py. The app file is responsible for managing the game states and the game loop.
#### State Machine
inside of app, the state machine manages switching between the main_menu, gameplay, etc.
It is responsible to make new instances of game upon reset and render it.

####  main while loop
the simplegui draw calss and everything else is now inside a main while loop. if while loop chain is broken, the game exits.

---

## New: Menus (main-menu, pause-menu)
#### MainMenu
is always the first state of the game. it is responsible for showing the game title and the start button. it also has a quit button to exit the game.
its a copy of PauseMenu except the buttons here are lowered and are smaller.

#### PauseMenu
pauses all movement of entities, calls the buttons, renders them and darkens the background. it also has a quit button to exit the game.
Handles click buttons to either resume or quit the game.

---

## Refactored: Gameplay
game.py and levels.py are no more

#### Render:
handles rendering and interaction of all entities in the game.

---
## Added: Score display (skeleton)
Super skeleton of showing current score on top right of screen.
functional yet needs to be improved.

---

### How to run the game now?
simply instead of running game.py, run app.py
```bash
python3 app.py
```
or 
```bash
python app.py
```

<details>
<summary> How to Run the game file </summary>

#### Running the game

To run the game, you need to have python installed on your machine. You can download python from [here](https://www.python.org/downloads/). Once you have python installed, you can run the game by running the following command in the terminal.

```bash
python3 app.py
```

#### Any dependencies?

Yes, The game uses the simplegui library. An older version to be exact. You can install it by running the following command in the terminal.
All other dependencies as of 5 March, 2024 are included in the standard python3 library.

if you are using **python 3.x**

```bash
pip3 install SimpleGUICS2Pygame
```

if you are using **python 2.x**

```bash
pip install SimpleGUICS2Pygame
```

#### What is sg in the code?

**sg** is an alias for the simplegui library. It is used to make the code more readable and easier to write. You can find the alias at the top of the game.py file.
it is defined as follows:

```python
from SimpleGUICS2Pygame import simpleguics2pygame as sg
```

#### Where is the binary (.exe)?

The game is unfinished and is still in development. There is no binary available for the game yet.

</details>
