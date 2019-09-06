import arcade
import os

#arcade uses pixels to measure eveything, so the below line of code
#create a game window that is 600 pixels wide and 600 pixels high
#the last variable gives the window its name
arcade.open_window(600, 600, "ArcadeIntroduction")

#you need this line of code to start drawing
arcade.start_render()

#this is where you type all the code you want to use to draw
#for example arcade.draw_rectangle_filled(..) or arcade.draw_ellipse_filled()




#this command tells the program you are done writing all your drawing commands
arcade.finish_render()

#this line runs your game
arcade.run()
