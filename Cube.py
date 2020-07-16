# Getter & Setter
def set_colors(window, colors, cube):
    """
    sets the color of a cube which is represented by multiple rectangle objects
    """
    for side_idx, side in enumerate(colors):
        for piece_idx, piece in enumerate(side):
            window.itemconfigure(cube[side_idx][piece_idx], fill=piece)


def get_colors_from_cubies(cubies):
    """
    get the colors form a list of cubies
    and returns a list of colors (str)
    """
    colors = [[None for i in range(9)] for j in range(6)]

    for item in cubies:
        colors[item.pos1[0]][item.pos1[1]] = item.color1

        if 2 == item.number or 3 == item.number:
            colors[item.pos2[0]][item.pos2[1]] = item.color2

        if 3 == item.number:
            colors[item.pos3[0]][item.pos3[1]] = item.color3
    return colors


def get_id_from_cubies(cubies):
    """
    get the ID form a list of cubies
    and returns a list of IDs (str)
    """
    ids = [[None for i in range(9)] for j in range(6)]

    for item in cubies:
        ids[item.pos1[0]][item.pos1[1]] = item.id1

        if 2 == item.number or 3 == item.number:
            ids[item.pos2[0]][item.pos2[1]] = item.id2

        if 3 == item.number:
            ids[item.pos3[0]][item.pos3[1]] = item.id3
    return ids


# ________________________________________________________________________________________________________#
def actualize_cubie(cubies, id_array, temp_side, new_pos):
    """
    actualizing the position of the cubies
    in the id_array and the cubie it self
    """
    id_array[new_pos[0]][new_pos[1]] = temp_side
    temp_partition = temp_side.rpartition("0")
    name = int(temp_partition[0]) - 1

    if "1" == temp_partition[2]:
        cubies[name].pos1 = new_pos

    if "2" == temp_partition[2]:
        cubies[name].pos2 = new_pos

    if "3" == temp_partition[2]:
        cubies[name].pos3 = new_pos


# ________________________________________________________________________________________________________#

# rotate the cubies

# rotation-functions for rotating the whole cube
def rotate_cube_right_cubies(cubies, id_array):
    downtemp0 = id_array[5][0]
    downtemp1 = id_array[5][1]
    downtemp2 = id_array[5][2]
    downtemp3 = id_array[5][3]
    downtemp4 = id_array[5][4]
    downtemp5 = id_array[5][5]
    downtemp6 = id_array[5][6]
    downtemp7 = id_array[5][7]
    downtemp8 = id_array[5][8]

    fronttemp0 = id_array[1][0]
    fronttemp1 = id_array[1][1]
    fronttemp2 = id_array[1][2]
    fronttemp3 = id_array[1][3]
    fronttemp4 = id_array[1][4]
    fronttemp5 = id_array[1][5]
    fronttemp6 = id_array[1][6]
    fronttemp7 = id_array[1][7]
    fronttemp8 = id_array[1][8]

    righttemp0 = id_array[2][0]
    righttemp1 = id_array[2][1]
    righttemp2 = id_array[2][2]
    righttemp3 = id_array[2][3]
    righttemp4 = id_array[2][4]
    righttemp5 = id_array[2][5]
    righttemp6 = id_array[2][6]
    righttemp7 = id_array[2][7]
    righttemp8 = id_array[2][8]

    lefttemp0 = id_array[4][0]
    lefttemp1 = id_array[4][1]
    lefttemp2 = id_array[4][2]
    lefttemp3 = id_array[4][3]
    lefttemp4 = id_array[4][4]
    lefttemp5 = id_array[4][5]
    lefttemp6 = id_array[4][6]
    lefttemp7 = id_array[4][7]
    lefttemp8 = id_array[4][8]

    uptemp0 = id_array[0][0]
    uptemp1 = id_array[0][1]
    uptemp2 = id_array[0][2]
    uptemp3 = id_array[0][3]
    uptemp4 = id_array[0][4]
    uptemp5 = id_array[0][5]
    uptemp6 = id_array[0][6]
    uptemp7 = id_array[0][7]
    uptemp8 = id_array[0][8]

    backtemp0 = id_array[3][0]
    backtemp1 = id_array[3][1]
    backtemp2 = id_array[3][2]
    backtemp3 = id_array[3][3]
    backtemp4 = id_array[3][4]
    backtemp5 = id_array[3][5]
    backtemp6 = id_array[3][6]
    backtemp7 = id_array[3][7]
    backtemp8 = id_array[3][8]

    actualize_cubie(cubies, id_array, uptemp2, [0, 0])
    actualize_cubie(cubies, id_array, uptemp5, [0, 1])
    actualize_cubie(cubies, id_array, uptemp8, [0, 2])
    actualize_cubie(cubies, id_array, uptemp1, [0, 3])
    actualize_cubie(cubies, id_array, uptemp4, [0, 4])
    actualize_cubie(cubies, id_array, uptemp7, [0, 5])
    actualize_cubie(cubies, id_array, uptemp0, [0, 6])
    actualize_cubie(cubies, id_array, uptemp3, [0, 7])
    actualize_cubie(cubies, id_array, uptemp6, [0, 8])

    actualize_cubie(cubies, id_array, downtemp6, [5, 0])
    actualize_cubie(cubies, id_array, downtemp3, [5, 1])
    actualize_cubie(cubies, id_array, downtemp0, [5, 2])
    actualize_cubie(cubies, id_array, downtemp7, [5, 3])
    actualize_cubie(cubies, id_array, downtemp4, [5, 4])
    actualize_cubie(cubies, id_array, downtemp1, [5, 5])
    actualize_cubie(cubies, id_array, downtemp8, [5, 6])
    actualize_cubie(cubies, id_array, downtemp5, [5, 7])
    actualize_cubie(cubies, id_array, downtemp2, [5, 8])

    actualize_cubie(cubies, id_array, lefttemp0, [1, 0])
    actualize_cubie(cubies, id_array, lefttemp1, [1, 1])
    actualize_cubie(cubies, id_array, lefttemp2, [1, 2])
    actualize_cubie(cubies, id_array, lefttemp3, [1, 3])
    actualize_cubie(cubies, id_array, lefttemp4, [1, 4])
    actualize_cubie(cubies, id_array, lefttemp5, [1, 5])
    actualize_cubie(cubies, id_array, lefttemp6, [1, 6])
    actualize_cubie(cubies, id_array, lefttemp7, [1, 7])
    actualize_cubie(cubies, id_array, lefttemp8, [1, 8])

    actualize_cubie(cubies, id_array, fronttemp0, [2, 0])
    actualize_cubie(cubies, id_array, fronttemp1, [2, 1])
    actualize_cubie(cubies, id_array, fronttemp2, [2, 2])
    actualize_cubie(cubies, id_array, fronttemp3, [2, 3])
    actualize_cubie(cubies, id_array, fronttemp4, [2, 4])
    actualize_cubie(cubies, id_array, fronttemp5, [2, 5])
    actualize_cubie(cubies, id_array, fronttemp6, [2, 6])
    actualize_cubie(cubies, id_array, fronttemp7, [2, 7])
    actualize_cubie(cubies, id_array, fronttemp8, [2, 8])

    actualize_cubie(cubies, id_array, righttemp0, [3, 0])
    actualize_cubie(cubies, id_array, righttemp1, [3, 1])
    actualize_cubie(cubies, id_array, righttemp2, [3, 2])
    actualize_cubie(cubies, id_array, righttemp3, [3, 3])
    actualize_cubie(cubies, id_array, righttemp4, [3, 4])
    actualize_cubie(cubies, id_array, righttemp5, [3, 5])
    actualize_cubie(cubies, id_array, righttemp6, [3, 6])
    actualize_cubie(cubies, id_array, righttemp7, [3, 7])
    actualize_cubie(cubies, id_array, righttemp8, [3, 8])

    actualize_cubie(cubies, id_array, backtemp0, [4, 0])
    actualize_cubie(cubies, id_array, backtemp1, [4, 1])
    actualize_cubie(cubies, id_array, backtemp2, [4, 2])
    actualize_cubie(cubies, id_array, backtemp3, [4, 3])
    actualize_cubie(cubies, id_array, backtemp4, [4, 4])
    actualize_cubie(cubies, id_array, backtemp5, [4, 5])
    actualize_cubie(cubies, id_array, backtemp6, [4, 6])
    actualize_cubie(cubies, id_array, backtemp7, [4, 7])
    actualize_cubie(cubies, id_array, backtemp8, [4, 8])


def rotate_cube_left_cubies(cubies, id_array):
    rotate_cube_right_cubies(cubies, id_array)
    rotate_cube_right_cubies(cubies, id_array)
    rotate_cube_right_cubies(cubies, id_array)


def rotate_cube_up_cubies(cubies, id_array):
    downtemp0 = id_array[5][0]
    downtemp1 = id_array[5][1]
    downtemp2 = id_array[5][2]
    downtemp3 = id_array[5][3]
    downtemp4 = id_array[5][4]
    downtemp5 = id_array[5][5]
    downtemp6 = id_array[5][6]
    downtemp7 = id_array[5][7]
    downtemp8 = id_array[5][8]

    fronttemp0 = id_array[1][0]
    fronttemp1 = id_array[1][1]
    fronttemp2 = id_array[1][2]
    fronttemp3 = id_array[1][3]
    fronttemp4 = id_array[1][4]
    fronttemp5 = id_array[1][5]
    fronttemp6 = id_array[1][6]
    fronttemp7 = id_array[1][7]
    fronttemp8 = id_array[1][8]

    righttemp0 = id_array[2][0]
    righttemp1 = id_array[2][1]
    righttemp2 = id_array[2][2]
    righttemp3 = id_array[2][3]
    righttemp4 = id_array[2][4]
    righttemp5 = id_array[2][5]
    righttemp6 = id_array[2][6]
    righttemp7 = id_array[2][7]
    righttemp8 = id_array[2][8]

    lefttemp0 = id_array[4][0]
    lefttemp1 = id_array[4][1]
    lefttemp2 = id_array[4][2]
    lefttemp3 = id_array[4][3]
    lefttemp4 = id_array[4][4]
    lefttemp5 = id_array[4][5]
    lefttemp6 = id_array[4][6]
    lefttemp7 = id_array[4][7]
    lefttemp8 = id_array[4][8]

    uptemp0 = id_array[0][0]
    uptemp1 = id_array[0][1]
    uptemp2 = id_array[0][2]
    uptemp3 = id_array[0][3]
    uptemp4 = id_array[0][4]
    uptemp5 = id_array[0][5]
    uptemp6 = id_array[0][6]
    uptemp7 = id_array[0][7]
    uptemp8 = id_array[0][8]

    backtemp0 = id_array[3][0]
    backtemp1 = id_array[3][1]
    backtemp2 = id_array[3][2]
    backtemp3 = id_array[3][3]
    backtemp4 = id_array[3][4]
    backtemp5 = id_array[3][5]
    backtemp6 = id_array[3][6]
    backtemp7 = id_array[3][7]
    backtemp8 = id_array[3][8]

    actualize_cubie(cubies, id_array, righttemp6, [2, 0])
    actualize_cubie(cubies, id_array, righttemp3, [2, 1])
    actualize_cubie(cubies, id_array, righttemp0, [2, 2])
    actualize_cubie(cubies, id_array, righttemp7, [2, 3])
    actualize_cubie(cubies, id_array, righttemp4, [2, 4])
    actualize_cubie(cubies, id_array, righttemp1, [2, 5])
    actualize_cubie(cubies, id_array, righttemp8, [2, 6])
    actualize_cubie(cubies, id_array, righttemp5, [2, 7])
    actualize_cubie(cubies, id_array, righttemp2, [2, 8])

    actualize_cubie(cubies, id_array, lefttemp2, [4, 0])
    actualize_cubie(cubies, id_array, lefttemp5, [4, 1])
    actualize_cubie(cubies, id_array, lefttemp8, [4, 2])
    actualize_cubie(cubies, id_array, lefttemp1, [4, 3])
    actualize_cubie(cubies, id_array, lefttemp4, [4, 4])
    actualize_cubie(cubies, id_array, lefttemp7, [4, 5])
    actualize_cubie(cubies, id_array, lefttemp0, [4, 6])
    actualize_cubie(cubies, id_array, lefttemp3, [4, 7])
    actualize_cubie(cubies, id_array, lefttemp6, [4, 8])

    actualize_cubie(cubies, id_array, uptemp8, [3, 0])
    actualize_cubie(cubies, id_array, uptemp7, [3, 1])
    actualize_cubie(cubies, id_array, uptemp6, [3, 2])
    actualize_cubie(cubies, id_array, uptemp5, [3, 3])
    actualize_cubie(cubies, id_array, uptemp4, [3, 4])
    actualize_cubie(cubies, id_array, uptemp3, [3, 5])
    actualize_cubie(cubies, id_array, uptemp2, [3, 6])
    actualize_cubie(cubies, id_array, uptemp1, [3, 7])
    actualize_cubie(cubies, id_array, uptemp0, [3, 8])

    actualize_cubie(cubies, id_array, backtemp8, [5, 0])
    actualize_cubie(cubies, id_array, backtemp7, [5, 1])
    actualize_cubie(cubies, id_array, backtemp6, [5, 2])
    actualize_cubie(cubies, id_array, backtemp5, [5, 3])
    actualize_cubie(cubies, id_array, backtemp4, [5, 4])
    actualize_cubie(cubies, id_array, backtemp3, [5, 5])
    actualize_cubie(cubies, id_array, backtemp2, [5, 6])
    actualize_cubie(cubies, id_array, backtemp1, [5, 7])
    actualize_cubie(cubies, id_array, backtemp0, [5, 8])

    actualize_cubie(cubies, id_array, fronttemp0, [0, 0])
    actualize_cubie(cubies, id_array, fronttemp1, [0, 1])
    actualize_cubie(cubies, id_array, fronttemp2, [0, 2])
    actualize_cubie(cubies, id_array, fronttemp3, [0, 3])
    actualize_cubie(cubies, id_array, fronttemp4, [0, 4])
    actualize_cubie(cubies, id_array, fronttemp5, [0, 5])
    actualize_cubie(cubies, id_array, fronttemp6, [0, 6])
    actualize_cubie(cubies, id_array, fronttemp7, [0, 7])
    actualize_cubie(cubies, id_array, fronttemp8, [0, 8])

    actualize_cubie(cubies, id_array, downtemp0, [1, 0])
    actualize_cubie(cubies, id_array, downtemp1, [1, 1])
    actualize_cubie(cubies, id_array, downtemp2, [1, 2])
    actualize_cubie(cubies, id_array, downtemp3, [1, 3])
    actualize_cubie(cubies, id_array, downtemp4, [1, 4])
    actualize_cubie(cubies, id_array, downtemp5, [1, 5])
    actualize_cubie(cubies, id_array, downtemp6, [1, 6])
    actualize_cubie(cubies, id_array, downtemp7, [1, 7])
    actualize_cubie(cubies, id_array, downtemp8, [1, 8])


def rotate_cube_down_cubies(cubies, id_array):
    rotate_cube_up_cubies(cubies, id_array)
    rotate_cube_up_cubies(cubies, id_array)
    rotate_cube_up_cubies(cubies, id_array)


def rotate_front_cubies(cubies, id_array):
    # temp values (identifier)
    fronttemp0 = id_array[1][0]
    fronttemp1 = id_array[1][1]
    fronttemp2 = id_array[1][2]
    fronttemp3 = id_array[1][3]
    fronttemp4 = id_array[1][4]
    fronttemp5 = id_array[1][5]
    fronttemp6 = id_array[1][6]
    fronttemp7 = id_array[1][7]
    fronttemp8 = id_array[1][8]
    obentemp1 = id_array[0][6]
    obentemp2 = id_array[0][7]
    obentemp3 = id_array[0][8]
    rechtstemp1 = id_array[2][0]
    rechtstemp2 = id_array[2][3]
    rechtstemp3 = id_array[2][6]
    untentemp1 = id_array[5][0]
    untentemp2 = id_array[5][1]
    untentemp3 = id_array[5][2]
    linkstemp1 = id_array[4][2]
    linkstemp2 = id_array[4][5]
    linkstemp3 = id_array[4][8]

    # swapping the elements
    actualize_cubie(cubies, id_array, fronttemp6, [1, 0])
    actualize_cubie(cubies, id_array, fronttemp3, [1, 1])
    actualize_cubie(cubies, id_array, fronttemp0, [1, 2])
    actualize_cubie(cubies, id_array, fronttemp7, [1, 3])
    actualize_cubie(cubies, id_array, fronttemp4, [1, 4])
    actualize_cubie(cubies, id_array, fronttemp1, [1, 5])
    actualize_cubie(cubies, id_array, fronttemp8, [1, 6])
    actualize_cubie(cubies, id_array, fronttemp5, [1, 7])
    actualize_cubie(cubies, id_array, fronttemp2, [1, 8])
    actualize_cubie(cubies, id_array, linkstemp3, [0, 6])
    actualize_cubie(cubies, id_array, linkstemp2, [0, 7])
    actualize_cubie(cubies, id_array, linkstemp1, [0, 8])
    actualize_cubie(cubies, id_array, obentemp1, [2, 0])
    actualize_cubie(cubies, id_array, obentemp2, [2, 3])
    actualize_cubie(cubies, id_array, obentemp3, [2, 6])
    actualize_cubie(cubies, id_array, rechtstemp3, [5, 0])
    actualize_cubie(cubies, id_array, rechtstemp2, [5, 1])
    actualize_cubie(cubies, id_array, rechtstemp1, [5, 2])
    actualize_cubie(cubies, id_array, untentemp1, [4, 2])
    actualize_cubie(cubies, id_array, untentemp2, [4, 5])
    actualize_cubie(cubies, id_array, untentemp3, [4, 8])



# ---------------------------------------------------------------------------#
# rotations of parts of the cube

# "front" means the front part of the side of the cube etc.


def rotate_front_prime_cubies(cubies, id_array):
    rotate_front_cubies(cubies, id_array)
    rotate_front_cubies(cubies, id_array)
    rotate_front_cubies(cubies, id_array)
    

def rotate_right_cubies(cubies, id_array):
    rotate_cube_left_cubies(cubies, id_array)
    rotate_front_cubies(cubies, id_array)
    rotate_cube_right_cubies(cubies, id_array)


def rotate_right_prime_cubies(cubies, id_array):
    rotate_cube_left_cubies(cubies, id_array)
    rotate_front_prime_cubies(cubies, id_array)
    rotate_cube_right_cubies(cubies, id_array)


def rotate_left_cubies(cubies, id_array):
    rotate_cube_right_cubies(cubies, id_array)
    rotate_front_cubies(cubies, id_array)
    rotate_cube_left_cubies(cubies, id_array)


def rotate_left_prime_cubies(cubies, id_array):
    rotate_cube_right_cubies(cubies, id_array)
    rotate_front_prime_cubies(cubies, id_array)
    rotate_cube_left_cubies(cubies, id_array)


def rotate_back_cubies(cubies, id_array):
    rotate_cube_right_cubies(cubies, id_array)
    rotate_cube_right_cubies(cubies, id_array)
    rotate_front_cubies(cubies, id_array)
    rotate_cube_right_cubies(cubies, id_array)
    rotate_cube_right_cubies(cubies, id_array)


def rotate_back_prime_cubies(cubies, id_array):
    rotate_cube_right_cubies(cubies, id_array)
    rotate_cube_right_cubies(cubies, id_array)
    rotate_front_prime_cubies(cubies, id_array)
    rotate_cube_right_cubies(cubies, id_array)
    rotate_cube_right_cubies(cubies, id_array)


def rotate_up_cubies(cubies, id_array):
    rotate_cube_down_cubies(cubies, id_array)
    rotate_front_cubies(cubies, id_array)
    rotate_cube_up_cubies(cubies, id_array)


def rotate_up_prime_cubies(cubies, id_array):
    rotate_cube_down_cubies(cubies, id_array)
    rotate_front_prime_cubies(cubies, id_array)
    rotate_cube_up_cubies(cubies, id_array)


def rotate_down_cubies(cubies, id_array):
    rotate_cube_up_cubies(cubies, id_array)
    rotate_front_cubies(cubies, id_array)
    rotate_cube_down_cubies(cubies, id_array)


def rotate_down_prime_cubies(cubies, id_array):
    rotate_cube_up_cubies(cubies, id_array)
    rotate_front_prime_cubies(cubies, id_array)
    rotate_cube_down_cubies(cubies, id_array)

# ________________________________________________________________________________________________________#


def rotate_by_side_idx(cubies, id_array, side_idx):
    if 0 == side_idx:
        rotate_up_cubies(cubies, id_array)
    if 1 == side_idx:
        rotate_front_cubies(cubies, id_array)
    if 2 == side_idx:
        rotate_right_cubies(cubies, id_array)
    if 3 == side_idx:
        rotate_back_cubies(cubies, id_array)
    if 4 == side_idx:
        rotate_left_cubies(cubies, id_array)
    if 5 == side_idx:
        rotate_down_cubies(cubies, id_array)


def rotate_prime_by_side_idx(cubies, id_array, side_idx):
    if 0 == side_idx:
        rotate_up_prime_cubies(cubies, id_array)
    if 1 == side_idx:
        rotate_front_prime_cubies(cubies, id_array)
    if 2 == side_idx:
        rotate_right_prime_cubies(cubies, id_array)
    if 3 == side_idx:
        rotate_back_prime_cubies(cubies, id_array)
    if 4 == side_idx:
        rotate_left_prime_cubies(cubies, id_array)
    if 5 == side_idx:
        rotate_down_prime_cubies(cubies, id_array)
