<p align="center">
  <img
    width="552"
    src="/assets/logo/title-logo.png"
    alt="AoF, Top-down shooter game written in Python."
  />
</p>



 <p align="center">
     SimpleGUICS2Pygame-based game written in Python.<br />
     Fun top-down shooter with simple graphics and gameplay.<br />
</p>

<p align="center">
    <sup>Latest version: Beta</sup>
</p>

## 🐍 Getting Started

### Prerequisites

- ##### Python3

  You need Python3 to run this game at this point.

<details>
<summary>Windows</summary>
Visit [here](https://www.python.org/downloads/windows/) and download the latest version of Python3.
Follow the full instructions.
</details>

<details>
<summary>macOS</summary>
Visit [here](https://www.python.org/downloads/mac-osx/) and download the latest version of Python3.
Follow the full instructions.
</details>

<details>
<summary>Ubuntu</summary>

```bash
sudo apt update
sudo apt install python3
```
</details>

<details>
<summary>Others</summary>
Visit [here](https://www.python.org/downloads/) and download the latest version of Python3.
Follow the full instructions.
</details>

- ##### SimpleGUICS2Pygame

  This game uses SimpleGUICS2Pygame as its API for graphics and input.
  You can simply install it by running the following command:

```bash
pip install SimpleGUICS2Pygame
```

or

```bash
pip3 install SimpleGUICS2Pygame
```

or if you have downloaded the repository, you can install all the requirements by running:

```bash
# in the root dir of the repo
pip install -r requirements.txt
```

if none of the above solutions works, visit [here](https://pypi.org/project/SimpleGUICS2Pygame/) and follow the instructions for your OS.

---

## 👾 Running the game

Navigate to the root directory of the repository and run the following command in your terminal:

```bash
python app.py
```

or

```bash
# if python3 installed
python3 app.py
```

The directory structure should look like this:

```markdown
.
├── README.md
├── app.py
├── requirements.txt
├── ...
└── assets/
   ├── sprite/
   ├── audio/
   └── ...
```

**`app.py` is the main file that runs the game.** - has the main game loop -> simplegui API calls - has the main state machine

---

## 🎮 Controls

#### Movement

- `W` or `↑` | Move up
- `A` or `←` | Move left
- `S` or `↓` | Move down
- `D` or `→` | Move right

#### Shooting

- `mouse left click` | Shoot

---

## 🌲 Structure

```markdown
.
├── app.py -> main loop / state machine
├── assets.py -> loads all assets into memory
├── bullet.py -> bullet rendering and movement
├── collision.py -> collision detection for all entities
├── config.py -> game configuration and constants
├── enemies.py -> enemy rendering and movement
├── factory.py -> entity factory / continuous entity generation
├── gameplay.py -> main gameplay loop and logic / calls all relevant class instances
├── guide.py -> player guide / instructions before starting the game
├── jukebox.py -> audio player / plays background music and sound effects
├── main_menu.py -> main menu / game start screen
├── mouse.py -> mouse click handler
├── pause_menu.py -> renders pause menu
├── player.py -> player rendering and movement
├── score.py -> score rendering and updating
├── shoot.py -> player shooting mechanism and cooldown
├── splash.py -> splash screen / opening screen
├── title.py -> game title / game name
├── user_input.py -> keyboard input handler
├── vector.py -> utility class for vector operations
├── wasted_menu.py -> renders game over screen
├
├── assets/ -> all game assets
  ├── sprite/
  ├── audio/
  └── ...
```
---
## 🐞 Known Issues

The SimpleGUICS2Pygame API is a buggy and outdated/unspported repo, causing some issues with the game. The game may not run as expected on some systems.
These issues are mostly related to the API itself and not the game code.
Some of the bugs cannot be patched since our project requirements prohibit us from using other APIs.

#### ‼️ Audio Device

The API requires an audio device to be present on the system. If the system does not have an audio device, the game will not run.
This does **not** mean that the system has to be unmuted; it just needs to have an audio device present.

#### Sounds and Music

- Rapidly shooting will not play the sound effect upon clicking.
- The background music stops playing after a while.
- Any sound effect being played gets in a queue and will not play simultaneously with other sounds.

**Planned solution:** Alternative audio API

#### Graphics

- The scaling system is somewhat random and broken; depending on the system, the game may not scale properly. **Unpatchable**
- Resizing the game window is not supported. **Unpatchable**

---

#### Binary Distribution

The `.exe` file will be available soon.

---

## 📝 License

This project is for demonstration purposes only and is not licensed for commercial use or any distribution.

## 🎉 Acknowledgements

My amazing team members who made coding this game a fun experience:

- [Jasmin](https://github.com/jasmin192004)
- [Imran](https://github.com/imranslab12)
- [Sienna](https://github.com/siennadarya)
````
