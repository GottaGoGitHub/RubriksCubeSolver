# from RubriksCubeSolver.Cube import *
from Cube import *
import random


# random scrambling
def scramble(cubies, id_array):
    for _ in range(50):
        temp = random.randrange(6)

        if temp == 0:
            rotate_down_cubies(cubies, id_array)

        if temp == 1:
            rotate_left_cubies(cubies, id_array)

        if temp == 2:
            rotate_front_cubies(cubies, id_array)

        if temp == 3:
            rotate_right_cubies(cubies, id_array)

        if temp == 4:
            rotate_back_cubies(cubies, id_array)

        if temp == 5:
            rotate_up_cubies(cubies, id_array)


#   R U R' U'
def ruru(cubies, id_array):
    rotate_right_cubies(cubies, id_array)
    rotate_up_cubies(cubies, id_array)
    rotate_right_prime_cubies(cubies, id_array)
    rotate_up_prime_cubies(cubies, id_array)


#   L U' L' U
def lulu(cubies, id_array):
    rotate_left_cubies(cubies, id_array)
    rotate_up_prime_cubies(cubies, id_array)
    rotate_left_prime_cubies(cubies, id_array)
    rotate_up_cubies(cubies, id_array)


#   U R U R' U' y L U' L' U
def second_layer_right(cubies, id_array):
    rotate_up_cubies(cubies, id_array)
    ruru(cubies, id_array)
    rotate_cube_right_cubies(cubies, id_array)
    lulu(cubies, id_array)


#   U' L U' L' U y' R U R' U'
def second_layer_left(cubies, id_array):
    rotate_up_prime_cubies(cubies, id_array)
    lulu(cubies, id_array)
    rotate_cube_left_cubies(cubies, id_array)
    ruru(cubies, id_array)


#   F R U R' U' F'
def top_cross(cubies, id_array):
    rotate_front_cubies(cubies, id_array)
    ruru(cubies, id_array)
    rotate_front_prime_cubies(cubies, id_array)


#   R U R' U R 2U' R'
def correct_front(cubies, id_array):
    rotate_right_cubies(cubies, id_array)
    rotate_up_cubies(cubies, id_array)
    rotate_right_prime_cubies(cubies, id_array)
    rotate_up_cubies(cubies, id_array)
    rotate_right_cubies(cubies, id_array)
    rotate_up_prime_cubies(cubies, id_array)
    rotate_up_prime_cubies(cubies, id_array)
    rotate_right_prime_cubies(cubies, id_array)


#   U R U' L U R' U' L'
def sort_corners(cubies, id_array):
    rotate_up_cubies(cubies, id_array)
    rotate_right_cubies(cubies, id_array)
    rotate_up_prime_cubies(cubies, id_array)
    rotate_left_cubies(cubies, id_array)
    rotate_up_cubies(cubies, id_array)
    rotate_right_prime_cubies(cubies, id_array)
    rotate_up_prime_cubies(cubies, id_array)
    rotate_left_prime_cubies(cubies, id_array)


def is_in_layer(id_array, layer, cubie_name):
    temp = []

    if layer == 1:
        for item in id_array[0]:
            temp1 = item.rpartition("0")
            temp.append(temp1[0])

    if layer == 3:
        for item in id_array[5]:
            temp1 = item.rpartition("0")
            temp.append(temp1[0])

    if layer == 2:
        temp2 = id_array[1][3].rpartition("0")
        temp3 = id_array[1][5].rpartition("0")
        temp4 = id_array[3][3].rpartition("0")
        temp5 = id_array[3][5].rpartition("0")
        temp = [temp2[0], temp3[0], temp4[0], temp5[0]]

    return str(cubie_name) in temp


def flip_orientation_of_edge_in_first_layer(cubies, id_array, index):
    temp = [0, 2, 4, 6, 8]
    if index in temp:
        print("Invalid index.")
    else:
        if 1 == index:
            rotate_cube_right_cubies(cubies, id_array)
            rotate_cube_right_cubies(cubies, id_array)

        if 3 == index:
            rotate_cube_right_cubies(cubies, id_array)

        if 5 == index:
            rotate_cube_left_cubies(cubies, id_array)

        rotate_front_cubies(cubies, id_array)
        rotate_right_prime_cubies(cubies, id_array)
        rotate_down_prime_cubies(cubies, id_array)
        rotate_right_cubies(cubies, id_array)
        rotate_front_cubies(cubies, id_array)
        rotate_front_cubies(cubies, id_array)


def white_cross(cubies, id_array):
    # insert cubie 14
    if cubies[13].pos2[0] != 5:
        if is_in_layer(id_array, 3, 14):
            rotate_prime_by_side_idx(cubies, id_array, cubies[13].pos2[0])
            rotate_prime_by_side_idx(cubies, id_array, cubies[13].pos1[0])

        elif cubies[13].pos2[0] == 0 or is_in_layer(id_array, 2, 14):
            while cubies[13].pos1[1] != 7:
                rotate_by_side_idx(cubies, id_array, cubies[13].pos1[0])

        elif cubies[13].pos2[0] != 0 and is_in_layer(id_array, 1, 14):
            rotate_by_side_idx(cubies, id_array, cubies[13].pos2[0])
            rotate_prime_by_side_idx(cubies, id_array, cubies[13].pos1[0])

    # rotate the down side until cubie 14 is at index 3
    while cubies[13].pos2[1] != 3:
        rotate_down_cubies(cubies, id_array)

    # insert cubie 18
    # if cubie 18 is in second layer
    if is_in_layer(id_array, 2, 18):
        if id_array[cubies[17].pos1[0]][7] == cubies[13].id1:
            rotate_down_prime_cubies(cubies, id_array)
            rotate_by_side_idx(cubies, id_array, cubies[17].pos1[0])
        else:
            if 1 == cubies[17].pos1[0]:
                while cubies[13].pos2[1] != 3:
                    rotate_down_cubies(cubies, id_array)

            if 2 == cubies[17].pos1[0]:
                while cubies[13].pos2[1] != 1:
                    rotate_down_cubies(cubies, id_array)

            if 3 == cubies[17].pos1[0]:
                while cubies[13].pos2[1] != 5:
                    rotate_down_cubies(cubies, id_array)

            if 4 == cubies[17].pos1[0]:
                while cubies[13].pos2[1] != 7:
                    rotate_down_cubies(cubies, id_array)

            rotate_by_side_idx(cubies, id_array, cubies[17].pos1[0])

    # if cubie 18 is in first layer but the white face is not at the yellow side
    if cubies[17].pos2[0] != 0 and is_in_layer(id_array, 1, 18):
        if id_array[cubies[17].pos1[0]][7] == cubies[13].id1:
            rotate_down_prime_cubies(cubies, id_array)
            rotate_by_side_idx(cubies, id_array, cubies[17].pos2[0])
            rotate_down_cubies(cubies, id_array)
            rotate_prime_by_side_idx(cubies, id_array, cubies[17].pos1[0])
        else:
            rotate_by_side_idx(cubies, id_array, cubies[17].pos2[0])
            temp = -1
            if cubies[17].pos2[0] == 1:
                temp = 1
            elif cubies[17].pos2[0] == 2:
                temp = 5
            elif cubies[17].pos2[0] == 3:
                temp = 7
            elif cubies[17].pos2[0] == 4:
                temp = 3

            while cubies[13].pos2[1] != temp:
                rotate_down_cubies(cubies, id_array)

            rotate_prime_by_side_idx(cubies, id_array, cubies[17].pos1[0])

    # if the white side of cubie 18 is on the yellow face
    if 0 == cubies[17].pos2[0]:
        if 1 == cubies[17].pos2[1]:
            while cubies[13].pos2[1] != 5:
                rotate_down_cubies(cubies, id_array)

        if 3 == cubies[17].pos2[1]:
            while cubies[13].pos2[1] != 7:
                rotate_down_cubies(cubies, id_array)

        if 5 == cubies[17].pos2[1]:
            while cubies[13].pos2[1] != 1:
                rotate_down_cubies(cubies, id_array)

        if 7 == cubies[17].pos2[1]:
            while cubies[13].pos2[1] != 3:
                rotate_down_cubies(cubies, id_array)

        rotate_by_side_idx(cubies, id_array, cubies[17].pos1[0])
        rotate_by_side_idx(cubies, id_array, cubies[17].pos1[0])

    # rotate the down side until cubie 14 is at index 3
    while cubies[13].pos2[1] != 3:
        rotate_down_cubies(cubies, id_array)

    # if cubie 18 is in the third layer but the white face is not at the white side
    if 5 == cubies[17].pos1[0]:
        if 1 == cubies[17].pos1[1]:
            rotate_front_cubies(cubies, id_array)
            rotate_down_prime_cubies(cubies, id_array)
            rotate_left_cubies(cubies, id_array)
            rotate_down_cubies(cubies, id_array)

        elif 5 == cubies[17].pos1[1]:
            rotate_right_cubies(cubies, id_array)
            rotate_front_cubies(cubies, id_array)

        elif 7 == cubies[17].pos1[1]:
            rotate_back_cubies(cubies, id_array)
            rotate_down_cubies(cubies, id_array)
            rotate_right_cubies(cubies, id_array)
            rotate_down_prime_cubies(cubies, id_array)

    # if cubie 18 is in the third layer and the white face is at the white side
    if 5 == cubies[17].pos2[0]:
        if 5 == cubies[17].pos2[1]:
            rotate_right_cubies(cubies, id_array)
            rotate_right_cubies(cubies, id_array)
            rotate_up_cubies(cubies, id_array)
            rotate_front_cubies(cubies, id_array)
            rotate_front_cubies(cubies, id_array)

        elif 7 == cubies[17].pos2[1]:
            rotate_back_cubies(cubies, id_array)
            rotate_back_cubies(cubies, id_array)
            rotate_up_cubies(cubies, id_array)
            rotate_up_cubies(cubies, id_array)
            rotate_front_cubies(cubies, id_array)
            rotate_front_cubies(cubies, id_array)

# insert cubie 22
    # if cubie 22 is in the second layer
    if is_in_layer(id_array, 2, 22):
        temp = cubies[21].pos2[0]
        if cubies[21].pos2[1] == 3:
            rotate_by_side_idx(cubies, id_array, temp)
        elif cubies[21].pos2[1] == 5:
            rotate_prime_by_side_idx(cubies, id_array, temp)

        while 7 != cubies[21].pos1[1]:
            rotate_up_cubies(cubies, id_array)

        rotate_front_cubies(cubies, id_array)
        rotate_right_prime_cubies(cubies, id_array)
        rotate_front_prime_cubies(cubies, id_array)

        # if cubie 22 was at the front or left side, cubie 14 will be affected by the rotation, which has to be undone
        while cubies[17].pos1[1] != 7:
            rotate_front_cubies(cubies, id_array)

        while cubies[13].pos1[1] != 7:
            rotate_left_prime_cubies(cubies, id_array)


    # if cubie 22 is in the first layer and the white face is not at the yellow side (up)
    if is_in_layer(id_array, 1, 22) and cubies[21].pos2[0] != 0:
        while 7 != cubies[21].pos1[1]:
            rotate_up_cubies(cubies, id_array)

        rotate_front_cubies(cubies, id_array)
        rotate_right_prime_cubies(cubies, id_array)
        rotate_front_prime_cubies(cubies, id_array)

    # if cubie 22 is in the first layer and the white face is at the yellow side (up)
    if cubies[21].pos2[0] == 0:
        while 5 != cubies[21].pos2[1]:
            rotate_up_cubies(cubies, id_array)

        rotate_right_cubies(cubies, id_array)
        rotate_right_cubies(cubies, id_array)

    # if cubie 22 is in the thrid layer
    if is_in_layer(id_array, 3, 22):
        if cubies[21].pos2 == [3, 7]:
            rotate_back_cubies(cubies, id_array)
            rotate_right_cubies(cubies, id_array)

        if cubies[21].pos2 == [5, 7]:
            rotate_back_cubies(cubies, id_array)
            rotate_back_cubies(cubies, id_array)
            rotate_up_cubies(cubies, id_array)
            rotate_right_cubies(cubies, id_array)
            rotate_right_cubies(cubies, id_array)

        if cubies[21].pos2 == [2, 7]:
            rotate_right_cubies(cubies, id_array)
            rotate_right_cubies(cubies, id_array)
            rotate_up_cubies(cubies, id_array)
            rotate_front_cubies(cubies, id_array)
            rotate_right_prime_cubies(cubies, id_array)
            rotate_front_prime_cubies(cubies, id_array)

    # insert cubie 25
    # if cubie 25 is in the second layer
    if is_in_layer(id_array, 2, 25):
        if cubies[24].pos1 == [3, 3]:
            rotate_back_prime_cubies(cubies, id_array)
        elif cubies[24].pos2[0] == 4 and cubies[24].pos2[1] == 3:
            rotate_back_cubies(cubies, id_array)
        else:
            temp = cubies[24].pos1

            if 3 == temp[1]:
                rotate_by_side_idx(cubies, id_array, temp[0])
            elif 5 == temp[1]:
                rotate_prime_by_side_idx(cubies, id_array, temp[0])

            while 1 != cubies[24].pos2[1]:
                rotate_up_cubies(cubies, id_array)

            if 3 == temp[1]:
                rotate_prime_by_side_idx(cubies, id_array, temp[0])
            elif 5 == temp[1]:
                rotate_by_side_idx(cubies, id_array, temp[0])

            rotate_back_cubies(cubies, id_array)
            rotate_back_cubies(cubies, id_array)

    # if cubie 25 is in the first layer and the white face is on the yellow side
    if cubies[24].pos2[0] == 0:
        while 1 != cubies[24].pos2[1]:
            rotate_up_cubies(cubies, id_array)

        rotate_back_cubies(cubies, id_array)
        rotate_back_cubies(cubies, id_array)

    # if cubie 25 is in the first layer and the white face is not on the yellow side
    if is_in_layer(id_array, 1, 25) and cubies[24].pos2[0] != 0:
        while 1 != cubies[24].pos1[1]:
            rotate_up_cubies(cubies, id_array)

        rotate_back_prime_cubies(cubies, id_array)
        rotate_down_prime_cubies(cubies, id_array)
        rotate_right_cubies(cubies, id_array)
        rotate_down_cubies(cubies, id_array)

    # if cubie 25 is already at the right spot but flipped
    if cubies[24].pos2 == [3, 7]:
        rotate_cube_up_cubies(cubies, id_array)
        rotate_cube_up_cubies(cubies, id_array)
        flip_orientation_of_edge_in_first_layer(cubies, id_array, 7)
        rotate_cube_up_cubies(cubies, id_array)
        rotate_cube_up_cubies(cubies, id_array)

