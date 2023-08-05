import tkinter as tk
import time
from typing import List, Tuple, Set, Callable, Any, Literal, Union

COLORS: Tuple[str, ...] = (
    'snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white',
    'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque',
    'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue',
    'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray',
    'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy',
    'cornflower blue',
    'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue',
    'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue',
    'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise',
    'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green',
    'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green',
    'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green',
    'yellow green', 'forest green', 'green',
    'olive drab', 'dark khaki', 'khaki', 'pale goldenrod',
    'light goldenrod yellow',
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod',
    'dark goldenrod', 'rosy brown',
    'indian red', 'saddle brown', 'sandy brown',
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink',
    'deep pink', 'pink', 'light pink',
    'pale violet red', 'maroon', 'medium violet red', 'violet red',
    'medium orchid', 'dark orchid', 'dark violet', 'blue violet',
    'purple', 'medium purple',
    'thistle', 'snow2', 'snow3',
    'snow4', 'seashell2', 'seashell3', 'seashell4',
    'black',
)

_NOP_HANDLER: Callable[[Any], None] = lambda _: None
_FRAMES_PER_SECOND = 30
_NS_PER_FRAME = int(10 ** 9 / _FRAMES_PER_SECOND)
_NS_IN_MS = 10 ** 6
_DEFAULT_COLOR_FOR_GEOMTRY = 'blue'

BoundaryRule = Literal['none', 'wall', 'wrap']
"Rule for what to do when an object hits a boundary"

_width: float = 600
_height: float = 400
_key_handler: Callable[['KeyEvent'], None] = _NOP_HANDLER
_click_handler: Callable[['ClickEvent'], None] = _NOP_HANDLER
_right_click_handler: Callable[['ClickEvent'], None] = _NOP_HANDLER
_all_objects: List['Object'] = []
_root = tk.Tk()
_collision_set: Set['Ball'] = set()
_collision_pairs: Set[Tuple[int, int]] = set()
_tick = 0

_canvas = tk.Canvas(
    _root,
    bg='black',
    width=_width,
    height=_height,
    bd=0,
    highlightthickness=0,
    relief='ridge')
_canvas.pack()


def title(title: str) -> None:
    _root.winfo_toplevel().title(title)


def resize(width: int, height: int):
    global _width, _height
    _width = width
    _height = height
    _canvas.config(width=width, height=height)
    _canvas.pack()


def get_screen_size() -> Tuple[float, float]:
    return _width, _height


def on_key(handler: Callable[['KeyEvent'], None]) -> None:
    global _key_handler
    _key_handler = handler


def on_click(handler: Callable[['ClickEvent'], None]) -> None:
    global _click_handler
    _click_handler = handler


def on_right_click(handler: Callable[['ClickEvent'], None]) -> None:
    global _right_click_handler
    _right_click_handler = handler


def mainloop():
    import __main__

    title(__main__.__file__)

    key_event = KeyEvent()
    click_event = ClickEvent()
    drag_object: Union[Object, None] = None
    drag_offset_x: float = 0
    drag_offset_y: float = 0
    drag_start_x: float = 0
    drag_start_y: float = 0
    drag_start_tick = 0

    def on_key_event(event: 'tk.Event[tk.Misc]') -> None:
        key_event.keysym = event.keysym
        key_event.keycode = event.keycode
        _key_handler(key_event)

    def on_click_event(event: 'tk.Event[tk.Misc]') -> None:
        x = click_event.x = event.x
        y = click_event.y = event.y

        for obj in reversed(_all_objects):
            if obj.contains_point(x, y):
                if obj.lift_on_click:
                    obj.lift()
                if obj.draggable:
                    nonlocal drag_object, drag_offset_x, drag_offset_y
                    nonlocal drag_start_x, drag_start_y, drag_start_tick
                    drag_object = obj
                    drag_offset_x = obj.x - x
                    drag_offset_y = obj.y - y
                    drag_start_x = obj.x
                    drag_start_y = obj.y
                    drag_start_tick = _tick
                    obj.velocity = Vector(0, 0)
                    break
                if obj.on_click_handler:
                    obj.on_click_handler(click_event)
                    break
        else:
            _click_handler(click_event)

    def on_right_click_event(event: 'tk.Event[tk.Misc]') -> None:
        click_event.x = event.x
        click_event.y = event.y
        _right_click_handler(click_event)

    def on_button_release_event(event: 'tk.Event[tk.Misc]') -> None:
        nonlocal drag_object
        if (drag_object and isinstance(drag_object, Ball) and
                drag_object in _collision_set):
            drag_object.velocity = (
                drag_object.position -
                Vector(drag_start_x, drag_start_y)
            ) * (1 / (_tick - drag_start_tick))

        drag_object = None

    def on_drag(event: 'tk.Event[tk.Misc]') -> None:
        if drag_object:
            drag_object.moveto(
                event.x + drag_offset_x, event.y + drag_offset_y)

    def on_motion(event: 'tk.Event[tk.Misc]') -> None:
        pass

    _root.bind('<KeyPress>', on_key_event)
    _root.bind('<Button-1>', on_click_event)
    _root.bind('<Button-3>', on_right_click_event)
    _root.bind('<ButtonRelease-1>', on_button_release_event)
    _root.bind('<B1-Motion>', on_drag)
    _root.bind('<Motion>', on_motion)
    _root.after(0, _update)
    tk.mainloop()


class KeyEvent:

    keysym: str
    "The name of the key that was pressed"

    keycode: int
    "The unique identifier for the key on the keyboard that was pressed"

    def __init__(self) -> None:
        self.keysym = ''
        self.keycode = 0


class ClickEvent:
    x: float
    y: float

    def __init__(self) -> None:
        self.x = 0
        self.y = 0


class Object:
    on_click_handler: Union[Callable[['ClickEvent'], None], None]

    boundary_rule_x: BoundaryRule
    """
    Controls how this object will behave when it reaches the left or right
    edges of the screen
    """

    boundary_rule_y: BoundaryRule
    """
    Controls how this object will behave when it reaches the top or bottom
    edges of the screen
    """

    lift_on_click: bool
    "Controls whether this object will be lifted when clicked"

    def __init__(self, id: int, x: float, y: float) -> None:
        _all_objects.append(self)
        self.id = id
        self._x = x
        self._y = y
        self._vx = 0
        self._vy = 0
        self.on_click_handler = None
        self.draggable = False
        self.boundary_rule_x = 'wall'
        self.boundary_rule_y = 'wall'
        self.lift_on_click = False

    def update(self) -> None:
        if self._vx or self._vy:
            self._x += self._vx
            self._y += self._vy

            if self.boundary_rule_x == 'wall':
                if self.left < 0 or self.right >= _width:
                    self._vx *= -1
                    self._x += self._vx
            elif self.boundary_rule_x == 'wrap':
                if self._x < 0 or self._x >= _width:
                    self._x = self._x % _width

            if self.boundary_rule_y == 'wall':
                if self.top < 0 or self.bottom >= _height:
                    self._vy *= -1
                    self._y += self._vy
            elif self.boundary_rule_y == 'wrap':
                if self._y < 0 or self._y >= _height:
                    self._y = self._y % _height

            self._reset_coords()

    def lift(self) -> None:
        """
        Lift this object so that this object appears on the 'top' of the pile.
        """
        obj = self
        for i in range(len(_all_objects)):
            prev = _all_objects[i]
            _all_objects[i] = obj
            obj = prev
            if obj == self:
                break
        _canvas.lift(self.id)

    def contains_point(self, x: float, y: float) -> bool:
        raise NotImplemented(f"{type(self).__name__}.contains_point")

    @property
    def left(self) -> float:
        raise NotImplemented(f"{type(self).__name__}.left")

    @property
    def right(self) -> float:
        raise NotImplemented(f"{type(self).__name__}.right")

    @property
    def top(self) -> float:
        raise NotImplemented(f"{type(self).__name__}.top")

    @property
    def bottom(self) -> float:
        raise NotImplemented(f"{type(self).__name__}.bottom")

    def _reset_coords(self) -> None:
        raise NotImplemented(f"{type(self).__name__}._reset_coords")

    @property
    def position(self) -> 'Vector':
        return Vector(self._x, self._y)

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, new_x: float) -> None:
        self._x = new_x
        self._reset_coords()

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, new_y: float) -> None:
        self._y = new_y
        self._reset_coords()

    @property
    def velocity(self) -> 'Vector':
        return Vector(self._vx, self._vy)

    @velocity.setter
    def velocity(self, v: 'Vector') -> None:
        self._vx = v.x
        self._vy = v.y

    def moveto(self, x: float, y: float) -> None:
        self._x = x
        self._y = y
        self._reset_coords()

    def move(self, dx: float, dy: float) -> None:
        self.moveto(self._x + dx, self._y + dy)

    def hide(self) -> None:
        _canvas.itemconfig(self.id, state='hidden')

    def show(self) -> None:
        _canvas.itemconfig(self.id, state='normal')

    def on_click(self, new_handler: Callable[['ClickEvent'], None]) -> None:
        self.on_click_handler = new_handler


class _ObjectWithColor(Object):
    def __init__(
                self,
                id: int,
                x: float,
                y: float) -> None:
        super().__init__(id, x, y)
        self._color = _DEFAULT_COLOR_FOR_GEOMTRY

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, new_color: str) -> None:
        _canvas.itemconfig(self.id, fill=new_color)
        self._color = new_color


class _RectangularObject(_ObjectWithColor):
    def __init__(
            self,
            id: int,
            x: float, y: float,
            width: float, height: float) -> None:
        super().__init__(id, x, y)
        self._width = width
        self._height = height

    def contains_point(self, x: float, y: float) -> bool:
        return self.left <= x <= self.right and self.top <= y <= self.bottom

    def _reset_coords(self) -> None:
        x = self._x
        y = self._y
        w2 = self._width / 2
        h2 = self._height / 2
        _canvas.coords(self.id, x - w2, y - h2, x + w2, y + h2)

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, new_width: float) -> None:
        self._width = new_width
        self._reset_coords()

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, new_height: float) -> None:
        self._height = new_height
        self._reset_coords()

    @property
    def left(self) -> float:
        return self._x - self._width / 2

    @property
    def right(self) -> float:
        return self._x + self._width / 2

    @property
    def top(self) -> float:
        return self._y - self._height / 2

    @property
    def bottom(self) -> float:
        return self._y + self._height / 2


class Box(_RectangularObject):
    def __init__(
            self,
            x: float, y: float,
            width: float, height: float) -> None:
        w2 = width / 2
        h2 = height / 2
        super().__init__(
            _canvas.create_rectangle(
                x - w2, y - h2,
                x + w2, y + h2, fill=_DEFAULT_COLOR_FOR_GEOMTRY),
            x, y, width, height)
        self._width = width
        self._height = height


class Ball(_ObjectWithColor):
    def __init__(
            self,
            x: float, y: float,
            radius: float) -> None:
        super().__init__(
            _canvas.create_oval(
                x - radius, y - radius,
                x + radius, y + radius,
                fill=_DEFAULT_COLOR_FOR_GEOMTRY),
            x, y)
        self._radius = radius

    def _reset_coords(self) -> None:
        x = self._x
        y = self._y
        r = self._radius
        _canvas.coords(self.id, x - r, y - r, x + r, y + r)

    def contains_point(self, x: float, y: float) -> bool:
        dx = self._x - x
        dy = self._y - y
        r = self._radius
        return dx * dx + dy * dy <= r * r

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, new_radius: float) -> None:
        self._radius = new_radius
        self._reset_coords()

    @property
    def left(self) -> float:
        return self._x - self._radius

    @property
    def right(self) -> float:
        return self._x + self._radius

    @property
    def top(self) -> float:
        return self._y - self._radius

    @property
    def bottom(self) -> float:
        return self._y + self._radius

    @property
    def collision(self) -> bool:
        return self in _collision_set

    @collision.setter
    def collision(self, enable: bool = True) -> None:
        if enable:
            _collision_set.add(self)
        else:
            _collision_set.discard(self)

class PictureFrame(_RectangularObject):
    pass


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float) -> 'Vector':
        return Vector(self.x * other, self.y * other)

    def dot(self, other: 'Vector') -> float:
        return self.x * other.x + self.y * other.y

    def __iter__(self):
        yield self.x
        yield self.y

    def len2(self) -> float:
        "Returns the square of the length of this vector"
        return self.x * self.x + self.y * self.y

    def len(self) -> float:
        return self.len2() ** 0.5

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"


def _compute_collision_velocity(
        m1: float, x1: Vector, v1: Vector,
        m2: float, x2: Vector, v2: Vector) -> Vector:
    return v1 - (x1 - x2) * (
        ((m2 + m2) / (m1 + m2)) *
        ((v1 - v2).dot(x1 - x2) / (x1 - x2).len2()))


def _update_collision(b1: Ball, b2: Ball) -> None:
    key = (b1.id, b2.id)
    dx = b1.x - b2.x
    dy = b1.y - b2.y
    rsum = b1.radius + b2.radius
    rsum2 = rsum * rsum
    if dx * dx + dy * dy > rsum2:
        _collision_pairs.discard(key)
        return

    if key in _collision_pairs:
        return

    _collision_pairs.add(key)

    # https://en.wikipedia.org/wiki/Elastic_collision
    # "Two-dimensional collision with two moving objects"

    x1 = b1.position
    v1 = b1.velocity
    x2 = b2.position
    v2 = b2.velocity
    m1 = b1.radius * b1.radius
    m2 = b2.radius * b2.radius

    b1.velocity = _compute_collision_velocity(
        m1, x1, v1,
        m2, x2, v2)
    b2.velocity = _compute_collision_velocity(
        m2, x2, v2,
        m1, x1, v1)

    # print("COLLISION")
    # print(f"  MASS {m1}, {m2}")
    # print(f"  VELOCITY {v1} -> {b1.velocity}")
    # print(f"  VELOCITY {v2} -> {b2.velocity}")


def _update() -> None:
    global _tick
    start_time_ns = time.time_ns()

    _tick += 1
    collision_list = tuple(_collision_set)
    for i in range(len(collision_list) - 1):
        a = collision_list[i]
        for j in range(i + 1, len(collision_list)):
            b = collision_list[j]
            _update_collision(a, b)

    for obj in _all_objects:
        obj.update()
    end_time_ns = time.time_ns()
    elapsed_time_ns = end_time_ns - start_time_ns
    _root.after(round((_NS_PER_FRAME - elapsed_time_ns) // _NS_IN_MS), _update)


def main(body: Callable[[], None]) -> None:
    body()
    mainloop()
