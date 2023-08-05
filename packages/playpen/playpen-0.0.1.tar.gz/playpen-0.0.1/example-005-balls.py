from playpen import *



@main
def _():
    WIDTH, HEIGHT = get_screen_size()

    red_ball = Ball(40, 40, 30)
    red_ball.color = 'red'
    red_ball.draggable = True
    red_ball.lift_on_click = True

    blue_ball = Ball(WIDTH // 2 + 70, 100, 30)
    blue_ball.color = 'blue'
    blue_ball.draggable = True
    blue_ball.lift_on_click = True

    green_ball = Ball(WIDTH - 100, HEIGHT - 20, 30)
    green_ball.color = 'green'
    green_ball.draggable = True
    green_ball.lift_on_click = True
