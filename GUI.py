from CubeMesh import *
from ListRotations import *
from tkinter import messagebox
from itertools import permutations
from copy import deepcopy
from FileHandler import *


def evaluate_input(window, answer1, answer2, cube, cubies, error_label):
    """ This function shall be called with the two entries (answer1, answer2) and evaluates their input

    Depending on the input of answer1 and answer2 the corresponding face and piece of the cube will be selected
    and colored. Therefore a window and a cube have to be committed as well.
    """

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

        # Coloring the piece, except its a centre piece
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


def actualize_id_array(cubies_list, solved_cubies, id_array, colors, error):
    """
    Actualizes the id_array by comparing the cubies of the input/scrambled cube with the solved cube.
    """
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

    # boolean for error message
    exists_cubie_with_false_colors = False

    # for each position, which resembles a single cubie in the list above; do
    for positions_of_cubie in cubies_positions:
        temp_colors = []

        # Each cube has 2 - 3 colors, add each color to the current list of colors
        for pos in positions_of_cubie:
            temp_colors.append(colors[pos[0]][pos[1]])

        # generate permutations of the colors
        perm_temp_colors = permutations(temp_colors)
        perm_temp_colors_list = []

        # permutations returns a n-tupel therefore we are casting the content to a list
        for i in perm_temp_colors:
            perm_temp_colors_list.append(list(i))

        # gets the cubie which has the corresponding colors from the solved cubies
        # its needed to write the correct ids into the id_array
        filtered = list(filter(lambda cubie: cubie.colors in perm_temp_colors_list, solved_cubies))

        # filtered is always a list with len(1) if there is a cubie which has the colors
        # filtered will be empty if there is somehow no cubie which has the colors
        # the boolean (exists_cubie_with_false_colors) will be set to TRUE to throw an user prompt
        # the corresponding fields are going to be set to blank/grey
        if len(filtered) == 0:
            exists_cubie_with_false_colors = True

            # finding the cube in the list of unsolved cubes
            filter_unsolved = list(filter(lambda cubie: cubie.colors in perm_temp_colors_list, cubies_list))

            # removing false colors
            filter_unsolved[0].color1 = "grey"
            filter_unsolved[0].color2 = "grey"

            if filter_unsolved[0].number == 3:
                filter_unsolved[0].color3 = "grey"
                filter_unsolved[0].colors = ["grey", "grey", "grey"]
            else:
                filter_unsolved[0].colors = ["grey", "grey"]

        # Actualizing the entries in the id_array based on the IDs of the solved cubies
        else:
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

    # User prompt and error messages
    if exists_cubie_with_false_colors:
        messagebox.showerror(title="Invalid coloring", message="Some of the colors were not correct, please set the "
                                                               "colors for the grey fields again and submit again.")
        error[0] == True
    else:
        messagebox.showinfo(title="Successful", message="Submission successful.")


def correct_cubies_list(id_array, cubies, solved_cubies, error):
    """
    Correcting the entries (position/color) of the unsolved cubies based on the id_array and solved_cubies.
    """
    if not error[0]:
        # Going through all the fields of the id_array and overwrite the current values of the corresponding cubie
        for i, side in enumerate(id_array):
            for j, identifier in enumerate(side):
                temp = identifier.rpartition("0")
                cubies_number = int(temp[0]) - 1
                
                if temp[2] == "1":
                    cubies[cubies_number].pos1[0] = i
                    cubies[cubies_number].pos1[1] = j
                    cubies[cubies_number].color1 = solved_cubies[cubies_number].color1

                if temp[2] == "2":
                    cubies[cubies_number].pos2[0] = i
                    cubies[cubies_number].pos2[1] = j
                    cubies[cubies_number].color2 = solved_cubies[cubies_number].color2

                if temp[2] == "3":
                    cubies[cubies_number].pos3[0] = i
                    cubies[cubies_number].pos3[1] = j
                    cubies[cubies_number].color3 = solved_cubies[cubies_number].color3

            
def generate_prompt(window, font1, font2):
    """ Generating the user prompt with fixed positions and values."""

    # example grid in the upper right hand corner
    grid_prompt = grid3x3(window, 380, 65)

    # Text lines in the upper left hand corner.
    line_1 = window.create_text(188, 10, text="The faces of the cube can be accessed via: front, left, right, up, down")
    line_2 = window.create_text(228, 25,
                                text="To access the pieces, have a look for the numeration in the upper right hand corner.")
    line_3 = window.create_text(200, 40,
                                text="The following colors are allowed: orange, blue, red, white, green, yellow")
    line_4 = window.create_text(218, 55,
                                text="The input is not case sensitive and works also with just the first letter of a word.")

    # Index Numbers for the grid of the prompt
    text_0 = window.create_text(395, 80, text="0")
    text_1 = window.create_text(430, 80, text="1")
    text_2 = window.create_text(465, 80, text="2")
    text_3 = window.create_text(395, 115, text="3")
    # INDEX 4 IS INVALID AND WILL NOT BE DISPLAYED
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


def next_step(window, colors, cube, optimized_array, start_idx):
    """
    Actualizes the display of the current state to the state when the next rotation was executed.

    Evaluates the rotation acronyms ("x","x'", etc.) of the optimized_array and calls the corresponding rotation
    function explicit for the display. The cubies are not affected at all!
    """

    if start_idx[0] >= len(optimized_array):
        print("There is no next step.")

    elif optimized_array[start_idx[0]] == "x":
        rotate_cube_right_list(colors)

    elif optimized_array[start_idx[0]] == "x'":
        rotate_cube_left_list(colors)

    elif optimized_array[start_idx[0]] == "y":
        rotate_cube_up_list(colors)

    elif optimized_array[start_idx[0]] == "y'":
        rotate_cube_down_list(colors)

    elif optimized_array[start_idx[0]] == "F":
        rotate_front_list(colors)

    elif optimized_array[start_idx[0]] == "F'":
        rotate_front_prime_list(colors)

    elif optimized_array[start_idx[0]] == "B":
        rotate_back_list(colors)

    elif optimized_array[start_idx[0]] == "B'":
        rotate_back_prime_list(colors)

    elif optimized_array[start_idx[0]] == "R":
        rotate_right_list(colors)

    elif optimized_array[start_idx[0]] == "R'":
        rotate_right_prime_list(colors)

    elif optimized_array[start_idx[0]] == "L":
        rotate_left_list(colors)

    elif optimized_array[start_idx[0]] == "L'":
        rotate_left_prime_list(colors)

    elif optimized_array[start_idx[0]] == "U":
        rotate_up_list(colors)

    elif optimized_array[start_idx[0]] == "U'":
        rotate_up_prime_list(colors)

    elif optimized_array[start_idx[0]] == "D":
        rotate_down_list(colors)

    elif optimized_array[start_idx[0]] == "D'":
        rotate_down_prime_list(colors)

    set_colors(window, colors, cube)


def previous_step(window, colors, cube, optimized_array, start_idx):
    """
    Actualizes the display of the current state to the state before the rotation was executed.

    Evaluates the rotation acronyms ("x","x'", etc.) of the optimized_array and calls the corresponding inverted
    rotation function explicit for the display. The cubies are not affected at all!
    """

    if start_idx[0] < 0:
        print("There is no previous step.")
    
    elif optimized_array[start_idx[0]] == "x":
        rotate_cube_left_list(colors)

    elif optimized_array[start_idx[0]] == "x'":
        rotate_cube_right_list(colors)

    elif optimized_array[start_idx[0]] == "y":
        rotate_cube_down_list(colors)

    elif optimized_array[start_idx[0]] == "y'":
        rotate_cube_up_list(colors)

    elif optimized_array[start_idx[0]] == "F":
        rotate_front_prime_list(colors)

    elif optimized_array[start_idx[0]] == "F'":
        rotate_front_list(colors)

    elif optimized_array[start_idx[0]] == "B":
        rotate_back_prime_list(colors)

    elif optimized_array[start_idx[0]] == "B'":
        rotate_back_list(colors)

    elif optimized_array[start_idx[0]] == "R":
        rotate_right_prime_list(colors)

    elif optimized_array[start_idx[0]] == "R'":
        rotate_right_list(colors)

    elif optimized_array[start_idx[0]] == "L":
        rotate_left_prime_list(colors)

    elif optimized_array[start_idx[0]] == "L'":
        rotate_left_list(colors)

    elif optimized_array[start_idx[0]] == "U":
        rotate_up_prime_list(colors)

    elif optimized_array[start_idx[0]] == "U'":
        rotate_up_list(colors)

    elif optimized_array[start_idx[0]] == "D":
        rotate_down_prime_list(colors)

    elif optimized_array[start_idx[0]] == "D'":
        rotate_down_list(colors)

    set_colors(window, colors, cube)


def create_sentence(letter):
    """
    Converts the rotation acronyms ("x","x'", etc.) to an actual sentence.
    """

    sentence = "Invalid operation."

    if letter == "x":
        sentence = "Rotate the cube to the right."

    elif letter == "x'":
        sentence = "Rotate the cube to the left."

    elif letter == "y":
        sentence = "Rotate the cube upwards."

    elif letter == "y'":
        sentence = "Rotate the cube downwards."

    elif letter == "F":
        sentence = "Rotate the front side clockwise."

    elif letter == "F'":
        sentence = "Rotate the front side counterclockwise."

    elif letter == "B":
        sentence = "Rotate the back side clockwise."

    elif letter == "B'":
        sentence = "Rotate the back side counterclockwise."

    elif letter == "R":
        sentence = "Rotate the right side clockwise."

    elif letter == "R'":
        sentence = "Rotate the right side counterclockwise."

    elif letter == "L":
        sentence = "Rotate the left side clockwise."

    elif letter == "L'":
        sentence = "Rotate the left side counterclockwise."

    elif letter == "U":
        sentence = "Rotate the up side clockwise."

    elif letter == "U'":
        sentence = "Rotate the up side counterclockwise."

    elif letter == "D":
        sentence = "Rotate the down side clockwise."

    elif letter == "D'":
        sentence = "Rotate the down side counterclockwise."

    return sentence


def set_prev_and_next_label(prev_label, next_label, direction, optimized_array, start_idx):
    """
    Updates the prev_label and next_label based on the start_index.
    """

    # If the cube is in its starting configuration
    if start_idx[0] < 0 or (start_idx[0] == 0 and direction == -1):
        prev_label.configure(text="There is no previous step.")
        next_prompt = create_sentence(optimized_array[0])
        next_label.configure(text=next_prompt)

    # if the cube is solved
    elif start_idx[0] >= len(optimized_array)-1:
        next_label.configure(text="Your cube is solved. There is no next step.")
        prev_prompt = create_sentence(optimized_array[len(optimized_array)-1])
        prev_label.configure(text=prev_prompt)

    # if a valid previous step operation is performed
    elif len(optimized_array) > start_idx[0] > 0 and direction == -1:
        next_prompt = create_sentence(optimized_array[start_idx[0]])
        prev_prompt = create_sentence(optimized_array[start_idx[0]-1])
        next_label.configure(text=next_prompt)
        prev_label.configure(text=prev_prompt)

    # if a valid next step operation is performed
    elif len(optimized_array) > start_idx[0] >= 0 and direction == 1:
        next_prompt = create_sentence(optimized_array[start_idx[0]+1])
        prev_prompt = create_sentence(optimized_array[start_idx[0]])
        next_label.configure(text=next_prompt)
        prev_label.configure(text=prev_prompt)




