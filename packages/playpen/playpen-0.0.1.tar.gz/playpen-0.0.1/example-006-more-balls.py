from playpen import *
import random


@main
def _():
    WIDTH, HEIGHT = get_screen_size()
    MAX_RADIUS = 50

    for _ in range(100):
        ball = Ball(
            random.random() * WIDTH,
            random.random() * HEIGHT,
            random.random() * MAX_RADIUS)
        ball.color = random.choice(COLORS)
        ball.draggable = True
        ball.lift_on_click = True
