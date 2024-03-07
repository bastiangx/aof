# Attack on Farm

py-simplegui shooter game inspired by space invaders. [Royal Holloway university Project]

###### this branch: **is_colliding**

#### Collision between Bullets, Zombies and Player
all the collision detection check and handling is done in collision.py file

**known issues:**

- possible bug in deleting instances of zombies when they are being hit by bullets and player at the same time 
	- possible solutions: 1. error handling, if x in list is empty, skip. 2. use flags to have collision between either bullet or player, not both at the same time 
- possible cache size leak in collisions class. needs to be automated to be cleared after a certain size or time 
- massive performance hindrance without the use of grids, or tree data structures for collision detection
- possible tunnelling of bullets through zombies if their sizes gets too small or speed too fast

<details>
<summary> How to Run the game file? </summary>

#### Running the game
To run the game, you need to have python installed on your machine. You can download python from [here](https://www.python.org/downloads/). Once you have python installed, you can run the game by running the following command in the terminal.

```bash
python3 game.py
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
