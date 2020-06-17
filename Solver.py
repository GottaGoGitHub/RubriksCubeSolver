from RubriksCubeSolver.Cube import *


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


def solve_white_cross(window, cube):
    for side_idx, side in enumerate(cube):
        for piece_idx in enumerate(side):
            if piece_idx == 1 and window.itemcget(cube[side_idx][piece_idx], "fill") == 'white':
                print("ich habe einen weißen stein gefunden juhuuu!")
