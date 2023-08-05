from playpen import *

# Set screen width to 600 pixels
WIDTH = 600

# Set screen height to 400 pixels
HEIGHT = 400

# Set the width and height of your window here.
resize(width=WIDTH, height=HEIGHT)


# Create a box and place it at the center of the screen
# Make the box 30 pixels wide and 20 pixels tall
box = Box(x=WIDTH/2, y=HEIGHT/2, width=30, height=20)


@on_click
def _(event: ClickEvent):
    # Code here will run whenever you click
    # somewhere on the screen.
    box.moveto(event.x, event.y)


# This line makes your program wait for you to press
# a key or move stuff around with your mouse.
mainloop()
