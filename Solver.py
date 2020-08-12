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


#   L' U' L U
def lulu(cubies, id_array):
    rotate_left_prime_cubies(cubies, id_array)
    rotate_up_prime_cubies(cubies, id_array)
    rotate_left_cubies(cubies, id_array)
    rotate_up_cubies(cubies, id_array)


#   U R U R' U' y L U' L' U
def second_layer_right(cubies, id_array):
    rotate_up_cubies(cubies, id_array)
    ruru(cubies, id_array)
    rotate_cube_left_cubies(cubies, id_array)
    lulu(cubies, id_array)
    rotate_cube_right_cubies(cubies, id_array)


#   U' L U' L' U y' R U R' U'
def second_layer_left(cubies, id_array):
    rotate_up_prime_cubies(cubies, id_array)
    lulu(cubies, id_array)
    rotate_cube_right_cubies(cubies, id_array)
    ruru(cubies, id_array)
    rotate_cube_left_cubies(cubies, id_array)


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
    #
    # When the cube is scrambled, the first necessary cubie can be in either the first,
    # second or already in the thrid layer of the cube.
    # First of all its checked in which of the three layers it is and then
    # it will be correctly oriented brought to the third layer.
    #
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
    #
    # Correcting the positioning, so that the following cubies will be in correct order
    #
    while cubies[13].pos2[1] != 3:
        rotate_down_cubies(cubies, id_array)

    # insert cubie 18
    #
    # If cubie 18 is in the second layer it can be easily rotated down to the "white side"
    # The already inserted cubie 14 shall be rotated if the rotation of cubie 18 would affect its
    # positioning. Afterwards cubie 18 will be inserted in correct order.
    #
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
    #
    # if the white side of cubie 18 is on the yellow face, down will be rotated until
    # the cubie can be inserted by two simple rotations of the side where the red face of cubie 18 is
    #
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
    #
    # Correcting the positioning, so that the following cubies will be in correct order
    #
    while cubies[13].pos2[1] != 3:
        rotate_down_cubies(cubies, id_array)

    #
    # Cubie 18 can be easily inserted if it is in the third layer but the white
    # face is not at the white side. With a few simple moves you can insert
    # the cubie correctly oriented into its slot
    #
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

    #
    # if cubie 18 is in the third layer and the white face is at the white side
    # then you need to correct its position and/or its orientation
    # the position of cubie 14 can be ignored but should not be affected
    #
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
    # same as 18 but with corrections if 14 or 18 is affected
    #
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

        #
        # if cubie 22 was at the front or left side, cubie 14 will be affected by the rotation, which has to be undone
        #
        while cubies[17].pos1[1] != 7:
            rotate_front_cubies(cubies, id_array)

        while cubies[13].pos1[1] != 7:
            rotate_left_prime_cubies(cubies, id_array)

    #
    # if cubie 22 is in the first layer and the white face is not at the yellow side (up)
    #
    if is_in_layer(id_array, 1, 22) and cubies[21].pos2[0] != 0:
        while 7 != cubies[21].pos1[1]:
            rotate_up_cubies(cubies, id_array)

        rotate_front_cubies(cubies, id_array)
        rotate_right_prime_cubies(cubies, id_array)
        rotate_front_prime_cubies(cubies, id_array)

    #
    # if cubie 22 is in the first layer and the white face is at the yellow side (up)
    #
    if cubies[21].pos2[0] == 0:
        while 5 != cubies[21].pos2[1]:
            rotate_up_cubies(cubies, id_array)

        rotate_right_cubies(cubies, id_array)
        rotate_right_cubies(cubies, id_array)

    #
    # if cubie 22 is in the thrid layer
    #
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
    #
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

    #
    # if cubie 25 is in the first layer and the white face is on the yellow side
    #
    if cubies[24].pos2[0] == 0:
        while 1 != cubies[24].pos2[1]:
            rotate_up_cubies(cubies, id_array)

        rotate_back_cubies(cubies, id_array)
        rotate_back_cubies(cubies, id_array)

    #
    # if cubie 25 is in the first layer and the white face is not on the yellow side
    #
    if is_in_layer(id_array, 1, 25) and cubies[24].pos2[0] != 0:
        while 1 != cubies[24].pos1[1]:
            rotate_up_cubies(cubies, id_array)

        rotate_back_prime_cubies(cubies, id_array)
        rotate_down_prime_cubies(cubies, id_array)
        rotate_right_cubies(cubies, id_array)
        rotate_down_cubies(cubies, id_array)

    #
    # if cubie 25 is already at the right spot but flipped
    #
    if cubies[24].pos2 == [3, 7]:
        rotate_cube_up_cubies(cubies, id_array)
        rotate_cube_up_cubies(cubies, id_array)
        flip_orientation_of_edge_in_first_layer(cubies, id_array, 7)
        rotate_cube_up_cubies(cubies, id_array)
        rotate_cube_up_cubies(cubies, id_array)


def white_corners(cubies, id_array):
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
            ruru(cubies, id_array)
        
        if id_array[5][6].rpartition("0")[0] == "15":
            rotate_cube_right_cubies(cubies, id_array)
            lulu(cubies, id_array)
            rotate_cube_left_cubies(cubies, id_array)

        if id_array[5][8].rpartition("0")[0] == "15":
            rotate_cube_left_cubies(cubies, id_array)
            ruru(cubies, id_array)
            rotate_cube_right_cubies(cubies, id_array)

        # if cubie 15 ist already at the right position, but swapped
        if id_array[5][0].rpartition("0")[0] == "15":
            while not (id_array[4][8] == "1501" and id_array[1][6] == "1502" and id_array[5][0] == "1503"):
                lulu(cubies, id_array)

    #
    # If cubie 15 is in the 1st layer, we rotate the up-side as long as
    # cubie 15 is not directly over the position in 3rd layer, where it
    # should be.
    # Then we use the "lulu"-algorithm to swap cubie 15 at it's right
    # position.
    #

    if is_in_layer(id_array, 1, 15):
        while id_array[0][6].rpartition("0")[0] != "15":
            rotate_up_cubies(cubies, id_array)

        while not (id_array[4][8] == "1501" and id_array[1][6] == "1502" and id_array[5][0] == "1503"):
            lulu(cubies, id_array)

    # insert cubie 19
    # red, green, white
    #
    # Now there are 3 possibilities where cubie 19 can be in the 3rd layer,
    # because cubie 15 is already inserted correctly.
    # We swap cubie 19 from 3rd layer to 1st layer too.
    #
    if is_in_layer(id_array, 3, 19):
        if id_array[5][6].rpartition("0")[0] == "19":
            rotate_cube_right_cubies(cubies, id_array)
            lulu(cubies, id_array)
            rotate_cube_left_cubies(cubies, id_array)

        if id_array[5][8].rpartition("0")[0] == "19":
            rotate_cube_left_cubies(cubies, id_array)
            ruru(cubies, id_array)
            rotate_cube_right_cubies(cubies, id_array)

        if id_array[5][2].rpartition("0")[0] == "19":
            while not (id_array[1][8] == "1901" and id_array[2][6] == "1902" and id_array[5][2] == "1903"):
                ruru(cubies, id_array)

    #
    # If cubie 19 is in the 1st layer, we rotate the up-side as long as
    # cubie 19 is not directly over the position in 3rd layer, where it
    # should be.
    # Then we use the "ruru"-algorithm to swap cubie 19 at it's right
    # position.
    #
    if is_in_layer(id_array, 1, 19):
        while id_array[0][8].rpartition("0")[0] != "19":
            rotate_up_cubies(cubies, id_array)
        
        while not (id_array[1][8] == "1901" and id_array[2][6] == "1902" and id_array[5][2] == "1903"):
                ruru(cubies, id_array)
        

    # insert cubie 23
    # green, orange, white
    #
    # Now there are 2 possibilities where cubie 23 can be in the 3rd layer,
    # because cubie 15 and cubie 19 are already inserted correctly.
    # That we can use the "lulu" and "ruru"-algorithms, we have to rotate the
    # whole cube 2 times (rotate_cube_right_cubies()).
    # We swap cubie 23 from 3rd layer to 1st layer too.
    #

    rotate_cube_right_cubies(cubies, id_array)
    rotate_cube_right_cubies(cubies, id_array)

    if is_in_layer(id_array, 3, 23):
        if id_array[5][2].rpartition("0")[0] == "23":
            ruru(cubies, id_array)

        if id_array[5][0].rpartition("0")[0] == "23":
            while not (id_array[4][8] == "2301" and id_array[1][6] == "2302" and id_array[5][0] == "2303"):
                lulu(cubies, id_array)

    #
    # If cubie 23 is in the 1st layer, we rotate the up-side as long as
    # cubie 23 is not directly over the position in 3rd layer, where it
    # should be.
    # Then we use the "lulu"-algorithm to swap cubie 23 at it's right
    # position.
    #

    if is_in_layer(id_array, 1, 23):
        while id_array[0][6].rpartition("0")[0] != "23":
            rotate_up_cubies(cubies, id_array)

        while not (id_array[4][8] == "2301" and id_array[1][6] == "2302" and id_array[5][0] == "2303"):
            lulu(cubies, id_array)

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
            rotate_up_cubies(cubies, id_array)
        
    while not (id_array[1][8] == "1302" and id_array[2][6] == "1301" and id_array[5][2] == "1303"):
            ruru(cubies, id_array)

    #
    # We have to rotate the whole cube 2 times again, that we are at the same
    # position like at the beginning again.
    #

    rotate_cube_right_cubies(cubies, id_array)
    rotate_cube_right_cubies(cubies, id_array)


def second_layer(cubies, id_array):
    # alle verbliebenen cubies mit 2 Farben, die NICHT gelb als Teilfarbe haben

    # insert cubie 12
    # blue, red
    if is_in_layer(id_array, 2, 12):
        if id_array[1][3] == "1201":
            second_layer_left(cubies, id_array)

        elif id_array[1][5].rpartition("0")[0] == "12":
            second_layer_right(cubies, id_array)

        elif id_array[3][3].rpartition("0")[0] == "12":
            rotate_cube_left_cubies(cubies, id_array)
            rotate_cube_left_cubies(cubies, id_array)
            second_layer_left(cubies, id_array)
            rotate_cube_left_cubies(cubies, id_array)
            rotate_cube_left_cubies(cubies, id_array)

        elif id_array[3][5].rpartition("0")[0] == "12":
            rotate_cube_left_cubies(cubies, id_array)
            rotate_cube_left_cubies(cubies, id_array)
            second_layer_right(cubies, id_array)
            rotate_cube_left_cubies(cubies, id_array)
            rotate_cube_left_cubies(cubies, id_array)

    if is_in_layer(id_array, 1, 12):
        if cubies[11].pos1[0] == 0:
            while not (id_array[0][7] == "1201"):
                rotate_up_cubies(cubies, id_array)
            second_layer_left(cubies, id_array)

        else:
            while not (id_array[0][3] == "1202"):
                rotate_up_cubies(cubies, id_array)
            rotate_cube_right_cubies(cubies, id_array)
            second_layer_right(cubies, id_array)
            rotate_cube_left_cubies(cubies, id_array)


    # insert cubie 17
    # red, green
    if is_in_layer(id_array, 2, 17):
        if id_array[1][5] == "1702":
            print("if 1")
            second_layer_right(cubies, id_array)

        elif id_array[3][3].rpartition("0")[0] == "17":
            rotate_cube_left_cubies(cubies, id_array)
            rotate_cube_left_cubies(cubies, id_array)
            second_layer_left(cubies, id_array)
            rotate_cube_left_cubies(cubies, id_array)
            rotate_cube_left_cubies(cubies, id_array)

        elif id_array[3][5].rpartition("0")[0] == "17":
            rotate_cube_left_cubies(cubies, id_array)
            rotate_cube_left_cubies(cubies, id_array)
            second_layer_right(cubies, id_array)
            rotate_cube_left_cubies(cubies, id_array)
            rotate_cube_left_cubies(cubies, id_array)


    if is_in_layer(id_array, 1, 17):
        if cubies[16].pos2[0] == 0:
            while not (id_array[0][7] == "1702"):
                rotate_up_cubies(cubies, id_array)
            second_layer_right(cubies, id_array)

        else:
            while not (id_array[0][5] == "1701"):
                rotate_up_cubies(cubies, id_array)
            rotate_cube_left_cubies(cubies, id_array)
            second_layer_left(cubies, id_array)
            rotate_cube_right_cubies(cubies, id_array)


    # insert cubie 21
    # green, orange

    rotate_cube_right_cubies(cubies, id_array)
    rotate_cube_right_cubies(cubies, id_array)

    if id_array[1][3] == "2101":
        second_layer_left(cubies, id_array)

    elif id_array[1][5].rpartition("0")[0] == "21":
        second_layer_right(cubies, id_array)


    if is_in_layer(id_array, 1, 21):
        if cubies[20].pos1[0] == 0:
            while not (id_array[0][7] == "2101"):
                rotate_up_cubies(cubies, id_array)
            second_layer_left(cubies, id_array)

        else:
            while not (id_array[0][3] == "2102"):
                rotate_up_cubies(cubies, id_array)
            rotate_cube_right_cubies(cubies, id_array)
            second_layer_right(cubies, id_array)
            rotate_cube_left_cubies(cubies, id_array)
    

    # insert cubie 10
    # blue, orange

    if id_array[1][5] == "1001":
        second_layer_right(cubies, id_array)
    
    if cubies[9].pos1[0] == 0:
        while not (id_array[0][7] == "1001"):
            rotate_up_cubies(cubies, id_array)
        second_layer_right(cubies, id_array)

    else:
        while not (id_array[0][5] == "1002"):
            rotate_up_cubies(cubies, id_array)
        rotate_cube_left_cubies(cubies, id_array)
        second_layer_left(cubies, id_array)
        rotate_cube_right_cubies(cubies, id_array)

    rotate_cube_right_cubies(cubies, id_array)
    rotate_cube_right_cubies(cubies, id_array)








