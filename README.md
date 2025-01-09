# KAMILA CAREER

## Description

KAMILA CAREER is a simple 2D platformer game built using Pygame. The player controls a character that needs to jump between platforms to gain score. The game features dynamic platform generation, sound effects, and a score system. The game ends if the player falls off the screen, and it displays the current and best scores along with a restart option.

## Features

* **Classic Platformer Gameplay:** Jump between platforms to reach higher scores.
* **Dynamic Platform Generation:** New platforms are generated as the player progresses.
* **Score Tracking:**  Keep track of your current score and the best score achieved.
* **Sound Effects:** Includes jump and fall sound effects to enhance the gaming experience.
* **Background Music:**  Immersive background music plays throughout the game.
* **Restart Functionality:** Easily restart the game after losing.
* **Responsive Controls:**  Smooth player movement and jumping mechanics.
* **Game Over Screen:** Displays the score and a restart button when the player loses.
* **Win Screen:**  Appears when the player achieves a new best score.

## How to Run

1. **Prerequisites:**
   - Ensure you have Python installed on your system.
   - Install the Pygame library. You can install it using pip:
     ```bash
     pip install pygame
     ```

2. **Download the Game Files:**
   - Save all the provided Python code (likely in a file named something like `main.py`) and the `images` and `sounds` folders in the same directory. Make sure the folder structure looks like this:

     ```
     your_game_directory/
         main.py
         images/
             bg.png
             front.png
             left.png
             lose.jpg
             money.png
             restart.png
             right.png
             scream.png
             win.jpg
         sounds/
             dummy.mp3
             jump1.wav
             jump2.wav
             scream.wav
         fonts/
             Pillowtalk.otf
     ```

3. **Run the Game:**
   - Open a terminal or command prompt.
   - Navigate to the directory where you saved the game files.
   - Execute the following command:
     ```bash
     python main.py
     ```
     (Replace `main.py` with the actual name of your Python file if it's different).

## Game Controls

* **Left Arrow Key:** Move the player to the left.
* **Right Arrow Key:** Move the player to the right.
* **Spacebar:** Make the player jump.

## Dependencies

* **Pygame:**  A free and open-source cross-platform library for the creation of multimedia applications like video games.

## Assets

The game utilizes the following assets:

* **Images:**
    * `images/bg.png`: Background image.
    * `images/front.png`: Player sprite (facing forward).
    * `images/left.png`: Player sprite (moving left).
    * `images/lose.jpg`: Game over screen image.
    * `images/money.png`: Platform image.
    * `images/restart.png`: Restart button image.
    * `images/right.png`: Player sprite (moving right).
    * `images/scream.png`: Player sprite (falling).
    * `images/win.jpg`: Win screen image.
* **Sounds:**
    * `sounds/dummy.mp3`: Background music.
    * `sounds/jump1.wav`, `sounds/jump2.wav`: Jump sound effects.
    * `sounds/scream.wav`: Fall sound effect.
* **Font:**
    * `fonts/Pillowtalk.otf`: Font used for text display.

**Make sure these assets are present in the `images`, `sounds`, and `fonts` folders respectively, within the same directory as your Python script.**

## Potential Improvements

* **More Varied Platform Design:** Introduce different types of platforms with varying sizes or behaviors.
* **Power-ups:** Add power-ups that could grant the player temporary abilities like double jump or invincibility.
* **Enemy Characters:** Introduce enemies to avoid, adding a challenge to the gameplay.
* **Level Design:** Create specific level layouts instead of purely random platform generation.
* **Visual Enhancements:** Improve the visual appeal with more detailed backgrounds, animations, and particle effects.
* **Leaderboard:** Implement a system to store and display high scores.
* **Pause Functionality:** Allow the player to pause the game.

Enjoy playing KAMILA CAREER!
