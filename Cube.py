# Getter & Setter

def get_colors(window, liste):
    colors = [[None for i in range(9)] for j in range(6)]
    for side_idx, side in enumerate(colors):
        for piece_idx, color_ in enumerate(side):
            colors[side_idx][piece_idx] = window.itemcget(liste[side_idx][piece_idx], "fill")

    return colors


def set_colors(window, colors, cube):
    for side_idx, side in enumerate(colors):
        for piece_idx, piece in enumerate(side):
            window.itemconfigure(cube[side_idx][piece_idx], fill=piece)


# ________________________________________________________________________________________________________#

# rotate lists (functions, which are used in the real rotate-functions)


def rotate_front_list(liste):
    fronttemp0 = liste[1][0]
    fronttemp1 = liste[1][1]
    fronttemp2 = liste[1][2]
    fronttemp3 = liste[1][3]
    fronttemp4 = liste[1][4]
    fronttemp5 = liste[1][5]
    fronttemp6 = liste[1][6]
    fronttemp7 = liste[1][7]
    fronttemp8 = liste[1][8]
    liste[1][0] = fronttemp6
    liste[1][1] = fronttemp3
    liste[1][2] = fronttemp0
    liste[1][3] = fronttemp7
    liste[1][4] = fronttemp4
    liste[1][5] = fronttemp1
    liste[1][6] = fronttemp8
    liste[1][7] = fronttemp5
    liste[1][8] = fronttemp2
    obentemp1 = liste[0][6]
    obentemp2 = liste[0][7]
    obentemp3 = liste[0][8]
    rechtstemp1 = liste[2][0]
    rechtstemp2 = liste[2][3]
    rechtstemp3 = liste[2][6]
    untentemp1 = liste[5][0]
    untentemp2 = liste[5][1]
    untentemp3 = liste[5][2]
    linkstemp1 = liste[4][2]
    linkstemp2 = liste[4][5]
    linkstemp3 = liste[4][8]
    liste[0][6] = linkstemp3
    liste[0][7] = linkstemp2
    liste[0][8] = linkstemp1
    liste[2][0] = obentemp1
    liste[2][3] = obentemp2
    liste[2][6] = obentemp3
    liste[5][0] = rechtstemp3
    liste[5][1] = rechtstemp2
    liste[5][2] = rechtstemp1
    liste[4][2] = untentemp1
    liste[4][5] = untentemp2
    liste[4][8] = untentemp3
    return liste


def rotate_cube_right_list(liste):
    fronttemp = liste[1]
    righttemp = liste[2]
    backtemp = liste[3]
    lefttemp = liste[4]
    uptemp0 = liste[0][0]
    uptemp1 = liste[0][1]
    uptemp2 = liste[0][2]
    uptemp3 = liste[0][3]
    uptemp4 = liste[0][4]
    uptemp5 = liste[0][5]
    uptemp6 = liste[0][6]
    uptemp7 = liste[0][7]
    uptemp8 = liste[0][8]
    downtemp0 = liste[5][0]
    downtemp1 = liste[5][1]
    downtemp2 = liste[5][2]
    downtemp3 = liste[5][3]
    downtemp4 = liste[5][4]
    downtemp5 = liste[5][5]
    downtemp6 = liste[5][6]
    downtemp7 = liste[5][7]
    downtemp8 = liste[5][8]
    liste[2] = fronttemp
    liste[3] = righttemp
    liste[4] = backtemp
    liste[1] = lefttemp
    liste[0][0] = uptemp2
    liste[0][1] = uptemp5
    liste[0][2] = uptemp8
    liste[0][3] = uptemp1
    liste[0][4] = uptemp4
    liste[0][5] = uptemp7
    liste[0][6] = uptemp0
    liste[0][7] = uptemp3
    liste[0][8] = uptemp6
    liste[5][0] = downtemp6
    liste[5][1] = downtemp3
    liste[5][2] = downtemp0
    liste[5][3] = downtemp7
    liste[5][4] = downtemp4
    liste[5][5] = downtemp1
    liste[5][6] = downtemp8
    liste[5][7] = downtemp5
    liste[5][8] = downtemp2
    return liste


def rotate_cube_left_list(liste):
    rotate_cube_right_list(liste)
    rotate_cube_right_list(liste)
    rotate_cube_right_list(liste)
    return liste


def rotate_cube_up_list(liste):

    downtemp0 = liste[5][0]
    downtemp1 = liste[5][1]
    downtemp2 = liste[5][2]
    downtemp3 = liste[5][3]
    downtemp4 = liste[5][4]
    downtemp5 = liste[5][5]
    downtemp6 = liste[5][6]
    downtemp7 = liste[5][7]
    downtemp8 = liste[5][8]

    fronttemp0 = liste[1][0]
    fronttemp1 = liste[1][1]
    fronttemp2 = liste[1][2]
    fronttemp3 = liste[1][3]
    fronttemp4 = liste[1][4]
    fronttemp5 = liste[1][5]
    fronttemp6 = liste[1][6]
    fronttemp7 = liste[1][7]
    fronttemp8 = liste[1][8]

    righttemp0 = liste[2][0]
    righttemp1 = liste[2][1]
    righttemp2 = liste[2][2]
    righttemp3 = liste[2][3]
    righttemp4 = liste[2][4]
    righttemp5 = liste[2][5]
    righttemp6 = liste[2][6]
    righttemp7 = liste[2][7]
    righttemp8 = liste[2][8]

    lefttemp0 = liste[4][0]
    lefttemp1 = liste[4][1]
    lefttemp2 = liste[4][2]
    lefttemp3 = liste[4][3]
    lefttemp4 = liste[4][4]
    lefttemp5 = liste[4][5]
    lefttemp6 = liste[4][6]
    lefttemp7 = liste[4][7]
    lefttemp8 = liste[4][8]
    
    uptemp0 = liste[0][0]
    uptemp1 = liste[0][1]
    uptemp2 = liste[0][2]
    uptemp3 = liste[0][3]
    uptemp4 = liste[0][4]
    uptemp5 = liste[0][5]
    uptemp6 = liste[0][6]
    uptemp7 = liste[0][7]
    uptemp8 = liste[0][8]
    
    backtemp0 = liste[3][0]
    backtemp1 = liste[3][1]
    backtemp2 = liste[3][2]
    backtemp3 = liste[3][3]
    backtemp4 = liste[3][4]
    backtemp5 = liste[3][5]
    backtemp6 = liste[3][6]
    backtemp7 = liste[3][7]
    backtemp8 = liste[3][8]

    liste[2][0] = righttemp6
    liste[2][1] = righttemp3
    liste[2][2] = righttemp0
    liste[2][3] = righttemp7
    liste[2][4] = righttemp4
    liste[2][5] = righttemp1
    liste[2][6] = righttemp8
    liste[2][7] = righttemp5
    liste[2][8] = righttemp2

    liste[4][0] = lefttemp2
    liste[4][1] = lefttemp5
    liste[4][2] = lefttemp8
    liste[4][3] = lefttemp1
    liste[4][4] = lefttemp4
    liste[4][5] = lefttemp7
    liste[4][6] = lefttemp0
    liste[4][7] = lefttemp3
    liste[4][8] = lefttemp6

    liste[3][0] = uptemp8
    liste[3][1] = uptemp7
    liste[3][2] = uptemp6
    liste[3][3] = uptemp5
    liste[3][4] = uptemp4
    liste[3][5] = uptemp3
    liste[3][6] = uptemp2
    liste[3][7] = uptemp1
    liste[3][8] = uptemp0

    liste[5][0] = backtemp8
    liste[5][1] = backtemp7
    liste[5][2] = backtemp6
    liste[5][3] = backtemp5
    liste[5][4] = backtemp4
    liste[5][5] = backtemp3
    liste[5][6] = backtemp2
    liste[5][7] = backtemp1
    liste[5][8] = backtemp0

    liste[0][0] = fronttemp0
    liste[0][1] = fronttemp1
    liste[0][2] = fronttemp2
    liste[0][3] = fronttemp3
    liste[0][4] = fronttemp4
    liste[0][5] = fronttemp5
    liste[0][6] = fronttemp6
    liste[0][7] = fronttemp7
    liste[0][8] = fronttemp8
    
    liste[1][0] = downtemp0
    liste[1][1] = downtemp1
    liste[1][2] = downtemp2
    liste[1][3] = downtemp3
    liste[1][4] = downtemp4
    liste[1][5] = downtemp5
    liste[1][6] = downtemp6
    liste[1][7] = downtemp7
    liste[1][8] = downtemp8

    return liste


def rotate_cube_down_list(liste):
    rotate_cube_up_list(liste)
    rotate_cube_up_list(liste)
    rotate_cube_up_list(liste)
    return liste


def rotate_front_prime_list(liste):
    rotate_front_list(liste)
    rotate_front_list(liste)
    rotate_front_list(liste)
    return liste


def rotate_right_list(liste):
    rotate_cube_left_list(liste)
    rotate_front_list(liste)
    rotate_cube_right_list(liste)
    return liste


def rotate_right_prime_list(liste):
    rotate_cube_left_list(liste)
    rotate_front_prime_list(liste)
    rotate_cube_right_list(liste)
    return liste


def rotate_left_list(liste):
    rotate_cube_right_list(liste)
    rotate_front_list(liste)
    rotate_cube_left_list(liste)
    return liste


def rotate_left_prime_list(liste):
    rotate_cube_right_list(liste)
    rotate_front_prime_list(liste)
    rotate_cube_left_list(liste)
    return liste


def rotate_back_list(liste):
    rotate_cube_right_list(liste)
    rotate_cube_right_list(liste)
    rotate_front_list(liste)
    rotate_cube_right_list(liste)
    rotate_cube_right_list(liste)
    return liste


def rotate_back_prime_list(liste):
    rotate_cube_right_list(liste)
    rotate_cube_right_list(liste)
    rotate_front_prime_list(liste)
    rotate_cube_right_list(liste)
    rotate_cube_right_list(liste)
    return liste


def rotate_up_list(liste):
    rotate_cube_down_list(liste)
    rotate_front_list(liste)
    rotate_cube_up_list(liste)
    return liste


def rotate_up_prime_list(liste):
    rotate_cube_down_list(liste)
    rotate_front_prime_list(liste)
    rotate_cube_up_list(liste)
    return liste


def rotate_down_list(liste):
    rotate_cube_up_list(liste)
    rotate_front_list(liste)
    rotate_cube_down_list(liste)
    return liste


def rotate_down_prime_list(liste):
    rotate_cube_up_list(liste)
    rotate_front_prime_list(liste)
    rotate_cube_down_list(liste)
    return liste

# ________________________________________________________________________________________________________#

# rotate the cube

# rotations of parts of the cube
# "front" means the front part of the side of the cube etc.

def rotate_front(window, cube):
    colors = get_colors(window, cube)
    colors = rotate_front_list(colors)
    set_colors(window, colors, cube)


def rotate_front_prime(window, cube):
    colors = get_colors(window, cube)
    colors = rotate_front_prime_list(colors)
    set_colors(window, colors, cube)


def rotate_right(window, cube):
    colors = get_colors(window, cube)
    colors = rotate_right_list(colors)
    set_colors(window, colors, cube)


def rotate_right_prime(window, cube):
    colors = get_colors(window, cube)
    colors = rotate_right_prime_list(colors)
    set_colors(window, colors, cube)


def rotate_left(window, cube):
    colors = get_colors(window, cube)
    colors = rotate_left_list(colors)
    set_colors(window, colors, cube)


def rotate_left_prime(window, cube):
    colors = get_colors(window, cube)
    colors = rotate_left_prime_list(colors)
    set_colors(window, colors, cube)


def rotate_back(window, cube):
    colors = get_colors(window, cube)
    colors = rotate_back_list(colors)
    set_colors(window, colors, cube)


def rotate_back_prime(window, cube):
    colors = get_colors(window, cube)
    colors = rotate_back_prime_list(colors)
    set_colors(window, colors, cube)


def rotate_up(window, cube):
    colors = get_colors(window, cube)
    colors = rotate_up_list(colors)
    set_colors(window, colors, cube)


def rotate_up_prime(window, cube):
    colors = get_colors(window, cube)
    colors = rotate_up_prime_list(colors)
    set_colors(window, colors, cube)


def rotate_down(window, cube):
    colors = get_colors(window, cube)
    colors = rotate_down_list(colors)
    set_colors(window, colors, cube)


def rotate_down_prime(window, cube):
    colors = get_colors(window, cube)
    colors = rotate_down_prime_list(colors)
    set_colors(window, colors, cube)


# ------------------------------------------------#


# rotations of the whole cube

def rotate_cube_right(window, cube):
    colors = get_colors(window, cube)
    colors = rotate_cube_right_list(colors)
    set_colors(window, colors, cube)


def rotate_cube_left(window, cube):
    colors = get_colors(window, cube)
    colors = rotate_cube_left_list(colors)
    set_colors(window, colors, cube)


def rotate_cube_up(window, cube):
    colors = get_colors(window, cube)
    colors = rotate_cube_up_list(colors)
    set_colors(window, colors, cube)


def rotate_cube_down(window, cube):
    colors = get_colors(window, cube)
    colors = rotate_cube_down_list(colors)
    set_colors(window, colors, cube)


# ________________________________________________________________________________________________________#
