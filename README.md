## <span style="color: gray;">Authors</span>

- **Names:** [Mircea-Andrei Beznea](https://www.instagram.com/mircea.wpp/) and [Stefan Ghenescu](https://www.instagram.com/stefan.ghenescu/)
- **GitHub Profiles:** [@BezneaMircea](https://github.com/BezneaMircea) [@stefanghenescu](https://github.com/stefanghenescu)
- **Emails:**  
  >[bezneamirceaandrei21@gmail.com]()  
[Stefan.ghenescu2005@gmail.com ]()
- **Date:** [January, 07, 2024]()  
# AIR HOCKEY PROJECT [airhockey](https://github.com/BezneaMircea/Python-Game)
  

## Introduction:  
This is an air hockey game that also has multiple configuration menus such as a  
main menu, a game settings menu, and menus for player one, player two. After  
configuring the game you can enter the actual game with the selected settings  
by pressing the PLAY button.  
    

## Packaging:

The sourse code can be found in the src directory. The starting point of the  
program can be found in the **StartGame.py** file.

### src:  
> * **game package** -> the source code for the actual game logic
> * **menus package** -> the source code for the cofiguration menus logic
> * **utils** -> package containing constans/pictures/music and most importantly  
two util classes **RectButton** representing a default button having a picture and   
can also include a text and **TextButton** just a text button, no picture

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
Run **makefile help** to see all the makefile commands.

## Linux (Bash):

You can run the following commands to download the dependencies:
> sudo apt-get install python3-pip  
  python3 -m pip install pygame  
  python3 -m pip install numpy

At last just run from the **src** directory python3 StartGame.py and have fun!

## Contribution:

### TODO for gheni pls :).  
PS: La final baga si o poza din aia frumoasa cu noi :)