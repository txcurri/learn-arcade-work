"""
This is a comment.
This is to help me remember later.
"""
# this is my single comment.
# import Arcade

import arcade


arcade.open_window(600, 600, "Drawing Example")

arcade.set_background_color(arcade.csscolor.RED)

# Get ready to draw
arcade.start_render()

# Draw a rectangle
# Left of 0, right of 599
# Top of 300, bottom of 0
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.DARK_RED)

# START LINE
arcade.draw_line(500, 290, 350, 0, arcade.color.WHITE_SMOKE, 30)

# FRONT WHEEL
arcade.draw_circle_filled(350, 100, 30, arcade.csscolor.BLACK)

# FAR BACK WHEEL
arcade.draw_circle_filled(250, 300, 80, arcade.csscolor.BLACK)

# CAR BODY
arcade.draw_triangle_filled(50, 200, 350, 100, 250, 320, arcade.csscolor.DARK_GREEN)

# CAR FINS
arcade.draw_triangle_filled(200, 250, 350, 100, 150, 180, arcade.csscolor.BLACK)
arcade.draw_triangle_filled(150, 250, 350, 100, 50, 480, arcade.csscolor.BLUE_VIOLET)
arcade.draw_triangle_filled(200, 250, 350, 100, 150, 480, arcade.csscolor.BLACK)

# NEAR BACK WHEEL
arcade.draw_circle_filled(100, 200, 80, arcade.csscolor.BLACK)

# Draw text at with a font size of 24 pts.
arcade.draw_text("DRAG RACE!",
                 200, 530,
                 arcade.color.BLACK, 24)

# Finish Drawing
arcade.finish_render()

# keep the window open
arcade.run()
