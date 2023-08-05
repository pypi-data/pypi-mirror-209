from playpen import *
import random
import math


@main
def _():
    WIDTH, HEIGHT = get_screen_size()
    MIN_RADIUS = 10
    MAX_RADIUS = 50
    MAX_SPEED = 10

    for _ in range(50):
        ball = Ball(
            random.random() * WIDTH,
            random.random() * HEIGHT,
            MIN_RADIUS + random.random() * (MAX_RADIUS - MIN_RADIUS))
        ball.color = random.choice(COLORS)
        ball.draggable = True
        ball.lift_on_click = True
        ball.boundary_rule_x = 'wrap'
        speed = random.random() * MAX_SPEED
        angle = random.random() * 2 * math.pi
        ball.velocity = Vector(
            speed * math.cos(angle),
            speed * math.sin(angle))
