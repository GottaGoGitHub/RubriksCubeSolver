# from RubriksCubeSolver.Cube import *
from Cube import *
import random
from tkinter import messagebox
from FileHandler import *


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
        if id_array[cubies[17].pos2[0]][7] == cubies[13].id1:
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


def white_corners(cubies, id_array, rotations, error, window, cube):
    """
    Inserts cubie 13, 15, 19 and 23 to their intended places.
    """
    # insert cubie 15
    # blue, red, white
    #
    # First we swap cubie 15 from 3rd layer in 1st layer.
    # There are 4 possibilities, where cubie 15 can be in the 3rd layer.
    #

    boolerror_message = False

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
                if id_array[4][8] == "1502" and id_array[1][6] == "1501" and id_array[5][0] == "1503":
                    boolerror_message = True
                    error[0] = True
                    break
                lulu(cubies, id_array, rotations)

    #
    # If cubie 15 is in the 1st layer, we rotate the up-side as long as
    # cubie 15 is not directly over the position in 3rd layer, where it
    # should be.
    # Then we use the "lulu"-algorithm to swap cubie 15 at it's right
    # position.
    #

    if not error[0]:
        if is_in_layer(id_array, 1, 15):
            while id_array[0][6].rpartition("0")[0] != "15":
                rotate_up_cubies(cubies, id_array, rotations)

            while not (id_array[4][8] == "1501" and id_array[1][6] == "1502" and id_array[5][0] == "1503"):
                if id_array[4][8] == "1502" and id_array[1][6] == "1501" and id_array[5][0] == "1503":
                    boolerror_message = True
                    error[0] = True
                    break
                lulu(cubies, id_array, rotations)

    if boolerror_message:

        messagebox.showerror("Flipped Corner Cubie Error", "Some of the colors of a white corner cubie are flipped," 
                                                            "please set the colors for the grey fields again and submit again.")
        import_cube_from_csv(cubies,"AUTOSAVE.csv")
        cubies[14].color1 = "grey"
        cubies[14].color2 = "grey"
        cubies[14].color3 = "grey"
        cubies[14].colors = ["grey", "grey", "grey"]
        export_cube_to_csv(cubies, "AUTOSAVE.csv")
        set_colors(window, get_colors_from_cubies(cubies), cube) 

        # insert cubie 19
        # red, green, white
        #
        # Now there are 3 possibilities where cubie 19 can be in the 3rd layer,
        # because cubie 15 is already inserted correctly.
        # We swap cubie 19 from 3rd layer to 1st layer too.
        #

    if not error[0]:
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
                    if id_array[1][8] == "1902" and id_array[2][6] == "1901" and id_array[5][2] == "1903":
                        boolerror_message = True
                        error[0] = True
                        break
                    ruru(cubies, id_array, rotations)

        #
        # If cubie 19 is in the 1st layer, we rotate the up-side as long as
        # cubie 19 is not directly over the position in 3rd layer, where it
        # should be.
        # Then we use the "ruru"-algorithm to swap cubie 19 at it's right
        # position.
        #

    if not error[0]:
        if is_in_layer(id_array, 1, 19):
            while id_array[0][8].rpartition("0")[0] != "19":
                rotate_up_cubies(cubies, id_array, rotations)

            while not (id_array[1][8] == "1901" and id_array[2][6] == "1902" and id_array[5][2] == "1903"):
                if id_array[1][8] == "1902" and id_array[2][6] == "1901" and id_array[5][2] == "1903":
                    boolerror_message = True
                    error[0] = True
                    break
                ruru(cubies, id_array, rotations)

    if boolerror_message:

        messagebox.showerror("Flipped Corner Cubie Error", "Some of the colors of a white corner cubie are flipped," 
                                                            "please set the colors for the grey fields again and submit again.")
        import_cube_from_csv(cubies,"AUTOSAVE.csv")
        cubies[18].color1 = "grey"
        cubies[18].color2 = "grey"
        cubies[18].color3 = "grey"
        cubies[18].colors = ["grey", "grey", "grey"]
        export_cube_to_csv(cubies, "AUTOSAVE.csv")
        set_colors(window, get_colors_from_cubies(cubies), cube) 

        # insert cubie 23
        # green, orange, white
        #
        # Now there are 2 possibilities where cubie 23 can be in the 3rd layer,
        # because cubie 15 and cubie 19 are already inserted correctly.
        # That we can use the "lulu" and "ruru"-algorithms, we have to rotate the
        # whole cube 2 times (rotate_cube_right_cubies()).
        # We swap cubie 23 from 3rd layer to 1st layer too.
        #

    if not error[0]:
        rotate_cube_right_cubies(cubies, id_array, rotations)
        rotate_cube_right_cubies(cubies, id_array, rotations)

        if is_in_layer(id_array, 3, 23):
            if id_array[5][2].rpartition("0")[0] == "23":
                ruru(cubies, id_array, rotations)

            if id_array[5][0].rpartition("0")[0] == "23":
                while not (id_array[4][8] == "2301" and id_array[1][6] == "2302" and id_array[5][0] == "2303"):
                    if id_array[4][8] == "2302" and id_array[1][6] == "2301" and id_array[5][0] == "2303":
                        boolerror_message = True
                        error[0] = True
                        break
                    lulu(cubies, id_array, rotations)

        #
        # If cubie 23 is in the 1st layer, we rotate the up-side as long as
        # cubie 23 is not directly over the position in 3rd layer, where it
        # should be.
        # Then we use the "lulu"-algorithm to swap cubie 23 at it's right
        # position.
        #

    if not error[0]:
        if is_in_layer(id_array, 1, 23):
            while id_array[0][6].rpartition("0")[0] != "23":
                rotate_up_cubies(cubies, id_array, rotations)

            while not (id_array[4][8] == "2301" and id_array[1][6] == "2302" and id_array[5][0] == "2303"):
                if id_array[4][8] == "2302" and id_array[1][6] == "2301" and id_array[5][0] == "2303":
                    boolerror_message = True
                    error[0] = True
                    break
                lulu(cubies, id_array, rotations)

    if boolerror_message:

        messagebox.showerror("Flipped Corner Cubie Error", "Some of the colors of a white corner cubie are flipped," 
                                                            "please set the colors for the grey fields again and submit again.")
        import_cube_from_csv(cubies,"AUTOSAVE.csv")
        cubies[22].color1 = "grey"
        cubies[22].color2 = "grey"
        cubies[22].color3 = "grey"
        cubies[22].colors = ["grey", "grey", "grey"]
        export_cube_to_csv(cubies, "AUTOSAVE.csv")
        set_colors(window, get_colors_from_cubies(cubies), cube) 

        # insert cubie 13
        # blue, orange, white
        #
        # Now there is only 1 possibility left where cubie 13 can be in the 3rd layer,
        # because cubie 15, cubie 19 and cubie 23 are already inserted correctly.
        # We swap cubie 13 from 3rd layer to 1st layer too.
        # Then we use the "ruru"-algorithm to swap cubie 13 at it's right position.
        #

    if not error[0]:
        if is_in_layer(id_array, 1, 13):
            while id_array[0][8].rpartition("0")[0] != "13":
                rotate_up_cubies(cubies, id_array, rotations)

        while not (id_array[1][8] == "1302" and id_array[2][6] == "1301" and id_array[5][2] == "1303"):
            if id_array[1][8] == "1301" and id_array[2][6] == "1302" and id_array[5][2] == "1303":
                boolerror_message = True
                error[0] = True
                break
            ruru(cubies, id_array, rotations)

        #
        # We have to rotate the whole cube 2 times again, that we are at the same
        # position like at the beginning again.
        #

        rotate_cube_right_cubies(cubies, id_array, rotations)
        rotate_cube_right_cubies(cubies, id_array, rotations)

    if boolerror_message:

        messagebox.showerror("Flipped Corner Cubie Error", "Some of the colors of a white corner cubie are flipped," 
                                                            "please set the colors for the grey fields again and submit again.")
        import_cube_from_csv(cubies,"AUTOSAVE.csv")
        cubies[12].color1 = "grey"
        cubies[12].color2 = "grey"
        cubies[12].color3 = "grey"
        cubies[12].colors = ["grey", "grey", "grey"]
        export_cube_to_csv(cubies, "AUTOSAVE.csv")
        set_colors(window, get_colors_from_cubies(cubies), cube) 

def second_layer(cubies, id_array, rotations, error):
    # alle verbliebenen cubies mit 2 Farben, die NICHT gelb als Teilfarbe haben

    # insert cubie 12
    # blue, red
    if not error[0]:
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

        elif cubies[9].pos2[0] == 0:
            while not (id_array[0][5] == "1002"):
                rotate_up_cubies(cubies, id_array, rotations)
            rotate_cube_left_cubies(cubies, id_array, rotations)
            second_layer_left(cubies, id_array, rotations)
            rotate_cube_right_cubies(cubies, id_array, rotations)

        rotate_cube_right_cubies(cubies, id_array, rotations)
        rotate_cube_right_cubies(cubies, id_array, rotations)


def top_cross(cubies, id_array, rotations, error):

    if not error[0]:
        temp = False

        yellow_ids = ["0201", "0401", "0601", "0801"]

        cubie2true = "0201" in id_array[0]
        cubie4true = "0401" in id_array[0]
        cubie6true = "0601" in id_array[0]
        cubie8true = "0801" in id_array[0]

        cubie_on_yellow_side = [cubie2true, cubie4true, cubie6true, cubie8true]

        counter = 0

        for i in cubie_on_yellow_side:
            if i == True:
                counter += 1

        if counter == 1 or counter == 3:
            messagebox.showerror("Flipped Cubie Error", "Please flip one of the 4 edge cubies with a yellow side.")
            error[0] = True

        else:
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

                    # line
                    if temparray[1] == "1" and temparray[2] == "1":
                        fruruf(cubies, id_array, rotations)
                        temp = True


def correct_top_cross(cubies, id_array, rotations, error):
    # insert cubie 2
    # yellow, orange

    # insert cubie 4
    # yellow, blue

    # insert cubie 6
    # yellow, green

    # insert cubie 8
    # yellow, red

    if not error[0]:
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


def sort_corners(cubies, id_array, rotations, error, window, cube):
    # sort the last 4 corners (cubies 1, 7, 9, 3)

    boolerror_message = False
    
    if not error[0]:
        # check if cubie 1 is at right position
        cubie_1_right = id_array[0][0].rpartition("0")[0] == "01"
        cubie_3_right = id_array[0][2].rpartition("0")[0] == "03"
        cubie_7_right = id_array[0][6].rpartition("0")[0] == "07"
        cubie_9_right = id_array[0][8].rpartition("0")[0] == "09"
        corners_right = False

        if not (cubie_1_right and cubie_3_right and cubie_7_right and cubie_9_right):
            while (cubie_1_right == False and cubie_3_right == False and cubie_7_right == False and cubie_9_right == False):
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

            counter = 0
            positions = []

            while not (corners_right or counter == 9):
                sort_corners_algorithm(cubies, id_array, rotations)

                corners = [id_array[0][0].rpartition("0")[0], id_array[0][2].rpartition("0")[0],
                        id_array[0][8].rpartition("0")[0], id_array[0][6].rpartition("0")[0]]

                corner_possibilities = [["01", "03", "09", "07"], ["03", "09", "07", "01"], ["09", "07", "01", "03"], ["07", "01", "03", "09"]]

                if (corners == ["01", "03", "09", "07"] or corners == ["03", "09", "07", "01"]
                        or corners == ["09", "07", "01", "03"] or corners == ["07", "01", "03", "09"]):
                    corners_right = True

                counter += 1

                if counter == 7 or counter == 8 or counter == 9:
                    for temp_corners in corner_possibilities:
                        for i, item in enumerate(temp_corners):
                            if item != corners[i]:
                                positions.append([i, int(item) - 1])
                        if len(positions) != 2:
                            positions.clear()

                        elif len(positions) == 2:
                            counter = 9
                            break


            if counter == 9 and len(positions) != 0:
                boolerror_message = True
                print(cubies[12].__str__())
                print(id(cubies[12]))
                import_cube_from_csv(cubies,"AUTOSAVE.csv")

                for i in range(4):
                    if i == positions[0][0]:
                        cubies[positions[0][1]].color1 = "grey"
                        cubies[positions[0][1]].color2 = "grey"
                        cubies[positions[0][1]].color3 = "grey"
                        cubies[positions[0][1]].colors = ["grey", "grey", "grey"]

                    if i == positions[1][0]:
                        cubies[positions[1][1]].color1 = "grey"
                        cubies[positions[1][1]].color2 = "grey"
                        cubies[positions[1][1]].color3 = "grey"
                        cubies[positions[1][1]].colors = ["grey", "grey", "grey"]

                export_cube_to_csv(cubies, "AUTOSAVE.csv")
                print(cubies[12].__str__())
                print(id(cubies[12]))
                set_colors(window, get_colors_from_cubies(cubies), cube) 

            print(cubies[12].__str__()) 
            print(id(cubies[12]))

            while not (id_array[0][7] == "0801"):
                rotate_cube_right_cubies(cubies, id_array, rotations)

    if boolerror_message:
        messagebox.showerror("Flipped Corner Error", "Two yellow corners are swapped. Please swap the position of the two cubies.")
        error[0] = True

    print(cubies[12].__str__()) 
    print(id(cubies[12]))



def correct_corners(cubies, id_array, rotations, error, window, cube):

    boolerror_message = False

    print(cubies[12].__str__())
    print(id(cubies[12]))

    if not error[0]:

        cubie1yellowtrue = ["0101" in id_array[0][0], 0]
        cubie3yellowtrue = ["0301" in id_array[0][2], 2]
        cubie7yellowtrue = ["0701" in id_array[0][6], 6]
        cubie9yellowtrue = ["0901" in id_array[0][8], 8]

        if cubie1yellowtrue[0]:
            if "0102" == id_array[3][2]:
                boolerror_message = True
                import_cube_from_csv(cubies,"AUTOSAVE.csv")
                cubies[0].color1 = "grey"
                cubies[0].color2 = "grey"
                cubies[0].color3 = "grey"
                cubies[0].colors = ["grey", "grey", "grey"]
                export_cube_to_csv(cubies, "AUTOSAVE.csv")
                set_colors(window, get_colors_from_cubies(cubies), cube) 

        if cubie3yellowtrue[0]:
            if "0303" == id_array[2][2]:
                boolerror_message = True
                import_cube_from_csv(cubies,"AUTOSAVE.csv")
                cubies[2].color1 = "grey"
                cubies[2].color2 = "grey"
                cubies[2].color3 = "grey"
                cubies[2].colors = ["grey", "grey", "grey"]
                export_cube_to_csv(cubies,"AUTOSAVE.csv")
                set_colors(window, get_colors_from_cubies(cubies), cube) 

        if cubie7yellowtrue[0]:
            if "0703" == id_array[4][2]:
                boolerror_message = True
                import_cube_from_csv(cubies,"AUTOSAVE.csv")
                cubies[6].color1 = "grey"
                cubies[6].color2 = "grey"
                cubies[6].color3 = "grey"
                cubies[6].colors = ["grey", "grey", "grey"]
                export_cube_to_csv(cubies,"AUTOSAVE.csv")
                set_colors(window, get_colors_from_cubies(cubies), cube) 

        if cubie9yellowtrue[0]:
            if "0903" == id_array[1][2]:
                boolerror_message = True
                import_cube_from_csv(cubies,"AUTOSAVE.csv")
                cubies[8].color1 = "grey"
                cubies[8].color2 = "grey"
                cubies[8].color3 = "grey"
                cubies[8].colors = ["grey", "grey", "grey"]
                export_cube_to_csv(cubies,"AUTOSAVE.csv")
                set_colors(window, get_colors_from_cubies(cubies), cube) 
                
        if boolerror_message:
            error[0] = True

        cubies_on_yellow_side = [cubie1yellowtrue, cubie3yellowtrue, cubie7yellowtrue, cubie9yellowtrue]

        counter = 0

        for i in cubies_on_yellow_side:
            if i[0] == True:
                counter += 1

        if (counter == 2 or counter == 3) and boolerror_message == False:
            messagebox.showerror("Flipped Corner Cubie Error", "Some of the colors of a yellow corner cubie are flipped," 
                                                               "please flip one of the corners and submit again.")
            # TODO: correct error message 
            for i in cubies_on_yellow_side:
                if i[0] == False:
                    import_cube_from_csv(cubies,"AUTOSAVE.csv")
                    cubies[i[1]].color1 = "grey"
                    cubies[i[1]].color2 = "grey"
                    cubies[i[1]].color3 = "grey"
                    cubies[i[1]].colors = ["grey", "grey", "grey"]
                    export_cube_to_csv(cubies,"AUTOSAVE.csv")
                    set_colors(window, get_colors_from_cubies(cubies), cube) 

            error[0] = True

    if not error[0]:

        rotate_cube_up_cubies(cubies, id_array, rotations)
        rotate_cube_up_cubies(cubies, id_array, rotations)

        while not ((id_array[5][2] == "0301") and (id_array[2][6] == "0302") and (id_array[1][8] == "0303")):
            if id_array[5][2] == "0301" and id_array[2][6] == "0303" and id_array[1][8] == "0302":
                boolerror_message = True
                error[0] = True
                import_cube_from_csv(cubies,"AUTOSAVE.csv")
                cubies[2].color1 = "grey"
                cubies[2].color2 = "grey"
                cubies[2].color3 = "grey"
                cubies[2].colors = ["grey", "grey", "grey"]
                export_cube_to_csv(cubies, "AUTOSAVE.csv")
                set_colors(window, get_colors_from_cubies(cubies), cube)
                break
            ruru(cubies, id_array, rotations)

    if not error[0]:
        rotate_down_cubies(cubies, id_array, rotations)

        while not (id_array[5][2] == "0101" and id_array[2][6] == "0103" and id_array[1][8] == "0102"):
            if id_array[5][2] == "0101" and id_array[2][6] == "0102" and id_array[1][8] == "0103":
                boolerror_message = True
                error[0] = True
                import_cube_from_csv(cubies,"AUTOSAVE.csv")
                cubies[0].color1 = "grey"
                cubies[0].color2 = "grey"
                cubies[0].color3 = "grey"
                cubies[0].colors = ["grey", "grey", "grey"]
                export_cube_to_csv(cubies, "AUTOSAVE.csv")
                set_colors(window, get_colors_from_cubies(cubies), cube)
                break
            ruru(cubies, id_array, rotations)

    if not error[0]:
        rotate_down_cubies(cubies, id_array, rotations)

        while not (id_array[5][2] == "0701" and id_array[2][6] == "0702" and id_array[1][8] == "0703"):
            if id_array[5][2] == "0701" and id_array[2][6] == "0703" and id_array[1][8] == "0702":
                boolerror_message = True
                error[0] = True
                import_cube_from_csv(cubies,"AUTOSAVE.csv")
                cubies[6].color1 = "grey"
                cubies[6].color2 = "grey"
                cubies[6].color3 = "grey"
                cubies[6].colors = ["grey", "grey", "grey"]
                export_cube_to_csv(cubies, "AUTOSAVE.csv")
                set_colors(window, get_colors_from_cubies(cubies), cube)
                break
            ruru(cubies, id_array, rotations)

    if not error[0]:
        rotate_down_cubies(cubies, id_array, rotations)

        while not (id_array[5][2] == "0901" and id_array[2][6] == "0902" and id_array[1][8] == "0903"):
            if id_array[5][2] == "0901" and id_array[2][6] == "0903" and id_array[1][8] == "0902":
                boolerror_message = True
                error[0] = True
                import_cube_from_csv(cubies,"AUTOSAVE.csv")
                cubies[8].color1 = "grey"
                cubies[8].color2 = "grey"
                cubies[8].color3 = "grey"
                cubies[8].colors = ["grey", "grey", "grey"]
                export_cube_to_csv(cubies, "AUTOSAVE.csv")
                set_colors(window, get_colors_from_cubies(cubies), cube)
                break
            ruru(cubies, id_array, rotations)

    if boolerror_message:
        messagebox.showerror("Flipped Corner Cubie Error", "Some of the colors of a yellow corner cubie are flipped," 
                                                           "please set the colors for the grey fields again and submit again.")
        error[0] = True

    if not error[0]:
        while not (id_array[5][0] == "0101"):
            rotate_down_cubies(cubies, id_array, rotations)

        rotate_cube_up_cubies(cubies, id_array, rotations)
        rotate_cube_up_cubies(cubies, id_array, rotations)


def solve_cube(cubies, id_array, rotations, error, window, cube):
    white_cross(cubies, id_array, rotations)
    white_corners(cubies, id_array, rotations, error, window, cube)
    second_layer(cubies, id_array, rotations, error)
    top_cross(cubies, id_array, rotations, error)
    correct_top_cross(cubies, id_array, rotations, error)
    sort_corners(cubies, id_array, rotations, error, window, cube)
    correct_corners(cubies, id_array, rotations, error, window, cube)
