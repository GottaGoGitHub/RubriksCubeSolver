# from RubriksCubeSolver.Cube import *
from Cube import *


#   R U R' U'
def ruru(window, cube):
    rotate_right(window, cube)
    rotate_up(window, cube)
    rotate_right_prime(window, cube)
    rotate_up_prime(window, cube)


#   L U' L' U
def lulu(window, cube):
    rotate_left(window, cube)
    rotate_up_prime(window, cube)
    rotate_left_prime(window, cube)
    rotate_up(window, cube)


#   U R U R' U' y L U' L' U
def second_layer_right(window, cube):
    rotate_up(window, cube)
    ruru(window, cube)
    rotate_cube_right(window, cube)
    lulu(window, cube)


#   U' L U' L' U y' R U R' U'
def second_layer_left(window, cube):
    rotate_up_prime(window, cube)
    lulu(window, cube)
    rotate_cube_left(window, cube)
    ruru(window, cube)


#   F R U R' U' F'
def top_cross(window, cube):
    rotate_front(window, cube)
    ruru(window, cube)
    rotate_front_prime(window, cube)


#   R U R' U R 2U' R'
def correct_front(window, cube):
    rotate_right(window, cube)
    rotate_up(window, cube)
    rotate_right_prime(window, cube)
    rotate_up(window, cube)
    rotate_right(window, cube)
    rotate_up_prime(window, cube)
    rotate_up_prime(window, cube)
    rotate_right_prime(window, cube)


#   U R U' L U R' U' L'
def sort_corners(window, cube):
    rotate_up(window, cube)
    rotate_right(window, cube)
    rotate_up_prime(window, cube)
    rotate_left(window, cube)
    rotate_up(window, cube)
    rotate_right_prime(window, cube)
    rotate_up_prime(window, cube)
    rotate_left_prime(window, cube)


def white_cross(window, cube):
    for side_idx, side in enumerate(cube):
        for piece_idx in enumerate(side):
            if piece_idx == 1 and window.itemcget(cube[side_idx][piece_idx], "fill") == 'white':
                if side_idx == 0:
                    rotate_back(window, cube)
                    rotate_back(window, cube)
                elif side_idx == 1:
                    rotate_front(window, cube)
                    rotate_right_prime(window, cube)
                elif side_idx == 2:
                    rotate_cube_right(window, cube)
                    rotate_front(window, cube)
                    rotate_right_prime(window, cube)
                elif side_idx == 3:
                    rotate_cube_right(window, cube)
                    rotate_cube_right(window, cube)
                    rotate_front(window, cube)
                    rotate_right_prime(window, cube)
                elif side_idx == 4:
                    rotate_cube_right(window, cube)
                    rotate_cube_right(window, cube)
                    rotate_cube_right(window, cube)
                    rotate_front(window, cube)
                    rotate_right_prime(window, cube)
            elif piece_idx == 3 and window.itemcget(cube[side_idx][piece_idx], "fill") == 'white':
                if side_idx == 0:
                    rotate_left(window, cube)
                    rotate_left(window, cube)
                elif side_idx == 1:
                    rotate_left(window, cube)
                elif side_idx == 2:
                    rotate_cube_right(window, cube)
                    rotate_left(window, cube)
                elif side_idx == 3:
                    rotate_cube_right(window, cube)
                    rotate_cube_right(window, cube)
                    rotate_left(window, cube)
                elif side_idx == 4:
                    rotate_cube_right(window, cube)
                    rotate_cube_right(window, cube)
                    rotate_cube_right(window, cube)
                    rotate_left(window, cube)
            elif piece_idx == 5 and window.itemcget(cube[side_idx][piece_idx], "fill") == 'white':
                if side_idx == 0:
                    rotate_right(window, cube)
                    rotate_right(window, cube)
                elif side_idx == 1:
                    rotate_right(window, cube)
                elif side_idx == 2:
                    rotate_cube_right(window, cube)
                    rotate_right(window, cube)
                elif side_idx == 3:
                    rotate_cube_right(window, cube)
                    rotate_cube_right(window, cube)
                    rotate_right(window, cube)
                elif side_idx == 4:
                    rotate_cube_right(window, cube)
                    rotate_cube_right(window, cube)
                    rotate_cube_right(window, cube)
                    rotate_right(window, cube)
            elif piece_idx == 7 and window.itemcget(cube[side_idx][piece_idx], "fill") == 'white':
                if side_idx == 0:
                    rotate_front(window, cube)
                    rotate_front(window, cube)
                elif side_idx == 1:
                    rotate_front_prime(window, cube)
                    rotate_right(window, cube)
                elif side_idx == 2:
                    rotate_cube_right(window, cube)
                    rotate_front_prime(window, cube)
                    rotate_right(window, cube)
                elif side_idx == 3:
                    rotate_cube_right(window, cube)
                    rotate_cube_right(window, cube)
                    rotate_front_prime(window, cube)
                    rotate_right(window, cube)
                elif side_idx == 4:
                    rotate_cube_right(window, cube)
                    rotate_cube_right(window, cube)
                    rotate_cube_right(window, cube)
                    rotate_front_prime(window, cube)
                    rotate_right(window, cube)



"""
def solve_white_cross(window, cube):
    #   init membervariables
    up_white = cube[None][None]
    up_secondary_color = None
    up_white_side = None
    left_white = cube[None][None]
    left_secondary_color = None
    left_white_side = None
    right_white = cube[None][None]
    right_secondary_color = None
    down_white = cube[None][None]
    down_secondary_color = None
    down_white_side = None
    #   finde alle weissen Kantensteine + die dazugehoerige Farbe
    for side_idx, side in enumerate(cube):
        for piece_idx in enumerate(side):
            if piece_idx == 1 and window.itemcget(cube[side_idx][piece_idx], "fill") == 'white':
                up_white = cube[side_idx][piece_idx]
                up_white_side = side_idx
                middle_piece_color = window.itemcget(cube[side_idx][4], "fill")
                if middle_piece_color == 'red':
                    up_secondary_color = window.itemcget(cube[0][7], "fill")
                elif middle_piece_color == 'green':
                    up_secondary_color = window.itemcget(cube[0][5], "fill")
                elif middle_piece_color == 'orange':
                    up_secondary_color = window.itemcget(cube[0][1], "fill")
                elif middle_piece_color == 'blue':
                    up_secondary_color = window.itemcget(cube[0][3], "fill")
                elif middle_piece_color == 'yellow':
                    up_secondary_color = window.itemcget(cube[3][1], "fill")
                elif middle_piece_color == 'white':
                    up_secondary_color = window.itemcget(cube[1][7], "fill")
            elif piece_idx == 3 and window.itemcget(cube[side_idx][piece_idx], "fill") == 'white':
                left_white = cube[side_idx][piece_idx]
                left_white_side = side_idx
                middle_piece_color = window.itemcget(cube[side_idx][4], "fill")
                if middle_piece_color == 'red':
                    left_secondary_color = window.itemcget(cube[4][5], "fill")
                elif middle_piece_color == 'green':
                    left_secondary_color = window.itemcget(cube[1][5], "fill")
                elif middle_piece_color == 'orange':
                    left_secondary_color = window.itemcget(cube[2][5], "fill")
                elif middle_piece_color == 'blue':
                    left_secondary_color = window.itemcget(cube[3][5], "fill")
                elif middle_piece_color == 'yellow':
                    left_secondary_color = window.itemcget(cube[4][1], "fill")
                elif middle_piece_color == 'white':
                    left_secondary_color = window.itemcget(cube[4][7], "fill")
            elif piece_idx == 5 and window.itemcget(cube[side_idx][piece_idx], "fill") == 'white':
                right_white = cube[side_idx][piece_idx]
                middle_piece_color = window.itemcget(cube[side_idx][4], "fill")
                if middle_piece_color == 'red':
                    right_secondary_color = window.itemcget(cube[2][3], "fill")
                elif middle_piece_color == 'green':
                    right_secondary_color = window.itemcget(cube[3][3], "fill")
                elif middle_piece_color == 'orange':
                    right_secondary_color = window.itemcget(cube[4][3], "fill")
                elif middle_piece_color == 'blue':
                    right_secondary_color = window.itemcget(cube[1][3], "fill")
                elif middle_piece_color == 'yellow':
                    right_secondary_color = window.itemcget(cube[2][1], "fill")
                elif middle_piece_color == 'white':
                    right_secondary_color = window.itemcget(cube[2][7], "fill")
            elif piece_idx == 7 and window.itemcget(cube[side_idx][piece_idx], "fill") == 'white':
                down_white = cube[side_idx][piece_idx]
                down_white_side = side_idx
                middle_piece_color = window.itemcget(cube[side_idx][4], "fill")
                if middle_piece_color == 'red':
                    down_secondary_color = window.itemcget(cube[5][1], "fill")
                elif middle_piece_color == 'green':
                    down_secondary_color = window.itemcget(cube[5][5], "fill")
                elif middle_piece_color == 'orange':
                    down_secondary_color = window.itemcget(cube[5][7], "fill")
                elif middle_piece_color == 'blue':
                    down_secondary_color = window.itemcget(cube[5][3], "fill")
                elif middle_piece_color == 'yellow':
                    down_secondary_color = window.itemcget(cube[1][1], "fill")
                elif middle_piece_color == 'white':
                    down_secondary_color = window.itemcget(cube[3][7], "fill")
    #   setze paarweise die Kantensteine ein
    if up_white_side == 0:
        rotate_back(window, cube)
        rotate_right(window, cube)
        rotate_right(window, cube)
        rotate_front_prime(window, cube)
    elif up_white_side == 1:
        rotate_up(window, cube)
        rotate_right(window, cube)
        rotate_front_prime(window, cube)
    elif up_white_side == 2:
        rotate_up(window, cube)
        rotate_up(window, cube)
        rotate_right(window, cube)
        rotate_front_prime(window, cube)
    elif up_white_side == 3:
        rotate_up_prime(window, cube)
        rotate_right(window, cube)
        rotate_front_prime(window, cube)
    elif up_white_side == 4:
        rotate_right(window, cube)
        rotate_front_prime(window, cube)
        #   bei 5 sollte er schon richtig seien

    if down_white_side == 0:
        rotate_up(window, cube)
        rotate_up(window, cube)
        rotate_back(window, cube)
        rotate_back(window, cube)
    elif down_white_side == 1:
        rotate_up(window, cube)
        rotate_right(window, cube)
        rotate_front_prime(window, cube)
    elif down_white_side == 2:
        rotate_up(window, cube)
        rotate_up(window, cube)
        rotate_right(window, cube)
        rotate_front_prime(window, cube)
    elif down_white_side == 3:
        rotate_up_prime(window, cube)
        rotate_right(window, cube)
        rotate_front_prime(window, cube)
    elif down_white_side == 4:
        rotate_right(window, cube)
        rotate_front_prime(window, cube)
"""





