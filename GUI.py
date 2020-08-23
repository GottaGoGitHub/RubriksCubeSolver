from CubeMesh import *
from itertools import permutations


def evaluate_input(window, answer1, answer2, cube, cubies, error_label):
    # This function shall be called with the two entries (answer1, answer2) and evaluates their input

    # Depending on the input of answer1 and answer2 the corresponding face and piece of the cube will be selected
    # and colored. Therefore a window and a cube have to be committed as well.

    string_of_answer1 = answer1.get()
    string_of_answer2 = answer2.get()

    if len(string_of_answer1) > 0 and len(string_of_answer2) > 0:
        # Converting the strings for a less difficult evaluation

        # Lower case
        string_of_answer1 = string_of_answer1.lower()
        string_of_answer2 = string_of_answer2.lower()

        # Removing white spaces
        string_of_answer1 = string_of_answer1.replace(" ", "")
        string_of_answer2 = string_of_answer2.replace(" ", "")

        # Casting the Strings to an list
        list_of_answer1 = list(string_of_answer1)
        list_of_answer2 = list(string_of_answer2)

        # defining side_idx as index for the side of the cube and piece_idx for the piece
        # color is a string which represents the color
        side_idx = 0
        piece_idx = 0
        color = ""

        # Evaluation of the first answer
        if "u" == list_of_answer1[0]:
            side_idx = 0

        if "f" == list_of_answer1[0]:
            side_idx = 1

        if "r" == list_of_answer1[0]:
            side_idx = 2

        if "b" == list_of_answer1[0]:
            side_idx = 3

        if "l" == list_of_answer1[0]:
            side_idx = 4

        if "d" == list_of_answer1[0]:
            side_idx = 5

        # Evaluation of the second answer

        # Which piece shall be chosen?
        if "0" == list_of_answer2[0]:
            piece_idx = 0
            error_label.grid_forget()

        if "1" == list_of_answer2[0]:
            piece_idx = 1
            error_label.grid_forget()

        if "2" == list_of_answer2[0]:
            piece_idx = 2
            error_label.grid_forget()

        if "3" == list_of_answer2[0]:
            piece_idx = 3
            error_label.grid_forget()

        if "4" == list_of_answer2[0]:
            error_label.configure(text="The index 4 is invalid. The cross of the cube can not be modified!", fg="red")
            error_label.grid(row=4, column=0)

        if "5" == list_of_answer2[0]:
            piece_idx = 5
            error_label.grid_forget()

        if "6" == list_of_answer2[0]:
            piece_idx = 6
            error_label.grid_forget()

        if "7" == list_of_answer2[0]:
            piece_idx = 7
            error_label.grid_forget()

        if "8" == list_of_answer2[0]:
            piece_idx = 8
            error_label.grid_forget()

        # Choosing the color.
        if "y" == list_of_answer2[1]:
            color = "yellow"

        if "b" == list_of_answer2[1]:
            color = "blue"

        if "r" == list_of_answer2[1]:
            color = "red"

        if "g" == list_of_answer2[1]:
            color = "green"

        if "o" == list_of_answer2[1]:
            color = "orange"

        if "w" == list_of_answer2[1]:
            color = "white"

        # Coloring the piece
        if "4" != list_of_answer2[0]:

            ids = get_id_from_cubies(cubies)
            temp_id = ids[side_idx][piece_idx]
            number = int(temp_id[0:2])
            number_color = int(temp_id[3])

            if 1 == number_color:
                cubies[number-1].color1 = color
            if 2 == number_color:
                cubies[int(temp_id[0:2])-1].color2 = color
            if 3 == number_color:
                cubies[int(temp_id[0:2])-1].color3 = color

            set_colors(window, get_colors_from_cubies(cubies), cube)

        # Deleting answer 2 for better user experience
        answer2.delete(0, END)


def actualize_id_array(solved_cubies, id_array, colors):
    cubies_positions = [[[0, 0], [4, 0], [3, 2]],
                        [[0, 1], [3, 1]],
                        [[0, 2], [2, 2], [3, 0]],
                        [[0, 3], [4, 1]],
                        [[0, 5], [2, 1]],
                        [[0, 6], [4, 2], [1, 0]],
                        [[0, 7], [1, 1]],
                        [[0, 8], [1, 2], [2, 0]],
                        [[4, 3], [3, 5]],
                        [[4, 5], [1, 3]],
                        [[4, 6], [3, 8], [5, 6]],
                        [[4, 7], [5, 3]],
                        [[4, 8], [1, 6], [5, 0]],
                        [[1, 5], [2, 3]],
                        [[1, 7], [5, 1]],
                        [[1, 8], [2, 6], [5, 2]],
                        [[2, 5], [3, 3]],
                        [[2, 7], [5, 5]],
                        [[2, 8], [3, 6], [5, 8]],
                        [[3, 7], [5, 7]]]

    for positions_of_cubie in cubies_positions:
        temp_colors = []

        for pos in positions_of_cubie:
            temp_colors.append(colors[pos[0]][pos[1]])

        perm_temp_colors = permutations(temp_colors)
        perm_temp_colors_list = []

        for i in perm_temp_colors:
            perm_temp_colors_list.append(list(i))

        filtered = list(filter(lambda cubie: cubie.colors in perm_temp_colors_list, solved_cubies))

        for i, element in enumerate(temp_colors):
            if element == filtered[0].color1:
                filtered[0].pos1 = positions_of_cubie[i]
                id_array[positions_of_cubie[i][0]][positions_of_cubie[i][1]] = filtered[0].id1

            if element == filtered[0].color2:
                filtered[0].pos2 = positions_of_cubie[i]
                id_array[positions_of_cubie[i][0]][positions_of_cubie[i][1]] = filtered[0].id2

            if element == filtered[0].color3:
                filtered[0].pos3 = positions_of_cubie[i]
                id_array[positions_of_cubie[i][0]][positions_of_cubie[i][1]] = filtered[0].id3

    return solved_cubies

def generate_prompt(window, font1, font2):
    # Generating the user prompt
    grid_prompt = grid3x3(window, 380, 65)
    line_1 = window.create_text(188, 10, text="The faces of the cube can be accessed via: front, left, right, up, down")
    line_2 = window.create_text(228, 25,
                                text="To access the pieces, have a look for the numeration in the upper right hand corner.")
    line_3 = window.create_text(196, 40,
                                text="The following colors are allowed: orange, blue, red, white, green, yellow")
    line_4 = window.create_text(218, 55,
                                text="The input is not case sensitive and works also with just the first letter of a word.")

    # Index Numbers for the grid of the prompt
    text_0 = window.create_text(395, 80, text="0")
    text_1 = window.create_text(430, 80, text="1")
    text_2 = window.create_text(465, 80, text="2")
    text_3 = window.create_text(395, 115, text="3")
    # INDEX 4 IS INVALID
    text_5 = window.create_text(465, 115, text="5")
    text_6 = window.create_text(395, 147, text="6")
    text_7 = window.create_text(430, 147, text="7")
    text_8 = window.create_text(465, 147, text="8")

    # Setting the fond for the user prompt
    window.itemconfigure(line_1, font=font1)
    window.itemconfigure(line_2, font=font1)
    window.itemconfigure(line_3, font=font1)
    window.itemconfigure(line_4, font=font1)
    window.itemconfigure(text_0, font=font2)
    window.itemconfigure(text_1, font=font2)
    window.itemconfigure(text_2, font=font2)
    window.itemconfigure(text_3, font=font2)
    window.itemconfigure(text_5, font=font2)
    window.itemconfigure(text_6, font=font2)
    window.itemconfigure(text_7, font=font2)
    window.itemconfigure(text_8, font=font2)
