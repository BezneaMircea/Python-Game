## <span style="color: gray;">Authors</span>

- **Names:** [Mircea-Andrei Beznea](https://www.instagram.com/mircea.wpp/) and [Stefan Ghenescu](https://www.instagram.com/stefan.ghenescu/)
- **GitHub Profiles:** [@BezneaMircea](https://github.com/BezneaMircea) [@stefanghenescu](https://github.com/stefanghenescu)
- **Emails:**  
  >[bezneamirceaandrei21@gmail.com]()  
[stefan.ghenescu2005@gmail.com ]()
- **Date:** [7 January, 2024]()  
# AIR HOCKEY PROJECT [airhockey](https://github.com/BezneaMircea/Python-Game)
  

## Introduction:  
This is an air hockey game that also has multiple configuration menus such as a  
main menu, a game settings menu and menus for player one, player two. After  
configuring the game you can enter the actual game with the selected settings  
by pressing the PLAY button.  
    

## Packaging:

The sourse code can be found in the src directory. The starting point of the  
program can be found in the **StartGame.py** file.

### src:  
> * **game package** -> the source code for the actual game logic
> * **menus package** -> the source code for the cofiguration menus logic
> * **utils** -> package containing constans/pictures/music and most importantly  
two util classes **RectButton**, **TextButton**

## How to use:

## Windows (PowerShell, CommandPromt):
The repo includes a **Makefile**. That is written so that the the game can be  
played on **WINDOWS**.
Assuming you have python and make insatalled simply run:  
>**make install**  
>**make run**   

In case you dont have **make** installed you can do so by running as administrator in CLI:  
> Set-ExecutionPolicy Bypass -Scope Process -Force; `
[System.Net.ServicePointManager]::SecurityProtocol = `
[System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))  

After that you can use:  
>choco install make

and you should be all set.  
Run **make help** to see all the makefile commands.

## Linux (Bash):

You can run the following commands to download the dependencies:
> sudo apt-get install python3-pip  
  python3 -m pip install pygame  
  python3 -m pip install numpy

At last just run from the **src** directory **python3 StartGame.py** and have fun!

## Contribution:

### Stefan's part

#### ***Gameplay Mechanics***:

1. *Game Flow Management:*
   - Designed the **main game loop** from where all functionalities are called. 
   - Added a system for updating and **displaying the score** in real-time.
   - Implemented logic that **ends the game** based on the score, ensuring the winner is displayed.
   - Added functionality for **sudden death mode**, a tie-breaking state where the first player to score wins.

2. *Puck Mechanics:*
   - Developed logic for the **puck’s movement** with boundary restrictions and collisions with paddles or table walls.
   - Added mechanisms to detect a **goal**, resetting the puck’s position appropriately.

3. *Paddle Mechanics:*
   - Programmed paddle controls, with each player having unique keys from the keyboard. Paddles remain within their permitted area of play and interact with the puck.
   - Ensured collision detection between paddles and the puck, changing it's direction.

#### ***Player Menu Enhancements***:

*Name Input Box:*
   - Created an interactive **text input field** for players to set their in-game names. This includes support for keyboard input and a character limit to ensure consistent display during gameplay.
   - Designed a blinking **cursor system** for visual feedback while the name box is active.

#### ***Challenges Faced***:

- **Puck Physics and Collisions**: Developing realistic physics for puck movement, particularly ensuring proper collision detection between paddles and walls, was a tricky task. We had to fine-tune collision detection to avoid the puck "glitching" at fast speeds or staying stuck on edges.

- **Name Box for player name Integration**: Blinking cursor implementation was challenging, as we had to ensure the cursor was displayed correctly and synchronized with the player's input. The position of the cursor had to be updated dynamically based on the player's input especially when the player deleted characters.

---

### Mircea's part

#### ***Menu Design and Components***:

1. *Menu System Development:*
   - Developed the **menus package**, which handles the logic of multiple game menus, including the main menu, settings menu and specific player menus.
   - Implemented essential components in **utils** package, such as **RectButton** and **TextButton**, where:
     - **RectButton** supports both images and text, used for interactive buttons throughout the game menus.
     - **TextButton** is a simpler button that contains just text, suitable for various menu options.
   - Created several configuration menus:
     - **Main Menu** to start the game or access settings.
     - **Game Settings Menu** to customize the gameplay environment.
     - **Player Settings Menus** to define players’ preferences and configurations.

2. *Game Settings Features:*
   - Integrated **swipe buttons** for customizing game options, such as:
     - Selecting the map to play on, allowing players to pick different tables for their game.
     - Selecting the paddles, giving players an option to choose between different paddles.

3. *In-Game Countdown and Timer:*
   - Designed and implemented a **countdown timer** displayed at the beginning of the game.
   - Developed a **real-time game timer** visible during the match, which dynamically updates to show the current game time.
   - Introduced a **red alert system** where the last 30 seconds of the game are displayed in red.

4. *Settings Menu Features:*
   - Built two **control bars** in the settings menu:
     - **Match Duration**, to control the length of the game, allowing players to adjust the game time to their preference.
     - **Music Volume**, enabling players to set the volume of the song played during the game.

#### ***Challenges Faced***:

- **Refactoring Game Logic**: At one point, we attempted to decouple the game logic into more modular classes, which required a significant refactor of the existing code. This restructuring process posed challenges as we needed to ensure that the refactored classes would integrate smoothly and function correctly across different parts of the game.

- **Utility Classes Implementation**: Initially, the process of working without utility classes like **RectButton** and **TextButton** was more difficult. Once these classes were implemented, they simplify many areas of the code. These utility classes helped remove redundant code and provided a cleaner architecture for handling menus and buttons.