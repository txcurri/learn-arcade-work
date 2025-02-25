
import arcade
import random
import os

SPRITE_SCALING = 0.5
SPRITE_SCALING_COIN = 0.2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Robot Collector"

NUMBER_OF_COINS = 50

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

#

        # Sprite lists
        self.all_sprites_list = None
        self.coin_list = None

        # Set up the player
        self.player_sprite = None
        self.wall_list = None
        self.physics_engine = None
        self.score = 0

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        self.player_sprite = arcade.Sprite("maleAdventurer_idle.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64

        # -- Set up the walls
        # Create a series of horizontal walls
        for y in range(0, 800, 200):
            for x in range(100, 800, 120):
                wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING)
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)
        for y in range(0, 200, 800):
            for x in range(100, 800, 64):
                wall = arcade.Sprite("Grass.png", SPRITE_SCALING)
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)
        for y in range(50, 800, 200):
            for x in range(100, 700, 120):
                wall = arcade.Sprite("Grass.png", SPRITE_SCALING)
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)

        # -- Randomly place coins where there are no walls
        # Create the coins
        for i in range(NUMBER_OF_COINS):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite("robot_idle.png", SPRITE_SCALING_COIN)



            # --- IMPORTANT PART ---



            # Boolean variable if we successfully placed the coin

            coin_placed_successfully = False



            # Keep trying until success

            while not coin_placed_successfully:

                # Position the coin

                coin.center_x = random.randrange(SCREEN_WIDTH)

                coin.center_y = random.randrange(SCREEN_HEIGHT)



                # See if the coin is hitting a wall

                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)



                # See if the coin is hitting another coin

                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)



                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:

                    # It is!

                    coin_placed_successfully = True



            # Add the coin to the lists

            self.coin_list.append(coin)



            # --- END OF IMPORTANT PART ---

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        # Draw all the sprites.
        self.wall_list.draw()
        self.coin_list.draw()
        self.player_sprite.draw()

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

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0





    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)


        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            explosion_sound = arcade.load_sound("coin3.wav")
            arcade.play_sound(explosion_sound)

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


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()