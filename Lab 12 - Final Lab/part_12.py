"""
for part 2
On-screen score
Players can lose the game if SHOT
sounds

for part 3
title screen
Multiplying enemies
game over screen
if you hit 20 enemies you win the game
"""

import arcade
import math
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Space Game"
BULLET_SPEED = 4
SPRITE_SCALING_LASER = 0.8
SPRITE_SCALING_PLAYER = 0.5


class MenuView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Welcome Space Warrior, may the force be with you!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100,
                         arcade.color.BLACK, font_size=28, anchor_x="center")
        arcade.draw_text("Be ready for a fast pace space attack!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50,
                         arcade.color.BLACK, font_size=25, anchor_x="center")
        arcade.draw_text("Watch out for multiplying enemies! ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Click to start", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 250,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instructions_view = MyGame()
        self.window.show_view(instructions_view)

class MyGame(arcade.View):
    """ Main application class """
    def __init__(self):
        super().__init__()

        self.frame_count = 0
        self.enemy_list = None
        self.bullet1_list = None
        self.bullet2_list = None
        self.player_list = None
        self.player = None
        self.enemy = None
        self.score = 0
        self.score_text = None
        self.level = 1

        # Load sounds. Sounds from kenney.nl
        self.gun_sound = arcade.sound.load_sound(":resources:sounds/laser1.wav")
        self.hit_sound = arcade.sound.load_sound(":resources:sounds/phaseJump1.wav")

    def setup(self):
        self.enemy_list = arcade.SpriteList()
        self.bullet1_list = arcade.SpriteList()
        self.bullet2_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.enemy_num = 5
        # Set up the player
        self.score = 0

        # Add player ship
        self.player = arcade.Sprite(":resources:images/space_shooter/playerShip1_orange.png", 0.5)
        self.player_list.append(self.player)

        # Add enemy ships
        for i in range(self.enemy_num):
            enemy = arcade.Sprite(":resources:images/space_shooter/playerShip1_green.png", 0.5)
            enemy.center_x = random.randint(0, SCREEN_WIDTH)
            enemy.center_y = SCREEN_HEIGHT - enemy.height
            enemy.angle = 180
            self.enemy_list.append(enemy)

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)
        self.setup()

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called whenever the mouse button is clicked. """
        # Create a bullet
        bullet2 = arcade.Sprite(":resources:images/space_shooter/laserRed01.png", SPRITE_SCALING_LASER)
        # Gunshot sound
        arcade.play_sound(self.gun_sound)
        # Position the bullet at the player's current location
        start_x = self.player.center_x
        start_y = self.player.center_y
        bullet2.center_x = start_x
        bullet2.center_y = start_y + 30
        bullet2.change_y += BULLET_SPEED
        # Add the bullet to the appropriate lists
        self.bullet2_list.append(bullet2)

    def on_draw(self):
        """Render the screen. """
        self.clear()
        self.bullet2_list.draw()
        self.enemy_list.draw()
        self.bullet1_list.draw()
        self.bullet2_list.draw()
        self.player_list.draw()

        # Call update() method for each bullet in the bullet list
        self.bullet2_list.update()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        output = f"Level: {self.level}"
        arcade.draw_text(output, 10, 35, arcade.color.WHITE, 15)

        # Prints score and game over
        if len(self.player_list) == 0:
            self.clear()
            arcade.draw_text("GAME OVER!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                             arcade.color.WHITE, 30, anchor_x="center")
            output = f"Score: {self.score}"

            arcade.draw_text(text=output, start_x=400, start_y=200,
                             color=arcade.color.WHITE, font_size=14)

        if len(self.enemy_list) == 20:
            self.clear()
            arcade.draw_text("YOU WIN!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                             arcade.color.WHITE, 30, anchor_x="center")
            output = f"Score: {self.score}"

            arcade.draw_text(text=output, start_x=400, start_y=200,
                             color=arcade.color.WHITE, font_size=14)

    def on_update(self, delta_time):

        # Call update on all sprites
        self.bullet2_list.update()

        # Loop through each bullet
        for bullet in self.bullet2_list:

            # Check this bullet to see if it hit a ship
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
                for i in range(2):
                    enemy = arcade.Sprite(":resources:images/space_shooter/playerShip1_green.png", 0.5)
                    enemy.center_x = random.randint(0, SCREEN_WIDTH)
                    enemy.center_y = SCREEN_HEIGHT - enemy.height
                    enemy.angle = 180
                    self.enemy_list.append(enemy)

            # For every ship we hit, add to the score and remove the ship
            for ship in hit_list:
                ship.remove_from_sprite_lists()
                self.score += 1

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > SCREEN_WIDTH or bullet.top < 0 or bullet.right < 0 or bullet.left > SCREEN_WIDTH:
                bullet.remove_from_sprite_lists()

        self.frame_count += 1

        # Loop through each bullet
        for bullet in self.bullet1_list:

            # Check this bullet to see if it hit a ship
            hit_list = arcade.check_for_collision_with_list(bullet, self.player_list)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            # For every ship we hit, add to the score and remove the ship
            for ship in hit_list:
                ship.remove_from_sprite_lists()
                self.score -= 1

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > SCREEN_WIDTH or bullet.top < 0 or bullet.right < 0 or bullet.left > SCREEN_WIDTH:
                bullet.remove_from_sprite_lists()

        # Loop through each enemy that we have
        for enemy in self.enemy_list:

            # First, calculate the angle to the player. We could do this
            # only when the bullet fires, but in this case we will rotate
            # the enemy to face the player each frame, so we'll do this
            # each frame.

            # Position the start at the enemy's current location
            start_x = enemy.center_x
            start_y = enemy.center_y

            # Get the destination location for the bullet
            dest_x = self.player.center_x
            dest_y = self.player.center_y

            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Set the enemy to face the player.
            enemy.angle = math.degrees(angle) - 90

            # Shoot every 60 frames change of shooting each frame
            if self.frame_count % 80 == 0:
                bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png")
                bullet.center_x = start_x
                bullet.center_y = start_y

                # Angle the bullet sprite
                bullet.angle = math.degrees(angle)

                # Taking into account the angle, calculate our change_x
                # and change_y. Velocity is how fast the bullet travels.
                bullet.change_x = math.cos(angle) * BULLET_SPEED
                bullet.change_y = math.sin(angle) * BULLET_SPEED

                self.bullet1_list.append(bullet)

        # Get rid of the bullet when it flies off-screen
        for bullet in self.bullet1_list:
            if bullet.top < 0:
                bullet.remove_from_sprite_lists()

        self.bullet1_list.update()

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """Called whenever the mouse moves. """
        self.player.center_x = x
        self.player.center_y = y


def main():
    """ Main function """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.total_score = 0
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()