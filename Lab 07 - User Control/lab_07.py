# GLOBALS
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 800
MOVEMENT_SPEED = 1

import arcade

def car_body(x, y):
    # DRAW CAR BODY
    arcade.draw_triangle_filled(x - 170, y - 30, x + 130, y - 130, x + 30, y + 70, arcade.csscolor.DARK_GREEN)
    arcade.draw_triangle_filled(x - 40, y + 20, x + 130, y - 130, x - 70, y - 50, arcade.csscolor.BLACK)


def car_fins(x, y):
    # CAR FINS
    arcade.draw_triangle_filled(x - 20, y + 20, x + 130, y - 130, x - 70, y + 250, arcade.csscolor.YELLOW_GREEN)
    arcade.draw_triangle_filled(x - 70, y + 20, x + 130, y - 130, x - 170, y + 250, arcade.csscolor.BLUE_VIOLET)



def draw_grass():
    # DRAW RACE FIELD
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 1.2, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_number(x, y, p):
    # DRAW CAR NUMBER
    arcade.draw_text(p,
                     x, y,
                     arcade.color.WHITE, 24)


def draw_car(x, y):
    car_body(x, y)
    # FRONT WHEEL
    arcade.draw_circle_filled(x + 130, y - 130, 30, arcade.csscolor.BLACK)

    # FAR BACK WHEEL
    arcade.draw_circle_filled(x + 30, y + 70, 80, arcade.csscolor.BLACK)

    # NEAR BACK WHEEL
    arcade.draw_circle_filled(x - 120, y - 30, 80, arcade.csscolor.BLACK)

    car_fins(x, y)
class Car:
    """ This class manages a car bouncing on the screen. """

    def __init__(self, position_x, position_y, change_x, change_y):
        """ Constructor. """

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
    def draw(self):
        draw_car(self.position_x, self.position_y)
    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x



class MyGame(arcade.Window):
    """ My window class. """

    def __init__(self, width, height, title):
        # Call the parent class's init function
        super().__init__(width, height, title)

        """ Constructor. """


        arcade.set_background_color(arcade.color.DARK_BLUE)        # Create our car
        self.car = Car(250, 250, 0, 0)



    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.car.draw()
    def on_mouse_motion(self, x, y, dx, dy):
        self.car.position_x = x
        self.car.position_y = y
        self.set_mouse_visible(False)
    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.car.position_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.car.position_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.car.position_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.car.position_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.car.position_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.car.position_y = 0




def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Car")

    arcade.run()



main()
