# 2D Shooter [Alien Invaders](https://github.com/CHAMPION316/alien-invaders)

Taking inspiration from the classic 1978 [Space Invaders](https://en.wikipedia.org/wiki/Space_Invaders). This is a 2D shooter created in [python](https://www.python.org/) using [pygame](https://www.pygame.org/news). 

## Table of contents

- [Description](#1-description)
- [Gameplay](#2-gameplay)
- [Technologies used](#3-technologies-used)
- [Testing](#4-testing)
- [Improvements](#5-improvements)
- [Deployment](#6-deployment)
- [Credits](#7-credits)
- [Acknowledgments](#8-acknowledgments)

## 1 Description

The game is a very standard old school style 2D [fixed shooter](https://en.wikipedia.org/wiki/Shoot_%27em_up#Fixed_shooters) game in which the player uses directional inputs in order to manuever the space ship. 

### 1.1 Objective

The objective is to make it through as many levels as possible without dying but successfully eliminating your enemies. This will be accomplished by firing a laser that you will have at your disposal.

### 1.2 [Main Menu](readme-files/main-menu.jpg)

Upon loading the game you will be presented with a very simplistic main menu. You will be instructed to [**click**](readme-files/start-game.jpg) the mouse button in order to begin playing.

### 1.3 Style
The background is presented with the same image that you see in the main menu of the game which is the background of where the game takes place. I chose a font that would fit an alien invasion theme and came to the conclusion that [_**Showcard Gothic**_](readme-files/font-style.jpg) was the best option visually.

### 1.4 Wireframes
I used OneNote for the rough draft ideas to draw the ships, and background of this project. However Photoshop was where I created the acutal png images that you see in the game. 

- [Enemy Drawing](docs/img/enemy_roughdraft.jpg)
- [Enemy Final](docs/img/space_ship_creation.jpg)
- [Player Drawing](docs/img/user_ship.jpg)
- [Player Final](assets/raider_raptor.png)



## 2 Gameplay

[**Gameplay**](readme-files/game-play.jpg) requires the use of the [**WASD**](readme-files/move-input.jpg) keys to move horizontally and vertically. Using the [**spacebar key**](readme-files/space-shoot.jpg) fires the player's laser.

In the top left and right corners of the screen the player will be presented with the lives and level numbers that corresponds to them.
- [Game-Bar](readme-files/game-bar.jpg)

### 2.1 How to play the game

You will need to install the [pygame package](https://github.com/pygame/pygame):

Depending on the version of pip that you have installed. Try pip3 first, and if the command is not recognised, try with pip.

```sh
$ pip3 install pygame
$ pip install pygame
```

### 2.2 Lives

[**Lives-Level**](readme-files/lives-level.jpg)

Player begins game with 5 lives but can _lose_ them if:

- _If the player allows the enemey to reach the bottom of the screen._

### 2.3 Health Bar

The player maintains a health bar of 100% that decreases by 10% by either:

1. _Taking a laser hit from the enemy -10%_
2. _Collide with the enemy resulting in the enemies death and a -10% deduction to players health._

When the player loses all of his health he will lose the game even if he has a single life remaining.

- _Lives only count toward letting the enemy reach bottom screen not wiping out player's health bar._

### 2.4 Lasers

Lasers in this game have a [__cooldown__](readme-files/cooldown-shot.jpg) of 1 second before they can be fired again for both the player and the enemy.

- _Laser [**speed**](readme-files/laser-speed.jpg) is set to 5 for both player and enemy_

- Background and ships are PNG images designed by me using [Adobe Photoshop](https://www.adobe.com/products/photoshop.html)

    * [Laser_Image](readme-files/laser_green_0.jpg)
    * [Enemy_Space_Ship](readme-files/space_ship_creation.jpg)
    * [Player_Space_Ship](readme-files/player_creation.jpg)
- (The other colors were only saved as **PNG** format since all I had to do was change the color in the **PSD** format which is what photoshop uses for images.)

### 2.5 Collision Detection
Collision in the game accurs between two objects. 

* _Player and enemy objects_
* _Player and enemy Lasers_
    * _Vice versa_

### 2.6 Quitting

The game can be quit by clicking on the "X" button on top of the window or by losing the game entirely which is followed by a [**'You Died'**](readme-files/end-game.jpg) screen and a timer set for 3 seconds that brings you back to the main menu.

### Future features
* Player lost of 100% results in life lost and a reset of position on the screen to continue playing.
* Option after losing the game to quit or start a new game. 
* New level means enemies with more health.
* Upgrades to lasers to help combat those stronger enemies.

## 3 Technologies used

- [Visual Studio Code](https://code.visualstudio.com/download) - used to develop the website outside of Gitpod.
- [GitHub](https://github.com/) - used to host the project.
- [Python](https://www.python.org/) - used to run python on the computer. 
- [Python-Tutor](https://pythontutor.com/) - used to understand breakdown of code. 
- [Git Bash](https://git-scm.com/downloads) - used as the terminal window to upload to github.
- [Shell Prompt](https://en.wikibooks.org/wiki/Guide_to_Unix/Explanations/Shell_Prompt) - used in Visual Studio and out.
- [YouTube](https://www.youtube.com/) - used to learn about the code I was writing.
- [Adobe Photoshop](https://www.adobe.com/products/photoshop.html) - used to create the images for the game.
- [Pygame Documentation](https://www.pygame.org/news) - learn the documentation of python for pygame.
- [OneNote](https://www.microsoft.com/en-us/microsoft-365/onenote/digital-note-taking-app) - all my ideas and drawings
- [PEP8](http://pep8online.com/) - online code validator for python
- [Stackedit](https://stackedit.io/) - is a README.md helper 

## 4 Testing

-   The testing process was done on a separate file [TESING.md](TESTING.md)

## 5 Improvements
- Program the game so that losing health also count towards lives lost and reset of player position.
- Option to continue playing after death or quitting the game.

## 6 Deployment

**How to deploy the project**

This project is hosted in GitHub Pages

1. On the menu on the top of the project’s repository on GitHub select **Settings**.
2. Scroll down to the GitHub **Pages** section.
3. Inside that section, click on the drop-down menu under **Source** and select **Main Branch**.
4. The page refreshes automatically and the website is now deployed.
5. The link to the webpage is just in the GitHub **Pages** section down below.

Only one branch has been used for this project.

**To run the project locally**

To clone this project from GitHub:

1. Under the repository’s name, click **Clone or download**.
2. In the **Clone with hTTPS** section, copy the given URL.
3. In your IDE of choice, open **Git Bash**.
4. Change the current working directory to the location where you want the cloned directory to be made.
5. Type **git clone**, and then paste the URL copied from GitHub.
6. Press **enter** and the local clone will be created.

**Update on deployment**

Due to this being a pygame project it will not run on heroku. I spoke with student care and it was concluded that I will upload this project on replit instead.
- [replit](https://replit.com/) 

## 7 Credits

### 7.1 Content
 
- I would like to thank Tim from [_Tech with Tim_](https://www.youtube.com/c/TechWithTim) from YouTube because with the short time that I had after returning from an isolated ship with no internet that required me to postpone my course. I needed guidance and understanding for a language I was not able to practice since September of 2021. It wasn't until now about 1.5 weeks ago that I was finally home and able to begin this project. I will credit Tim with the code I have written which is also open for personal use and learning with a few adjustments as to how I prefer the game to be played and with the creation of my own PNG images.  

### 8 Acknowledgments

- The [Code Institute](https://codeinstitute.net/) team.
- [Stackoverflow](https://stackoverflow.com/) for having answers when I need them.
- [Google](https://google.com/) for being the best search engine in this day and age.
- My wife Emelie for being encouraging while I stressed getting this done.
- Tim from 'Tech with Tim' as I mentioned above.