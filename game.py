# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.player_list = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        #Any other code that is needed to set up the game goes here



    def setup(self):
        """ Set up the game here. Call this function to restart the game. """

        # Create the Sprite lists
        self.player_list = arcade.SpriteList()

        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = arcade.Sprite...
        self.player_sprite.center_x =
        self.player_sprite.center_y =
        self.player_list.append(self.player_sprite)


    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw any sprites
        self.player_list.draw()

        # Draw our score on the screen, scrolling it with the viewport

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.player_list.update()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
