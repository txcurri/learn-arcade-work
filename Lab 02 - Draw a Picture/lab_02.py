"""
This is a comment.
This is to help me remember later.
"""
# this is my single comment.
# import Arcade

import arcade
import random

arcade.open_window(600, 600, "Drawing Example")

arcade.set_background_color(arcade.csscolor.RED)

# Get ready to draw
arcade.start_render()

arcade.draw_circle_filled(220, 230, 5, arcade.csscolor.WHITE)
# Draw a rectangle
# Left of 0, right of 599

# Top of 300, bottom of 0
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.DARK_RED)

# START LINE
arcade.draw_line(500, 290, 350, 0, arcade.color.WHITE_SMOKE, 30)

# FRONT WHEEL
x=220
y=230
arcade.draw_circle_filled(x + 130,y - 130, 30, arcade.csscolor.BLACK)
#arcade.draw_circle_filled(350, 100, 30, arcade.csscolor.BLACK)

# FAR BACK WHEEL
arcade.draw_circle_filled(x + 30, y + 70, 80, arcade.csscolor.BLACK)
#arcade.draw_circle_filled(250, 300, 80, arcade.csscolor.BLACK)
arcade.draw_circle_filled(x - 20, y - 30, 10, arcade.csscolor.WHITE)
#arcade.draw_circle_filled(200, 200, 10, arcade.csscolor.WHITE)

# CAR BODY
arcade.draw_triangle_filled(x - 170, y - 30,x + 130,y - 130,x +30,y + 70, arcade.csscolor.DARK_GREEN)
#arcade.draw_triangle_filled(50, 200, 350, 100, 250, 320, arcade.csscolor.DARK_GREEN)
x=220
y=230
# CAR FINS
arcade.draw_triangle_filled(x - 40, y + 20,x + 130,y - 130,x - 70,y -50, arcade.csscolor.BLACK)
#arcade.draw_triangle_filled(200, 250, 350, 100, 150, 180, arcade.csscolor.BLACK)
arcade.draw_triangle_filled(x - 70,y +20,x + 130,y - 130,x - 170, y + 250, arcade.csscolor.BLUE_VIOLET)
#arcade.draw_triangle_filled(150, 250, 350, 100, 50, 480, arcade.csscolor.BLUE_VIOLET)
arcade.draw_triangle_filled(x -20,y + 20,x + 130,y - 130,x - 70,y + 250, arcade.csscolor.BLACK)
#arcade.draw_triangle_filled(200, 250, 350, 100, 150, 480, arcade.csscolor.BLACK)
# NEAR BACK WHEEL
arcade.draw_circle_filled(x - 120,y - 30, 80, arcade.csscolor.BLACK)
#arcade.draw_circle_filled(100, 200, 80, arcade.csscolor.BLACK)

# Draw text at with a font size of 24 pts.
arcade.draw_text("DRAG RACE!",
                 200, 530,
                 arcade.color.BLACK, 24)
#x,y spot
arcade.draw_circle_filled(220, 230, 5, arcade.csscolor.WHITE)

# Finish Drawing
arcade.finish_render()

# keep the window open
arcade.run()
