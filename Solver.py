# from RubriksCubeSolver.Cube import *
from Cube import *
import random


# random scrambling
def scramble(cubies, id_array, rotations):
    for _ in range(50):
        temp = random.randrange(6)

        if temp == 0:
            rotate_down_cubies(cubies, id_array, rotations)

        if temp == 1:
            rotate_left_cubies(cubies, id_array, rotations)

        if temp == 2:
            rotate_front_cubies(cubies, id_array, rotations)

        if temp == 3:
            rotate_right_cubies(cubies, id_array, rotations)

        if temp == 4:
            rotate_back_cubies(cubies, id_array, rotations)

        if temp == 5:
            rotate_up_cubies(cubies, id_array, rotations)


#   R U R' U'
def ruru(cubies, id_array, rotations):
    rotate_right_cubies(cubies, id_array, rotations)
    rotate_up_cubies(cubies, id_array, rotations)
    rotate_right_prime_cubies(cubies, id_array, rotations)
    rotate_up_prime_cubies(cubies, id_array, rotations)


#   L' U' L U
def lulu(cubies, id_array, rotations):
    rotate_left_prime_cubies(cubies, id_array, rotations)
    rotate_up_prime_cubies(cubies, id_array, rotations)
    rotate_left_cubies(cubies, id_array, rotations)
    rotate_up_cubies(cubies, id_array, rotations)


#   U R U R' U' y L U' L' U
def second_layer_right(cubies, id_array, rotations):
    rotate_up_cubies(cubies, id_array, rotations)
    ruru(cubies, id_array, rotations)
    rotate_cube_left_cubies(cubies, id_array, rotations)
    lulu(cubies, id_array, rotations)
    rotate_cube_right_cubies(cubies, id_array, rotations)


#   U' L U' L' U y' R U R' U'
def second_layer_left(cubies, id_array, rotations):
    rotate_up_prime_cubies(cubies, id_array, rotations)
    lulu(cubies, id_array, rotations)
    rotate_cube_right_cubies(cubies, id_array, rotations)
    ruru(cubies, id_array, rotations)
    rotate_cube_left_cubies(cubies, id_array, rotations)


#   F R U R' U' F'
def fruruf(cubies, id_array, rotations):
    rotate_front_cubies(cubies, id_array, rotations)
    ruru(cubies, id_array, rotations)
    rotate_front_prime_cubies(cubies, id_array, rotations)


#   R U R' U R 2U' R'
def correct_front(cubies, id_array, rotations):
    rotate_right_cubies(cubies, id_array, rotations)
    rotate_up_cubies(cubies, id_array, rotations)
    rotate_right_prime_cubies(cubies, id_array, rotations)
    rotate_up_cubies(cubies, id_array, rotations)
    rotate_right_cubies(cubies, id_array, rotations)
    rotate_up_prime_cubies(cubies, id_array, rotations)
    rotate_up_prime_cubies(cubies, id_array, rotations)
    rotate_right_prime_cubies(cubies, id_array, rotations)


#   U R U' L U R' U' L'
def sort_corners_algorithm(cubies, id_array, rotations):
    rotate_up_cubies(cubies, id_array, rotations)
    rotate_right_cubies(cubies, id_array, rotations)
    rotate_up_prime_cubies(cubies, id_array, rotations)
    rotate_left_prime_cubies(cubies, id_array, rotations)
    rotate_up_cubies(cubies, id_array, rotations)
    rotate_right_prime_cubies(cubies, id_array, rotations)
    rotate_up_prime_cubies(cubies, id_array, rotations)
    rotate_left_cubies(cubies, id_array, rotations)


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


def flip_orientation_of_edge_in_first_layer(cubies, id_array, index, rotations):
    temp = [0, 2, 4, 6, 8]
    if index in temp:
        print("Invalid index.")
    else:
        if 1 == index:
            rotate_cube_right_cubies(cubies, id_array, rotations)
            rotate_cube_right_cubies(cubies, id_array, rotations)

        if 3 == index:
            rotate_cube_right_cubies(cubies, id_array, rotations)

        if 5 == index:
            rotate_cube_left_cubies(cubies, id_array, rotations)

        rotate_front_cubies(cubies, id_array, rotations)
        rotate_right_prime_cubies(cubies, id_array, rotations)
        rotate_down_prime_cubies(cubies, id_array, rotations)
        rotate_right_cubies(cubies, id_array, rotations)
        rotate_front_cubies(cubies, id_array, rotations)
        rotate_front_cubies(cubies, id_array, rotations)


def white_cross(cubies, id_array, rotations):
    # insert cubie 14
    #
    # When the cube is scrambled, the first necessary cubie can be in either the first,
    # second or already in the thrid layer of the cube.
    # First of all its checked in which of the three layers it is and then
    # it will be correctly oriented brought to the third layer.
    #
    if cubies[13].pos2[0] != 5:
        if is_in_layer(id_array, 3, 14):
            rotate_prime_by_side_idx(cubies, id_array, cubies[13].pos2[0], rotations)
            rotate_prime_by_side_idx(cubies, id_array, cubies[13].pos1[0], rotations)

        elif cubies[13].pos2[0] == 0 or is_in_layer(id_array, 2, 14):
            while cubies[13].pos1[1] != 7:
                rotate_by_side_idx(cubies, id_array, cubies[13].pos1[0], rotations)

        elif cubies[13].pos2[0] != 0 and is_in_layer(id_array, 1, 14):
            rotate_by_side_idx(cubies, id_array, cubies[13].pos2[0], rotations)
            rotate_prime_by_side_idx(cubies, id_array, cubies[13].pos1[0], rotations)

    # rotate the down side until cubie 14 is at index 3
    #
    # Correcting the positioning, so that the following cubies will be in correct order
    #
    while cubies[13].pos2[1] != 3:
        rotate_down_cubies(cubies, id_array, rotations)

    # insert cubie 18
    #
    # If cubie 18 is in the second layer it can be easily rotated down to the "white side"
    # The already inserted cubie 14 shall be rotated if the rotation of cubie 18 would affect its
    # positioning. Afterwards cubie 18 will be inserted in correct order.
    #
    if is_in_layer(id_array, 2, 18):
        if id_array[cubies[17].pos1[0]][7] == cubies[13].id1:
            rotate_down_prime_cubies(cubies, id_array, rotations)
            rotate_by_side_idx(cubies, id_array, cubies[17].pos1[0], rotations)
        else:
            if 1 == cubies[17].pos1[0]:
                while cubies[13].pos2[1] != 3:
                    rotate_down_cubies(cubies, id_array, rotations)

            if 2 == cubies[17].pos1[0]:
                while cubies[13].pos2[1] != 1:
                    rotate_down_cubies(cubies, id_array, rotations)

            if 3 == cubies[17].pos1[0]:
                while cubies[13].pos2[1] != 5:
                    rotate_down_cubies(cubies, id_array, rotations)

            if 4 == cubies[17].pos1[0]:
                while cubies[13].pos2[1] != 7:
                    rotate_down_cubies(cubies, id_array, rotations)

            rotate_by_side_idx(cubies, id_array, cubies[17].pos1[0], rotations)

    #
    # If cubie 18 is in first layer but the "white face" is not at the "yellow side" (up):
    #
    # If the insertion of cubie 18 should affect the inserted cubie 14 it shall be inserted without
    # removing the correct cubie. Else the cubie will be inserted by rotating the side with the white
    # side of cubie 18, rotating down until its at the correct place and rotating side with the white
    # side of cubie 18 yet again.
    #
    if cubies[17].pos2[0] != 0 and is_in_layer(id_array, 1, 18):
        if id_array[cubies[17].pos1[0]][7] == cubies[13].id1:
            rotate_down_prime_cubies(cubies, id_array, rotations)
            rotate_by_side_idx(cubies, id_array, cubies[17].pos2[0], rotations)
            rotate_down_cubies(cubies, id_array, rotations)
            rotate_prime_by_side_idx(cubies, id_array, cubies[17].pos1[0], rotations)
        else:
            rotate_by_side_idx(cubies, id_array, cubies[17].pos2[0], rotations)
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
                rotate_down_cubies(cubies, id_array, rotations)

            rotate_prime_by_side_idx(cubies, id_array, cubies[17].pos1[0], rotations)
    #
    # if the white side of cubie 18 is on the yellow face, down will be rotated until
    # the cubie can be inserted by two simple rotations of the side where the red face of cubie 18 is
    #
    if 0 == cubies[17].pos2[0]:
        if 1 == cubies[17].pos2[1]:
            while cubies[13].pos2[1] != 5:
                rotate_down_cubies(cubies, id_array, rotations)

        if 3 == cubies[17].pos2[1]:
            while cubies[13].pos2[1] != 7:
                rotate_down_cubies(cubies, id_array, rotations)

        if 5 == cubies[17].pos2[1]:
            while cubies[13].pos2[1] != 1:
                rotate_down_cubies(cubies, id_array, rotations)

        if 7 == cubies[17].pos2[1]:
            while cubies[13].pos2[1] != 3:
                rotate_down_cubies(cubies, id_array, rotations)

        rotate_by_side_idx(cubies, id_array, cubies[17].pos1[0], rotations)
        rotate_by_side_idx(cubies, id_array, cubies[17].pos1[0], rotations)

    # rotate the down side until cubie 14 is at index 3
    #
    # Correcting the positioning, so that the following cubies will be in correct order
    #
    while cubies[13].pos2[1] != 3:
        rotate_down_cubies(cubies, id_array, rotations)

    #
    # Cubie 18 can be easily inserted if it is in the third layer but the white
    # face is not at the white side. With a few simple moves you can insert
    # the cubie correctly oriented into its slot
    #
    if 5 == cubies[17].pos1[0]:
        if 1 == cubies[17].pos1[1]:
            rotate_front_cubies(cubies, id_array, rotations)
            rotate_down_prime_cubies(cubies, id_array, rotations)
            rotate_left_cubies(cubies, id_array, rotations)
            rotate_down_cubies(cubies, id_array, rotations)

        elif 5 == cubies[17].pos1[1]:
            rotate_right_cubies(cubies, id_array, rotations)
            rotate_front_cubies(cubies, id_array, rotations)

        elif 7 == cubies[17].pos1[1]:
            rotate_back_cubies(cubies, id_array, rotations)
            rotate_down_cubies(cubies, id_array, rotations)
            rotate_right_cubies(cubies, id_array, rotations)
            rotate_down_prime_cubies(cubies, id_array, rotations)

    #
    # if cubie 18 is in the third layer and the white face is at the white side
    # then you need to correct its position and/or its orientation
    # the position of cubie 14 can be ignored but should not be affected
    #
    if 5 == cubies[17].pos2[0]:
        if 5 == cubies[17].pos2[1]:
            rotate_right_cubies(cubies, id_array, rotations)
            rotate_right_cubies(cubies, id_array, rotations)
            rotate_up_cubies(cubies, id_array, rotations)
            rotate_front_cubies(cubies, id_array, rotations)
            rotate_front_cubies(cubies, id_array, rotations)

        elif 7 == cubies[17].pos2[1]:
            rotate_back_cubies(cubies, id_array, rotations)
            rotate_back_cubies(cubies, id_array, rotations)
            rotate_up_cubies(cubies, id_array, rotations)
            rotate_up_cubies(cubies, id_array, rotations)
            rotate_front_cubies(cubies, id_array, rotations)
            rotate_front_cubies(cubies, id_array, rotations)

    # insert cubie 22
    # if cubie 22 is in the second layer
    # same as 18 but with corrections if 14 or 18 is affected
    #
    if is_in_layer(id_array, 2, 22):
        temp = cubies[21].pos2[0]
        if cubies[21].pos2[1] == 3:
            rotate_by_side_idx(cubies, id_array, temp, rotations)
        elif cubies[21].pos2[1] == 5:
            rotate_prime_by_side_idx(cubies, id_array, temp, rotations)

        while 7 != cubies[21].pos1[1]:
            rotate_up_cubies(cubies, id_array, rotations)

        rotate_front_cubies(cubies, id_array, rotations)
        rotate_right_prime_cubies(cubies, id_array, rotations)
        rotate_front_prime_cubies(cubies, id_array, rotations)

        #
        # if cubie 22 was at the front or left side, cubie 14 will be affected by the rotation, which has to be undone
        #
        while cubies[17].pos1[1] != 7:
            rotate_front_cubies(cubies, id_array, rotations)

        while cubies[13].pos1[1] != 7:
            rotate_left_prime_cubies(cubies, id_array, rotations)

    #
    # if cubie 22 is in the first layer and the white face is not at the yellow side (up)
    #
    if is_in_layer(id_array, 1, 22) and cubies[21].pos2[0] != 0:
        while 7 != cubies[21].pos1[1]:
            rotate_up_cubies(cubies, id_array, rotations)

        rotate_front_cubies(cubies, id_array, rotations)
        rotate_right_prime_cubies(cubies, id_array, rotations)
        rotate_front_prime_cubies(cubies, id_array, rotations)

    #
    # if cubie 22 is in the first layer and the white face is at the yellow side (up)
    #
    if cubies[21].pos2[0] == 0:
        while 5 != cubies[21].pos2[1]:
            rotate_up_cubies(cubies, id_array, rotations)

        rotate_right_cubies(cubies, id_array, rotations)
        rotate_right_cubies(cubies, id_array, rotations)

    #
    # if cubie 22 is in the third layer
    #
    if is_in_layer(id_array, 3, 22):
        if cubies[21].pos2 == [3, 7]:
            rotate_back_cubies(cubies, id_array, rotations)
            rotate_right_cubies(cubies, id_array, rotations)

        if cubies[21].pos2 == [5, 7]:
            rotate_back_cubies(cubies, id_array, rotations)
            rotate_back_cubies(cubies, id_array, rotations)
            rotate_up_cubies(cubies, id_array, rotations)
            rotate_right_cubies(cubies, id_array, rotations)
            rotate_right_cubies(cubies, id_array, rotations)

        if cubies[21].pos2 == [2, 7]:
            rotate_right_cubies(cubies, id_array, rotations)
            rotate_right_cubies(cubies, id_array, rotations)
            rotate_up_cubies(cubies, id_array, rotations)
            rotate_front_cubies(cubies, id_array, rotations)
            rotate_right_prime_cubies(cubies, id_array, rotations)
            rotate_front_prime_cubies(cubies, id_array, rotations)

    # insert cubie 25
    # if cubie 25 is in the second layer
    #
    if is_in_layer(id_array, 2, 25):
        if cubies[24].pos1 == [3, 3]:
            rotate_back_prime_cubies(cubies, id_array, rotations)
        elif cubies[24].pos2[0] == 4 and cubies[24].pos2[1] == 3:
            rotate_back_cubies(cubies, id_array, rotations)
        else:
            temp = cubies[24].pos1

            if 3 == temp[1]:
                rotate_by_side_idx(cubies, id_array, temp[0], rotations)
            elif 5 == temp[1]:
                rotate_prime_by_side_idx(cubies, id_array, temp[0], rotations)

            while 1 != cubies[24].pos2[1]:
                rotate_up_cubies(cubies, id_array, rotations)

            if 3 == temp[1]:
                rotate_prime_by_side_idx(cubies, id_array, temp[0], rotations)
            elif 5 == temp[1]:
                rotate_by_side_idx(cubies, id_array, temp[0], rotations)

            rotate_back_cubies(cubies, id_array, rotations)
            rotate_back_cubies(cubies, id_array, rotations)

    #
    # if cubie 25 is in the first layer and the white face is on the yellow side
    #
    if cubies[24].pos2[0] == 0:
        while 1 != cubies[24].pos2[1]:
            rotate_up_cubies(cubies, id_array, rotations)

        rotate_back_cubies(cubies, id_array, rotations)
        rotate_back_cubies(cubies, id_array, rotations)

    #
    # if cubie 25 is in the first layer and the white face is not on the yellow side
    #
    if is_in_layer(id_array, 1, 25) and cubies[24].pos2[0] != 0:
        while 1 != cubies[24].pos1[1]:
            rotate_up_cubies(cubies, id_array, rotations)

        rotate_back_prime_cubies(cubies, id_array, rotations)
        rotate_down_prime_cubies(cubies, id_array, rotations)
        rotate_right_cubies(cubies, id_array, rotations)
        rotate_down_cubies(cubies, id_array, rotations)

    #
    # if cubie 25 is already at the right spot but flipped
    #
    if cubies[24].pos2 == [3, 7]:
        rotate_cube_up_cubies(cubies, id_array, rotations)
        rotate_cube_up_cubies(cubies, id_array, rotations)
        flip_orientation_of_edge_in_first_layer(cubies, id_array, 7, rotations)
        rotate_cube_up_cubies(cubies, id_array, rotations)
        rotate_cube_up_cubies(cubies, id_array, rotations)


def white_corners(cubies, id_array, rotations):
    """
    Inserts cubie 13, 15, 19 and 23 to their intended places.
    """
    # insert cubie 15
    # blue, red, white
    #
    # First we swap cubie 15 from 3rd layer in 1st layer.
    # There are 4 possibilities, where cubie 15 can be in the 3rd layer.
    #

    if is_in_layer(id_array, 3, 15):
        if id_array[5][2].rpartition("0")[0] == "15":
            ruru(cubies, id_array, rotations)
        
        if id_array[5][6].rpartition("0")[0] == "15":
            rotate_cube_right_cubies(cubies, id_array, rotations)
            lulu(cubies, id_array, rotations)
            rotate_cube_left_cubies(cubies, id_array, rotations)

        if id_array[5][8].rpartition("0")[0] == "15":
            rotate_cube_left_cubies(cubies, id_array, rotations)
            ruru(cubies, id_array, rotations)
            rotate_cube_right_cubies(cubies, id_array, rotations)

        # if cubie 15 ist already at the right position, but swapped
        if id_array[5][0].rpartition("0")[0] == "15":
            while not (id_array[4][8] == "1501" and id_array[1][6] == "1502" and id_array[5][0] == "1503"):
                lulu(cubies, id_array, rotations)

    #
    # If cubie 15 is in the 1st layer, we rotate the up-side as long as
    # cubie 15 is not directly over the position in 3rd layer, where it
    # should be.
    # Then we use the "lulu"-algorithm to swap cubie 15 at it's right
    # position.
    #

    if is_in_layer(id_array, 1, 15):
        while id_array[0][6].rpartition("0")[0] != "15":
            rotate_up_cubies(cubies, id_array, rotations)

        while not (id_array[4][8] == "1501" and id_array[1][6] == "1502" and id_array[5][0] == "1503"):
            lulu(cubies, id_array, rotations)

    # insert cubie 19
    # red, green, white
    #
    # Now there are 3 possibilities where cubie 19 can be in the 3rd layer,
    # because cubie 15 is already inserted correctly.
    # We swap cubie 19 from 3rd layer to 1st layer too.
    #
    if is_in_layer(id_array, 3, 19):
        if id_array[5][6].rpartition("0")[0] == "19":
            rotate_cube_right_cubies(cubies, id_array, rotations)
            lulu(cubies, id_array, rotations)
            rotate_cube_left_cubies(cubies, id_array, rotations)

        if id_array[5][8].rpartition("0")[0] == "19":
            rotate_cube_left_cubies(cubies, id_array, rotations)
            ruru(cubies, id_array, rotations)
            rotate_cube_right_cubies(cubies, id_array, rotations)

        if id_array[5][2].rpartition("0")[0] == "19":
            while not (id_array[1][8] == "1901" and id_array[2][6] == "1902" and id_array[5][2] == "1903"):
                ruru(cubies, id_array, rotations)

    #
    # If cubie 19 is in the 1st layer, we rotate the up-side as long as
    # cubie 19 is not directly over the position in 3rd layer, where it
    # should be.
    # Then we use the "ruru"-algorithm to swap cubie 19 at it's right
    # position.
    #
    if is_in_layer(id_array, 1, 19):
        while id_array[0][8].rpartition("0")[0] != "19":
            rotate_up_cubies(cubies, id_array, rotations)
        
        while not (id_array[1][8] == "1901" and id_array[2][6] == "1902" and id_array[5][2] == "1903"):
                ruru(cubies, id_array, rotations)
        

    # insert cubie 23
    # green, orange, white
    #
    # Now there are 2 possibilities where cubie 23 can be in the 3rd layer,
    # because cubie 15 and cubie 19 are already inserted correctly.
    # That we can use the "lulu" and "ruru"-algorithms, we have to rotate the
    # whole cube 2 times (rotate_cube_right_cubies()).
    # We swap cubie 23 from 3rd layer to 1st layer too.
    #

    rotate_cube_right_cubies(cubies, id_array, rotations)
    rotate_cube_right_cubies(cubies, id_array, rotations)

    if is_in_layer(id_array, 3, 23):
        if id_array[5][2].rpartition("0")[0] == "23":
            ruru(cubies, id_array, rotations)

        if id_array[5][0].rpartition("0")[0] == "23":
            while not (id_array[4][8] == "2301" and id_array[1][6] == "2302" and id_array[5][0] == "2303"):
                lulu(cubies, id_array, rotations)

    #
    # If cubie 23 is in the 1st layer, we rotate the up-side as long as
    # cubie 23 is not directly over the position in 3rd layer, where it
    # should be.
    # Then we use the "lulu"-algorithm to swap cubie 23 at it's right
    # position.
    #

    if is_in_layer(id_array, 1, 23):
        while id_array[0][6].rpartition("0")[0] != "23":
            rotate_up_cubies(cubies, id_array, rotations)

        while not (id_array[4][8] == "2301" and id_array[1][6] == "2302" and id_array[5][0] == "2303"):
            lulu(cubies, id_array, rotations)

    # insert cubie 13
    # blue, orange, white
    #
    # Now there is only 1 possibility left where cubie 13 can be in the 3rd layer,
    # because cubie 15, cubie 19 and cubie 23 are already inserted correctly.
    # We swap cubie 13 from 3rd layer to 1st layer too.
    # Then we use the "ruru"-algorithm to swap cubie 13 at it's right position.
    #

    if is_in_layer(id_array, 1, 13):
        while id_array[0][8].rpartition("0")[0] != "13":
            rotate_up_cubies(cubies, id_array, rotations)
        
    while not (id_array[1][8] == "1302" and id_array[2][6] == "1301" and id_array[5][2] == "1303"):
            ruru(cubies, id_array, rotations)

    #
    # We have to rotate the whole cube 2 times again, that we are at the same
    # position like at the beginning again.
    #

    rotate_cube_right_cubies(cubies, id_array, rotations)
    rotate_cube_right_cubies(cubies, id_array, rotations)


def second_layer(cubies, id_array, rotations):
    # alle verbliebenen cubies mit 2 Farben, die NICHT gelb als Teilfarbe haben

    # insert cubie 12
    # blue, red
    if is_in_layer(id_array, 2, 12):
        if id_array[1][3] == "1201":
            second_layer_left(cubies, id_array, rotations)

        elif id_array[1][5].rpartition("0")[0] == "12":
            second_layer_right(cubies, id_array, rotations)

        elif id_array[3][3].rpartition("0")[0] == "12":
            rotate_cube_left_cubies(cubies, id_array, rotations)
            rotate_cube_left_cubies(cubies, id_array, rotations)
            second_layer_left(cubies, id_array, rotations)
            rotate_cube_left_cubies(cubies, id_array, rotations)
            rotate_cube_left_cubies(cubies, id_array, rotations)

        elif id_array[3][5].rpartition("0")[0] == "12":
            rotate_cube_left_cubies(cubies, id_array, rotations)
            rotate_cube_left_cubies(cubies, id_array, rotations)
            second_layer_right(cubies, id_array, rotations)
            rotate_cube_left_cubies(cubies, id_array, rotations)
            rotate_cube_left_cubies(cubies, id_array, rotations)

    if is_in_layer(id_array, 1, 12):
        if cubies[11].pos1[0] == 0:
            while not (id_array[0][7] == "1201"):
                rotate_up_cubies(cubies, id_array, rotations)
            second_layer_left(cubies, id_array, rotations)

        else:
            while not (id_array[0][3] == "1202"):
                rotate_up_cubies(cubies, id_array, rotations)
            rotate_cube_right_cubies(cubies, id_array, rotations)
            second_layer_right(cubies, id_array, rotations)
            rotate_cube_left_cubies(cubies, id_array, rotations)


    # insert cubie 17
    # red, green
    if is_in_layer(id_array, 2, 17):
        if id_array[1][5] == "1702":
            second_layer_right(cubies, id_array, rotations)

        elif id_array[3][3].rpartition("0")[0] == "17":
            rotate_cube_left_cubies(cubies, id_array, rotations)
            rotate_cube_left_cubies(cubies, id_array, rotations)
            second_layer_left(cubies, id_array, rotations)
            rotate_cube_left_cubies(cubies, id_array, rotations)
            rotate_cube_left_cubies(cubies, id_array, rotations)

        elif id_array[3][5].rpartition("0")[0] == "17":
            rotate_cube_left_cubies(cubies, id_array, rotations)
            rotate_cube_left_cubies(cubies, id_array, rotations)
            second_layer_right(cubies, id_array, rotations)
            rotate_cube_left_cubies(cubies, id_array, rotations)
            rotate_cube_left_cubies(cubies, id_array, rotations)


    if is_in_layer(id_array, 1, 17):
        if cubies[16].pos2[0] == 0:
            while not (id_array[0][7] == "1702"):
                rotate_up_cubies(cubies, id_array, rotations)
            second_layer_right(cubies, id_array, rotations)

        else:
            while not (id_array[0][5] == "1701"):
                rotate_up_cubies(cubies, id_array, rotations)
            rotate_cube_left_cubies(cubies, id_array, rotations)
            second_layer_left(cubies, id_array, rotations)
            rotate_cube_right_cubies(cubies, id_array, rotations)


    # insert cubie 21
    # green, orange

    rotate_cube_right_cubies(cubies, id_array, rotations)
    rotate_cube_right_cubies(cubies, id_array, rotations)

    if id_array[1][3] == "2101":
        second_layer_left(cubies, id_array, rotations)

    elif id_array[1][5].rpartition("0")[0] == "21":
        second_layer_right(cubies, id_array, rotations)


    if is_in_layer(id_array, 1, 21):
        if cubies[20].pos1[0] == 0:
            while not (id_array[0][7] == "2101"):
                rotate_up_cubies(cubies, id_array, rotations)
            second_layer_left(cubies, id_array, rotations)

        else:
            while not (id_array[0][3] == "2102"):
                rotate_up_cubies(cubies, id_array, rotations)
            rotate_cube_right_cubies(cubies, id_array, rotations)
            second_layer_right(cubies, id_array, rotations)
            rotate_cube_left_cubies(cubies, id_array, rotations)
    

    # insert cubie 10
    # blue, orange

    if id_array[1][5] == "1001":
        second_layer_right(cubies, id_array, rotations)
    
    if cubies[9].pos1[0] == 0:
        while not (id_array[0][7] == "1001"):
            rotate_up_cubies(cubies, id_array, rotations)
        second_layer_right(cubies, id_array, rotations)

    else:
        while not (id_array[0][5] == "1002"):
            rotate_up_cubies(cubies, id_array, rotations)
        rotate_cube_left_cubies(cubies, id_array, rotations)
        second_layer_left(cubies, id_array, rotations)
        rotate_cube_right_cubies(cubies, id_array, rotations)

    rotate_cube_right_cubies(cubies, id_array, rotations)
    rotate_cube_right_cubies(cubies, id_array, rotations)


def top_cross(cubies, id_array, rotations):
    temp = False

    yellow_ids = ["0201", "0401", "0601", "0801"]

    # while not (id_array[0][1].rpartition("0")[2] == 1 and id_array[0][3].rpartition("0")[2] == 1 and
    #            id_array[0][5].rpartition("0")[2] == 1 and id_array[0][7].rpartition("0")[2] == 1):

    while not temp:

        if (id_array[0][1] in yellow_ids and id_array[0][3] in yellow_ids and
            id_array[0][5] in yellow_ids and id_array[0][7] in yellow_ids):
            temp = True
            break

        temparray = [id_array[0][1].rpartition("0")[2], id_array[0][3].rpartition("0")[2],
                        id_array[0][5].rpartition("0")[2], id_array[0][7].rpartition("0")[2]]

        if not (id_array[0][1] in yellow_ids or id_array[0][3] in yellow_ids 
                or id_array[0][5] in yellow_ids or id_array[0][7] in yellow_ids):
            fruruf(cubies, id_array, rotations)

        if temparray[0] == "1":
            # L up
            if temparray[3] != "1" and temparray[1] == "1":
                fruruf(cubies, id_array, rotations)

            # L down
            if temparray[1] != "1" and temparray[2] == "1":
                rotate_up_prime_cubies(cubies, id_array, rotations)
                fruruf(cubies, id_array, rotations)

            # line
            if temparray[3] == "1":
                rotate_up_cubies(cubies, id_array, rotations)
                fruruf(cubies, id_array, rotations)
                temp = True

        if temparray[0] != "1":
            # L 
            if temparray[1] == "1" and temparray[3] == "1":
                rotate_up_cubies(cubies, id_array, rotations)
                fruruf(cubies, id_array, rotations)

            if temparray[2] == "1" and temparray[3] == "1":
                rotate_up_cubies(cubies, id_array, rotations)
                rotate_up_cubies(cubies, id_array, rotations)
                fruruf(cubies, id_array, rotations)
                    
            #line
            if temparray[1] == "1" and temparray[2] == "1":
                fruruf(cubies, id_array, rotations)
                temp = True


def correct_top_cross(cubies, id_array, rotations):
    # insert cubie 2
    # yellow, orange

    # insert cubie 4
    # yellow, blue

    # insert cubie 6
    # yellow, green

    # insert cubie 8
    # yellow, red

    while not (id_array[0][1] == "0201"):
        rotate_up_cubies(cubies, id_array, rotations)

    while not (id_array[0][3] == "0401" and id_array[0][5] == "0601" and id_array[0][7] == "0801"):

        if id_array[0][7] == "0801":
            correct_front(cubies, id_array, rotations)

        elif id_array[0][3] == "0401":
            rotate_cube_right_cubies(cubies, id_array, rotations)
            correct_front(cubies, id_array, rotations)
            rotate_cube_left_cubies(cubies, id_array, rotations)

        elif id_array[0][5] == "0601": 
            correct_front(cubies, id_array, rotations)

        elif id_array[0][3] == "0801" and id_array[0][5] == "0401":
            rotate_up_prime_cubies(cubies, id_array, rotations)
            rotate_up_prime_cubies(cubies, id_array, rotations)
            correct_front(cubies, id_array, rotations)

        elif id_array[0][3] == "0601" and id_array[0][5] == "0801":
            rotate_up_cubies(cubies, id_array, rotations)
            correct_front(cubies, id_array, rotations)

        while not (id_array[0][1] == "0201"):
            rotate_up_cubies(cubies, id_array, rotations)
        

def sort_corners(cubies, id_array, rotations):
    # sort the last 4 corners (cubies 1, 7, 9, 3)

    # check if cubie 1 is at right position
    cubie_1_right = id_array[0][0].rpartition("0")[0] == "01"
    cubie_3_right = id_array[0][2].rpartition("0")[0] == "03"
    cubie_7_right = id_array[0][6].rpartition("0")[0] == "07"
    cubie_9_right = id_array[0][8].rpartition("0")[0] == "09"
    corners_right = False

    if not (cubie_1_right and cubie_3_right and cubie_7_right and cubie_9_right):

        # TODO: if case fuer den Fall, dass kein cubie richtig liegt
        if cubie_1_right == False and cubie_3_right == False and cubie_7_right == False and cubie_9_right == False:
            sort_corners_algorithm(cubies, id_array, rotations)

            if id_array[0][0].rpartition("0")[0] == "01":
                cubie_1_right = True

            if id_array[0][2].rpartition("0")[0] == "03":
                cubie_3_right = True

            if id_array[0][6].rpartition("0")[0] == "07":
                cubie_7_right = True

            if id_array[0][8].rpartition("0")[0] == "09":
                cubie_9_right = True

        if cubie_1_right:
            rotate_cube_right_cubies(cubies, id_array, rotations)
            rotate_cube_right_cubies(cubies, id_array, rotations)

        elif cubie_3_right:
            rotate_cube_left_cubies(cubies, id_array, rotations)

        elif cubie_7_right:
            rotate_cube_right_cubies(cubies, id_array, rotations)

        while not (corners_right):
            sort_corners_algorithm(cubies, id_array, rotations)

            corners = [id_array[0][0].rpartition("0")[0], id_array[0][2].rpartition("0")[0], 
                       id_array[0][8].rpartition("0")[0], id_array[0][6].rpartition("0")[0]]

            if (corners == ["01", "03", "09", "07"] or corners == ["03", "09", "07", "01"] 
                or corners == ["09", "07", "01", "03"] or corners == ["07", "01", "03", "09"]):
                corners_right = True

        while not (id_array[0][7] == "0801"):
            rotate_cube_right_cubies(cubies, id_array, rotations)


def correct_corners(cubies, id_array, rotations):

    rotate_cube_up_cubies(cubies, id_array, rotations)
    rotate_cube_up_cubies(cubies, id_array, rotations)

    t = 0

    help = [id_array[5][2], id_array[2][6], id_array[1][8]]
    
    # if not ("0301" in help and "0302" in help and "0303" in help):
        # print("help!!!")
        # print(help)

    while not ((id_array[5][2] == "0301") and (id_array[2][6] == "0302") and (id_array[1][8] == "0303")):
        # print(id_array[5][2], end=" ")
        # print(id_array[2][6], end=" ")
        # print(id_array[1][8])
        # t += 1
        # if t == 20:
        #     break
        ruru(cubies, id_array, rotations)

    rotate_down_cubies(cubies, id_array, rotations)

    help2 = [id_array[5][2], id_array[2][6], id_array[1][8]]
    
    # if not ("0101" in help2 and "0102" in help2 and "0103" in help2):
        # print("help2!!!")
        # print(help2)

    while not (id_array[5][2] == "0101" and id_array[2][6] == "0103" and id_array[1][8] == "0102"):
        # print("ruru")
        # print(id_array[5][2], end=" ")
        # print(id_array[2][6], end=" ")
        # print(id_array[1][8])
        ruru(cubies, id_array, rotations)

    rotate_down_cubies(cubies, id_array, rotations)

    help3 = [id_array[5][2], id_array[2][6], id_array[1][8]]
    
    # if not ("0701" in help3 and "0702" in help3 and "0703" in help3):
        # print("help3!!!")
        # print(help3)

    while not (id_array[5][2] == "0701" and id_array[2][6] == "0702" and id_array[1][8] == "0703"):
        # print(id_array[5][2], end=" ")
        # print(id_array[2][6], end=" ")
        # print(id_array[1][8])
        ruru(cubies, id_array, rotations)

    rotate_down_cubies(cubies, id_array, rotations)

    help4 = [id_array[5][2], id_array[2][6], id_array[1][8]]
    
    # if not ("0901" in help4 and "0902" in help4 and "0903" in help4):
    #     print("help4!!!")
    #     print(help4)

    while not (id_array[5][2] == "0901" and id_array[2][6] == "0902" and id_array[1][8] == "0903"):
        # print(id_array[5][2], end=" ")
        # print(id_array[2][6], end=" ")
        # print(id_array[1][8])
        ruru(cubies, id_array, rotations)

    while not (id_array[5][0] == "0101"):
        rotate_down_cubies(cubies, id_array, rotations)

    rotate_cube_up_cubies(cubies, id_array, rotations)
    rotate_cube_up_cubies(cubies, id_array, rotations)


def solve_cube(cubies, id_array, rotations):
    white_cross(cubies, id_array, rotations)
    white_corners(cubies, id_array, rotations)
    second_layer(cubies, id_array, rotations)
    top_cross(cubies, id_array, rotations)
    correct_top_cross(cubies, id_array, rotations)
    sort_corners(cubies, id_array, rotations)
    correct_corners(cubies, id_array, rotations)