import arcade
# GLOBALS
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 800


def draw_car(x, y):
    # FRONT WHEEL
    arcade.draw_circle_filled(x + 130, y - 130, 30, arcade.csscolor.BLACK)

    # FAR BACK WHEEL
    arcade.draw_circle_filled(x + 30, y + 70, 80, arcade.csscolor.BLACK)

    # NEAR BACK WHEEL
    arcade.draw_circle_filled(x - 120, y - 30, 80, arcade.csscolor.BLACK)


def car_body(x, y):
    # DRAW CAR BODY
    arcade.draw_triangle_filled(x - 170, y - 30, x + 130, y - 130, x + 30, y + 70, arcade.csscolor.DARK_GREEN)
    arcade.draw_triangle_filled(x - 40, y + 20, x + 130, y - 130, x - 70, y - 50, arcade.csscolor.BLACK)


def car_fins(x, y):
    # CAR FINS
    arcade.draw_triangle_filled(x - 70, y + 20, x + 130, y - 130, x - 170, y + 250, arcade.csscolor.BLUE_VIOLET)
    arcade.draw_triangle_filled(x - 20, y + 20, x + 130, y - 130, x - 70, y + 250, arcade.csscolor.YELLOW_GREEN)


def draw_grass():
    # DRAW RACE FIELD
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 1.2, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_number(x, y, p):
    # DRAW CAR NUMBER
    arcade.draw_text(p,
                     x, y,
                     arcade.color.WHITE, 24)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()
    draw_grass()
# FINISH LINE
    arcade.draw_line(900, 600, 250, 0, arcade.color.WHITE_SMOKE, 30)

# CAR 1
    car_body(450, 250)
    draw_car(450, 250)
    car_fins(450, 250)
    draw_number(450, 250, 1)
# CAR #2
    car_body(80, 180)
    draw_car(80, 180)
    car_fins(80, 180)
    draw_number(80, 180, 13)
# CAR #3
    car_body(600, 600)
    draw_car(600, 600)
    car_fins(600, 600)
    draw_number(600, 600, 2)
# DECLARE WINNER
    arcade.draw_text("Winner!",
                     200, 500,
                     arcade.color.BLACK, 20)
# FINISH DRAWING
    arcade.finish_render()
# KEEP WINDOW OPEN
    arcade.run()
# RUN MAIN FUNCTION


main()
