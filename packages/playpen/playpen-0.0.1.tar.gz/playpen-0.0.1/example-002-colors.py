from playpen import *

# Set screen width to 600 pixels
WIDTH = 600

# Set screen height to 400 pixels
HEIGHT = 400

# Set the width and height of your window here.
resize(width=WIDTH, height=HEIGHT)

color_index = 0
colors = [
    'red',
    'blue',
    'green',
    'orange',
    'yellow',

    # You can specify custom colors
    # by specifying the red, green and blue components.
    # The brightness component is made up of 2 hex digits
    # for a total of 6 hex digits per color.
    '#2244FF',
]

box = Box(
    x=WIDTH/2, y=HEIGHT/2,
    width=WIDTH/2, height=HEIGHT/2)
box.color = 'red'


# Notice the 'box.' we put before 'on_click'
# This makes sure that the code below only runs
# when we actually click the box itself
@box.on_click
def _(event: ClickEvent):
    # Every time we click on the screen, we cycle
    # through the colors
    global color_index
    color_index = (color_index + 1) % len(colors)
    box.color = colors[color_index]


# This line makes your program wait for you to press
# a key or move stuff around with your mouse.
mainloop()
