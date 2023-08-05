from playpen import *
import random
import math


@main
def _():
    WIDTH, HEIGHT = get_screen_size()
    MIN_RADIUS = 30
    MAX_RADIUS = 50
    MAX_SPEED = 10

    for _ in range(16):
        radius = MIN_RADIUS + random.random() * (MAX_RADIUS - MIN_RADIUS)
        ball = Ball(
            radius + random.random() * (WIDTH - radius),
            radius + random.random() * (HEIGHT - radius),
            radius)
        ball.color = random.choice(COLORS)
        ball.draggable = True
        ball.lift_on_click = True
        ball.collision = True
        speed = random.random() * MAX_SPEED
        angle = random.random() * 2 * math.pi
        ball.velocity = Vector(
            speed * math.cos(angle),
            speed * math.sin(angle))
