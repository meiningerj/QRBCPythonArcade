import arcade
import os

#arcade uses pixels to measure eveything, so the below line of code
#create a game window that is 600 pixels wide and 600 pixels high
#the last variable gives the window its name
arcade.open_window(600, 600, "ArcadeIntroduction")

#you need this line of code to start drawing
arcade.start_render()

#this is where you type all the code you want to use to draw
#try and work out what each number does
#http://arcade.academy/arcade.html#drawing-commands may give you some hints
arcade.draw_triangle_filled(100,100,300,400,500,100,arcade.color.BLACK)

#this command tells the program you are done writing all your drawing commands
arcade.finish_render()

#this line runs your game
arcade.run()
