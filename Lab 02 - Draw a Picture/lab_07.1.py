import arcade
# GLOBALS
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 800

class Car(arcade.Window):

    def __init__(self, width, height, title):

        super()__init__(600, 480, "Help Me")

        def draw(self):
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


            def draw_number(x, y, p):
                # DRAW CAR NUMBER
                arcade.draw_text(p,
                                 x, y,
                                 arcade.color.WHITE, 24)

            # CAR 1
            car_body(450, 250)
            draw_car(450, 250)
            car_fins(450, 250)
            draw_number(450, 250, 1)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()
    Window = Car(600, 480, 'MyCar')
    #draw_grass()
    # FINISH DRAWING
    arcade.finish_render()
    # KEEP WINDOW OPEN
    arcade.run()
    # RUN MAIN FUNCTION


main()
