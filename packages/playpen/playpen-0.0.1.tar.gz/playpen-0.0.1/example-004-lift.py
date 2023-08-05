from playpen import *


# Set screen width to 600 pixels
WIDTH = 600

# Set screen height to 400 pixels
HEIGHT = 400

# Set the width and height of your window here.
resize(width=WIDTH, height=HEIGHT)


###################################
#
# *.lift_on_click = True
#
###################################

box = Box(x=WIDTH/2, y=HEIGHT/2, width=100, height=100)
box.color = 'pink'
box.draggable = True
box.lift_on_click = True

red_ball = Ball(40, 40, 30)
red_ball.color = 'red'
red_ball.draggable = True
red_ball.lift_on_click = True

# This line makes your program wait for you to press
# a key or move stuff around with your mouse.
mainloop()
