   # Rotate the cube, so that the white side is the front
    # Cubie N° 26 has to be at [1][4]
    white_centre = cubies[25].pos1

    if 1 != white_centre[0]:
        if 0 == white_centre[0]:
            rotate_cube_down_cubies(cubies, id_array)

        if 2 == white_centre[0]:
            rotate_cube_left_cubies(cubies, id_array)

        if 3 == white_centre[0]:
            rotate_cube_left_cubies(cubies, id_array)
            rotate_cube_left_cubies(cubies, id_array)

        if 4 == white_centre[0]:
            rotate_cube_right_cubies(cubies, id_array)

        if 5 == white_centre[0]:
            rotate_cube_up_cubies(cubies, id_array)

    # find piece 14 and insert it back to its original position
    side1_14 = cubies[13].pos1   # blue side
    side2_14 = cubies[13].pos2   # white side

    if 1 != side2_14[0]:
        # if the white side of N°14 is a the top (0)
        if 0 == side2_14[0]:
            if 1 == side2_14[1]:
                rotate_up_prime_cubies(cubies, id_array)
                rotate_left_cubies(cubies, id_array)
                rotate_up_cubies(cubies, id_array)

            if 5 == side2_14[1]:
                rotate_up_cubies(cubies, id_array)
                rotate_up_cubies(cubies, id_array)
                rotate_left_cubies(cubies, id_array)
                rotate_up_prime_cubies(cubies, id_array)
                rotate_up_prime_cubies(cubies, id_array)

            if 7 == side2_14[1]:
                rotate_up_cubies(cubies, id_array)

            if 3 == side2_14[1]:
                rotate_left_cubies(cubies, id_array)

        # if the white side of N°14 is at the right side (2)
        if 2 == side2_14[0]:
            if 1 == side2_14[1]:
                rotate_front_cubies(cubies, id_array)
                rotate_up_cubies(cubies, id_array)
                rotate_front_prime_cubies(cubies, id_array)

            if 3 == side2_14[1]:
                rotate_right_prime_cubies(cubies, id_array)
                rotate_front_prime_cubies(cubies, id_array)
                rotate_down_prime_cubies(cubies, id_array)
                rotate_front_cubies(cubies, id_array)

            if 5 == side2_14[1]:
                rotate_back_cubies(cubies, id_array)
                rotate_front_cubies(cubies, id_array)
                rotate_up_cubies(cubies, id_array)
                rotate_up_cubies(cubies, id_array)
                rotate_front_prime_cubies(cubies, id_array)

            if 7 == side2_14[1]:
                rotate_front_prime_cubies(cubies, id_array)
                rotate_down_prime_cubies(cubies, id_array)
                rotate_front_cubies(cubies, id_array)

        # if the white side of N°14 is a the back (3)
        if 3 == side2_14[0]:
            if 3 == side2_14[1]:
                rotate_back_cubies(cubies, id_array)

            if 5 == side2_14[1]:
                rotate_back_prime_cubies(cubies, id_array)

            if 1 == side2_14[1]:
                rotate_front_cubies(cubies, id_array)
                rotate_up_cubies(cubies, id_array)
                rotate_up_cubies(cubies, id_array)
                rotate_front_prime_cubies(cubies, id_array)

            if 7 == side2_14[1]:
                rotate_front_prime_cubies(cubies, id_array)
                rotate_down_cubies(cubies, id_array)
                rotate_down_cubies(cubies, id_array)
                rotate_front_cubies(cubies, id_array)

        # if the white side of N°14 is a the left (4)
        if 4 == side2_14[0]:
            if 1 == side2_14[1]:
                rotate_front_cubies(cubies, id_array)
                rotate_up_cubies(cubies, id_array)
                rotate_front_prime_cubies(cubies, id_array)

            if 3 == side2_14[1]:
                rotate_left_cubies(cubies, id_array)
                rotate_left_cubies(cubies, id_array)

            if 5 == side2_14[1]:
                rotate_front_cubies(cubies, id_array)
                rotate_up_prime_cubies(cubies, id_array)
                rotate_front_prime_cubies(cubies, id_array)
                rotate_left_prime_cubies(cubies, id_array)

            if 7 == side2_14[1]:
                rotate_front_prime_cubies(cubies, id_array)
                rotate_down_cubies(cubies, id_array)
                rotate_front_cubies(cubies, id_array)

        # if the white side of N°14 is a the top (0)
        if 5 == side2_14[0]:
            if 1 == side2_14[1]:
                rotate_down_prime_cubies(cubies, id_array)

            if 3 == side2_14[1]:
                rotate_left_prime_cubies(cubies, id_array)

            if 5 == side2_14[1]:
                rotate_front_cubies(cubies, id_array)
                rotate_front_cubies(cubies, id_array)
                rotate_right_cubies(cubies, id_array)
                rotate_front_cubies(cubies, id_array)
                rotate_front_cubies(cubies, id_array)

            if 7 == side2_14[1]:
                rotate_down_cubies(cubies, id_array)
                rotate_left_prime_cubies(cubies, id_array)
                rotate_down_prime_cubies(cubies, id_array)

    if 1 == side2_14[0]:
        if 1 == side2_14[1]:
            rotate_up_cubies(cubies, id_array)
            rotate_up_cubies(cubies, id_array)
            rotate_back_cubies(cubies, id_array)
            rotate_left_cubies(cubies, id_array)

            if [3, 5] == cubies[17].pos2:
                rotate_back_prime_cubies(cubies, id_array)
                rotate_up_cubies(cubies, id_array)
                rotate_up_cubies(cubies, id_array)

        if 5 == side2_14[1]:
            print("HELP ME")
    # find piece 18 and insert it back to its original position

    # find piece 22 and insert it back to its original position

    # find piece 25 and insert it back to its original position

"""
def white_cross(cubies, id_array):
    for side_idx, side in enumerate(cube):
        for piece_idx in enumerate(side):
            if piece_idx == 1 and window.itemcget(cube[side_idx][piece_idx], "fill") == 'white':
                if side_idx == 0:
                    rotate_back_cubies(cubies, id_array)
                    rotate_backv(cubies, id_array)
                elif side_idx == 1:
                    rotate_front_cubies(cubies, id_array)
                    rotate_right_prime(cubies, id_array)
                elif side_idx == 2:
                    rotate_cube_right(cubies, id_array)
                    rotate_front(cubies, id_array)
                    rotate_right_prime(cubies, id_array)
                elif side_idx == 3:
                    rotate_cube_right(cubies, id_array)
                    rotate_cube_right(cubies, id_array)
                    rotate_front(cubies, id_array)
                    rotate_right_prime(cubies, id_array)
                elif side_idx == 4:
                    rotate_cube_right(cubies, id_array)
                    rotate_cube_right(cubies, id_array)
                    rotate_cube_right(cubies, id_array)
                    rotate_front(cubies, id_array)
                    rotate_right_prime(cubies, id_array)
            elif piece_idx == 3 and window.itemcget(cube[side_idx][piece_idx], "fill") == 'white':
                if side_idx == 0:
                    rotate_left(cubies, id_array)
                    rotate_left(cubies, id_array)
                elif side_idx == 1:
                    rotate_left(cubies, id_array)
                elif side_idx == 2:
                    rotate_cube_right(cubies, id_array)
                    rotate_left(cubies, id_array)
                elif side_idx == 3:
                    rotate_cube_right(cubies, id_array)
                    rotate_cube_right(cubies, id_array)
                    rotate_left(cubies, id_array)
                elif side_idx == 4:
                    rotate_cube_right(cubies, id_array)
                    rotate_cube_right(cubies, id_array)
                    rotate_cube_right(cubies, id_array)
                    rotate_left(cubies, id_array)
            elif piece_idx == 5 and window.itemcget(cube[side_idx][piece_idx], "fill") == 'white':
                if side_idx == 0:
                    rotate_right(cubies, id_array)
                    rotate_right(cubies, id_array)
                elif side_idx == 1:
                    rotate_right(cubies, id_array)
                elif side_idx == 2:
                    rotate_cube_right(cubies, id_array)
                    rotate_right(cubies, id_array)
                elif side_idx == 3:
                    rotate_cube_right(cubies, id_array)
                    rotate_cube_right(cubies, id_array)
                    rotate_right(cubies, id_array)
                elif side_idx == 4:
                    rotate_cube_right(cubies, id_array)
                    rotate_cube_right(cubies, id_array)
                    rotate_cube_right(cubies, id_array)
                    rotate_right(cubies, id_array)
            elif piece_idx == 7 and window.itemcget(cube[side_idx][piece_idx], "fill") == 'white':
                if side_idx == 0:
                    rotate_front(cubies, id_array)
                    rotate_front(cubies, id_array)
                elif side_idx == 1:
                    rotate_front_prime(cubies, id_array)
                    rotate_right(cubies, id_array)
                elif side_idx == 2:
                    rotate_cube_right(cubies, id_array)
                    rotate_front_prime(cubies, id_array)
                    rotate_right(cubies, id_array)
                elif side_idx == 3:
                    rotate_cube_right(cubies, id_array)
                    rotate_cube_right(cubies, id_array)
                    rotate_front_prime(cubies, id_array)
                    rotate_right(cubies, id_array)
                elif side_idx == 4:
                    rotate_cube_right(cubies, id_array)
                    rotate_cube_right(cubies, id_array)
                    rotate_cube_right(cubies, id_array)
                    rotate_front_prime(cubies, id_array)
                    rotate_right(cubies, id_array)"""



"""
def solve_white_cross(cubies, id_array):
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
        rotate_back(cubies, id_array)
        rotate_right(cubies, id_array)
        rotate_right(cubies, id_array)
        rotate_front_prime(cubies, id_array)
    elif up_white_side == 1:
        rotate_up(cubies, id_array)
        rotate_right(cubies, id_array)
        rotate_front_prime(cubies, id_array)
    elif up_white_side == 2:
        rotate_up(cubies, id_array)
        rotate_up(cubies, id_array)
        rotate_right(cubies, id_array)
        rotate_front_prime(cubies, id_array)
    elif up_white_side == 3:
        rotate_up_prime(cubies, id_array)
        rotate_right(cubies, id_array)
        rotate_front_prime(cubies, id_array)
    elif up_white_side == 4:
        rotate_right(cubies, id_array)
        rotate_front_prime(cubies, id_array)
        #   bei 5 sollte er schon richtig seien

    if down_white_side == 0:
        rotate_up(cubies, id_array)
        rotate_up(cubies, id_array)
        rotate_back(cubies, id_array)
        rotate_back(cubies, id_array)
    elif down_white_side == 1:
        rotate_up(cubies, id_array)
        rotate_right(cubies, id_array)
        rotate_front_prime(cubies, id_array)
    elif down_white_side == 2:
        rotate_up(cubies, id_array)
        rotate_up(cubies, id_array)
        rotate_right(cubies, id_array)
        rotate_front_prime(cubies, id_array)
    elif down_white_side == 3:
        rotate_up_prime(cubies, id_array)
        rotate_right(cubies, id_array)
        rotate_front_prime(cubies, id_array)
    elif down_white_side == 4:
        rotate_right(cubies, id_array)
        rotate_front_prime(cubies, id_array)
"""


def insert_to_white_cross(cubies, id_array, cubies_name):
    stop = False
    while not stop:
        # if an other cubie, which contains a white side is already at
        # position 7 of the same side the cubie will be rotated away
        # so that the cubie to insert can be inserted without removing
        # a cubie which already is at the correct level of the cube
        cubie_pos_white = cubies[int(cubies_name) - 1].pos2
        temp = cubie_pos_white.rpartition("0")
        if temp[0] == 14 or temp[0] == 18 or temp[0] == 22 or temp[0] == 25:
            rotate_down_cubies(cubies, id_array)
        else:
            stop = True
    if stop:
        # if the cubie is not already at position 7 of the corresponding side
        # the side will be rotated until it has reached position 7
        cubie_pos_white = cubies[int(cubies_name)-1].pos2

        while cubie_pos_white[1] != 7:
            rotate_by_side_idx(cubies, id_array, cubie_pos_white[0])
            cubie_pos_white = cubies[int(cubies_name) - 1].pos2




def white_cross(cubies, id_array):
    """ reconstructs the white cross """
    # pos white face -> 0, 1, 2 ,3 ,4 , 5
    #                   if 0  1,3,5,7
    #                       1b, 3l, 5r , 7f
    # 1,2,3,4 -> 1f, 2r 3b 4l rotate until 7
    # 14 18 22 25

    stop = False

    while not stop:
        pos_5_1 = id_array[5][1]
        pos_5_3 = id_array[5][3]
        pos_5_5 = id_array[5][5]
        pos_5_7 = id_array[5][7]
        pos_5_1 = pos_5_1.rpartition("0")
        pos_5_3 = pos_5_3.rpartition("0")
        pos_5_5 = pos_5_5.rpartition("0")
        pos_5_7 = pos_5_7.rpartition("0")
        temp_list = [pos_5_1, pos_5_3, pos_5_5, pos_5_7]

        if (14 in temp_list) and (18 in temp_list) and (22 in temp_list) and (25 in temp_list):
            stop = True

            # if all white faces are at the white side
            if 5 == cubies[13].pos2[0] and 5 == cubies[17].pos2[0] and 5 == cubies[21].pos2[0] and 5 == cubies[24].pos2[0]:
                if 3 == cubies[13].pos2[1] and 1 == cubies[17].pos2[1] and 5 == cubies[21].pos2[1] and 7 == cubies[24].pos2[1]:
                    break
                else:
                    # [18, 14, 22, 25]
                    if temp_list == [14, 25, 18, 22]:
                        rotate_down_prime_cubies(cubies, id_array)
                        break

                    if temp_list == [25, 22, 14, 18]:
                        rotate_down_cubies(cubies, id_array)
                        rotate_down_cubies(cubies, id_array)
                        break

                    if temp_list == [22, 18, 25, 14]:
                        rotate_down_cubies(cubies, id_array)
                        break

                    # Not yet implemented.


        else:
            if not is_in_layer(id_array, 3, 14):
                insert_to_white_cross(cubies, id_array, 14)

            if not is_in_layer(id_array, 3, 18):
                insert_to_white_cross(cubies, id_array, 18)

            if not is_in_layer(id_array, 3, 22):
                insert_to_white_cross(cubies, id_array, 22)

            if not is_in_layer(id_array, 3, 25):
                insert_to_white_cross(cubies, id_array, 25)



