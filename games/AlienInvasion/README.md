In the "**Alien Invasion**" game, players take control of a spaceship positioned at the bottom center of the screen. 
They can navigate the ship left and right using the arrow keys and fire bullets using the spacebar. The game 
starts with a fleet of aliens filling the sky, moving horizontally and descending down the screen. The player's 
objective is to shoot and destroy these aliens. If all the aliens are eliminated, a new, faster fleet replaces the 
previous one. However, if any alien collides with the player's ship or reaches the bottom of the screen, the player 
loses one of their ships. If the player loses all three ships, the game ends.

Here's a breakdown of the key components of the game:

- **alien.py:** This file defines the Alien class. The Alien class has an __init__ method inheriting from the Sprite 
class, which sets its initial position on the screen and loads the alien image. The **blitme()** method is responsible 
for drawing aliens on the screen. The image of the alien is stored in **ufo.bmp**, located in the images folder. 
Additionally, this file contains a **check_edges()** function to manage alien boundaries on the screen and an 
**update()** function to move aliens left and right.

- **alien_invasion.py:** The main file, **alien_invasion.py**, creates essential game objects such as **ai_settings** 
to store settings, **screen** for the main display surface, and initializes a **ship** instance. This file also houses 
the main game loop, implemented as a **while** loop. Within this loop, various functions are called, including 
**check_events()**, which handles keyboard input, ship updates (**ship.update()**), bullet updates 
(**update_bullets()**), and alien updates(**update_aliens()**). Finally, it updates the screen with the latest 
changes using **update_screen()**.

- **bullet.py:** The **bullet.py** file defines the Bullet class. This class has an __init__ method for creating 
bullets at the ship's position. The file also contains an **update()** function to manage bullet speed and position, 
along with a**draw_bullet()** function for drawing bullets on the screen.

- **button.py:** In this file, you'll find the Button class. The Button class has an __init__() method for defining 
button dimensions and properties, centering the button on the screen. It also contains a **prep_msg()** function for 
rendering images and text on the screen and a **draw_button()** function to display the button.

- **game_functions.py:** The **game_functions.py** file contains various functions that perform essential game tasks. 
The **check_events()** function detects relevant events such as keypresses and releases, and it processes these events 
using helper functions like **check_keydown_events()** and **check_keyup_events()**. These functions manage ship 
movement in the game. Additionally, the module contains **update_screen()**, responsible for redrawing the screen in 
each iteration of the main loop.

- **game_stats.py:** Inside this file, you'll find the **GameStats** class. The **GameStats** class has an __init__() 
method to handle the game state and high score, as well as a **reset_stats()** function that resets game statistics to 
their default values.

- **scoreboard.py:** This file contains the **Scoreboard** class, which handles various aspects of the in-game 
scoreboard. The class's __init__() method manages text fonts and image initialization for displaying the player's 
score, high score, level, and remaining ships. Each of these aspects is handled within its respective function for 
rendering images.

- **settings.py:** The **settings.py** file defines the **Settings** class. This class has an __init__() method to 
initialize attributes that control the game's appearance and ship speed. It also includes an 
**initialize_dynamic_settings()** function to manage settings that change during gameplay and an **increase_speed()** 
function to adjust the speed of the ship, bullets, and aliens.

- **ship.py:** In this file, you'll find the **Ship** class, which defines the player's spaceship. The Ship class has 
an __init__() method and an **update()** method to manage the ship's position, as well as a **center_ship()** function 
to center the ship, and a **blitme()** method for drawing the ship on the screen. The image of the ship is stored in 
**ship.bmp**, located in the images folder.

These components come together to create the "Alien Invasion" game, providing an exciting and challenging gaming 
experience for players.