from tkinter import *
from tkinter.font import Font
from Cube import *


def rectangle(canvas, x1, x2, y1, y2):
    rect = canvas.create_rectangle(x1, x2, y1, y2)
    return rect


def grid3x3(canvas, origin_x, origin_y):
    """
    Creates a 3x3 grid of uncolored squares with a black rim.

    ├───99px────┤

    ┌───┬───┬───┐  ┬
    │ 0 │ 1 │ 2 │  │
    ├───┼───┼───┤  │
    │ 3 │ 4 │ 5 │  99px
    ├───┼───┼───┤  │
    │ 6 │ 7 │ 8 │  │
    └───┴───┴───┘  ┴

    The Origin consists of a x and y coordinate and represents the upper left hand corner,
    from which the grid will be created. Every square will be 33x33px with a border width of 1px.

    """
    grid = [None] * 9
    y = origin_y
    x = origin_x

    for idx, item in enumerate(grid):
        if idx == 3 or idx == 6:
            y += 33
        if idx % 3 == 0:
            x = origin_x
        else:
            x += 33

        item = canvas.create_rectangle(x, y, x + 33, y + 33)
        grid[idx] = item
    return grid


def create_cube_hexomino(window, int_x, int_y):
    # Creating each side as a list which contains 9 rectangles.
    # The given coordinates are the coordinates of the left side
    up = grid3x3(window, int_x+105, int_y-105)
    left = grid3x3(window, int_x, int_y)
    front = grid3x3(window, int_x+105, int_y)
    right = grid3x3(window, int_x+210, int_y)
    back = grid3x3(window, int_x+315, int_y)
    down = grid3x3(window, int_x+105, int_y+105)

    # Combining all the sides to one single iterable list
    cube = [up, front, right, back, left, down]

    # Coloring the the fixed cross of the cube.
    for side_idx, side in enumerate(cube):
        for piece_idx, piece in enumerate(side):
            if 4 != piece_idx:
                window.itemconfigure(side[piece_idx], fill='grey')

    window.itemconfigure(cube[0][4], fill='yellow')
    window.itemconfigure(cube[1][4], fill='red')
    window.itemconfigure(cube[2][4], fill='green')
    window.itemconfigure(cube[3][4], fill='orange')
    window.itemconfigure(cube[4][4], fill='blue')
    window.itemconfigure(cube[5][4], fill='white')

    return cube
