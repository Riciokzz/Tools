In Alien Invasion, the player controls a ship that appears at
the bottom center of the screen. The player can move the ship
right and left using the arrow keys and shoot bullets using the
spacebar. When the game begins, a fleet of aliens fills the sky
and moves across and down the screen. The player shoots and
destroys the aliens. If the player shoots all the aliens, a new fleet
appears that moves faster than the previous fleet. If any alien hits
the player’s ship or reaches the bottom of the screen, the player
loses a ship. If the player loses three ships, the game ends.

- **alien.py** The alien.py file have Alien class. Alien has __init__ method with Sprite 
inheritance, setting it position on screen. Get alien image and set its attributes. It 
has blitme() method to draw aliens on the screen. The actual image of the alien is stored in
ufo.bmp, which is in the images folder. Also file have check_edges() function to handle 
alien boundary on screen. And update() to move aliens left and right.

- **alien_invasion.py** The main file, alien_invasion.py, creates a number of important objects used
throughout the game: the settings are stored in ai_settings, the main display
surface is stored in screen, and a ship instance is created in this file as
well. Also stored in alien_invasion.py is the main loop of the game, which is
a while loop that calls check_events() than checks if game is active to handle: ship.update(), 
update_bullets(), update_aliens(). Lastly update screen with previous updates using and update_screen().

- **bullet.py** The bullet.py file have Bullet class. Bullet has __init__ method, create bullets at ship position.
File have update() function to handle bullet speed and position. Also draw_bullet() function draw bullet on screen.

- **button.py** The button.py file have Button class. Button has an __init__() method to handle dimension and properties,
center button on screen. File have prep_msg() function to render image and text on screen and draw_button() to draw 
actually on screen.

- **game_functions.py** The game_functions.py file contains a number of functions that carry out
the bulk of the work in the game. The check_events() function detects relevant
events, such as keypresses and releases, and processes each of these
types of events through the helper functions check_keydown_events() and
A Ship That Fires Bullets
check_keyup_events(). For now, these functions manage the movement of
the ship. The game_functions module also contains update_screen(), which
redraws the screen on each pass through the main loop.

- **game_stats.py** The game_stats.py file contains the GameStats class. GameStats class has __init__() method 
with game state and high_score handle, and reset_stats() function with default values.

- **scoreboard.py** The scoreboard.py file contains Scoreboard class. Scoreboard has __init__() method, 
it handles text font, and image of prep_score(), prep_high_score(), prep_level() and prep_ships() 
initializing. Every function handles their own image rendering.

- **settings.py** The settings.py file contains the Settings class. This class has an
__init__() method, which initializes attributes controlling the game’s
appearance and the ship’s speed. File have initialize_dynamic_settings() function to handle settings 
that change throughout the game. And increace_spead() to adjust speed of ship, bullets and aliens.

- **ship.py** The ship.py file contains the Ship class. Ship has an __init__() method, an
update() method to manage the ship’s position, center_ship(), update() function to adjust ship movement left and right.
blitme() method draws the ship to the screen. The actual image of the ship is stored in ship.bmp, which is in the images folder.