import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.50
SPRITE_SCALING_COIN = .25
SPRITE_SCALING_TORCH = .25
COIN_COUNT = 50
TORCH_COUNT = 60

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN_TITLE = "ROBOT and TORCH"


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.torch_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.torch_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        img = ":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(img, SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite(":resources:images/animated_characters/robot/robot_idle.png",
                                 SPRITE_SCALING_COIN)
            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            # Add the coin to the lists
            self.coin_list.append(coin)

        for i in range(TORCH_COUNT):

            torch = arcade.Sprite(":resources:images/tiles/torch1.png", SPRITE_SCALING_TORCH)

            torch.center_x = random.randrange(SCREEN_WIDTH)
            torch.center_y = random.randrange(SCREEN_HEIGHT)
            self.torch_list.append(torch)
    def on_draw(self):
        """ Draw everything """
        self.clear()
        self.coin_list.draw()
        self.torch_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(text=output, start_x=10, start_y=20,
                         color=arcade.color.WHITE, font_size=14)

        if len(self.coin_list) == 0:
            self.clear()
            arcade.draw_text("GAME OVER!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                             arcade.color.WHITE, 30, anchor_x="center")
            output = f"Score: {self.score}"

            arcade.draw_text(text=output, start_x=400, start_y=200,
                             color=arcade.color.WHITE, font_size=14)


    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)
        torch_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.torch_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            explosion_sound = arcade.load_sound(":resources:sounds/coin3.wav")
            arcade.play_sound(explosion_sound)

        for torch in torch_hit_list:
            torch.remove_from_sprite_lists()
            self.score -= 1
            laser_sound = arcade.load_sound("laser.wav")
            arcade.play_sound(laser_sound)




def main():
    """ Main function """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()