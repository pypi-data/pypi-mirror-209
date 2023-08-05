from playpen import *


@main
def _():
    WIDTH, HEIGHT = get_screen_size()
    RADIUS = 30

    b1 = Ball(WIDTH // 2, HEIGHT // 2, RADIUS)
    b1.collision = True
    b1.color = 'white'
    b1.draggable = True

    b2 = Ball(RADIUS, HEIGHT // 2, RADIUS)
    b2.collision = True
    b2.color = 'green'
    b2.draggable = True

    b3 = Ball(WIDTH // 4, HEIGHT // 4, RADIUS)
    b3.collision = True
    b3.color = 'orange'
    b3.draggable = True

    @on_right_click
    def _(e: ClickEvent):
        print("INFO")
        print(f"  b1.velocity = {b1.velocity}")
        print(f"  b2.velocity = {b2.velocity}")
        print(f"  b3.velocity = {b3.velocity}")
