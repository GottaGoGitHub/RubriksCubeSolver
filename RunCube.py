from tkinter import *
from tkinter.font import Font
from Cube import *
from GUI import *
from FileHandler import *
from Solver import *
from Optimize import *

# Creating the workspace
# root is the whole working space; it defines the properties of the popup
root = Tk()

root.title("Rubik's Cube - Hexomino")
root.geometry("1920x1080")

for col in range(51):
    root.grid_columnconfigure(col, minsize=50)

for row in range(51):
    root.grid_rowconfigure(row, minsize=20)

# Setting font styles
text_font = Font(family="Times New Roman", size=10)
text_font_bold = Font(family="Times New Roman", size=10, weight="bold")


# window defines the canvas on which the hexomino will be drawn
window = Canvas(root, width=1000, height=500, bg="grey")
window.grid(row=5, column=0, columnspan=11, padx=9)

# Creation of the cube
cube = create_cube_hexomino(window, 45, 199)
cubies_list = create_cubie_list_from_csv("IMPORT_EXAMPLE_2.csv")
cubies_id = get_id_from_cubies(cubies_list)
cubies_colors = get_colors_from_cubies(cubies_list)
set_colors(window, cubies_colors, cube)


# Creation of a second cube, which is supposed to be solved
solved_cube = create_cube_hexomino(window, 550, 199)
solved_cubies_list = create_cubie_list_from_csv("IMPORT.csv")
solved_cubies_id = get_id_from_cubies(solved_cubies_list)
solved_cubies_colors = get_colors_from_cubies(solved_cubies_list)
set_colors(window, solved_cubies_colors, solved_cube)

# initialize array for every step of rotation
scramble_rotations = []
rotations = [] 

# Generating the prompt in the upper right hand corner.
generate_prompt(window, text_font, text_font_bold)

# Creating the questions and input fields
question1 = Label(root,  font=text_font, text="Which side do you want to modify?")
question1.grid(row=0, column=0, columnspan=5)

answer1 = Entry(root)
answer1.configure(width=30)
answer1.grid(row=1, column=0, columnspan=5)

question2 = Label(root, font=text_font, text="How do you want to color your pieces? Please enter the number followed by the color. ")
question2.grid(row=2, column=0, columnspan=5)

answer2 = Entry(root)
answer2.configure(width=30)
answer2.grid(row=3, column=0, columnspan=5)

error_label = Label()

which_cube = [1]

# Binding the ENTER Key as event to the Entries "answer1" and "answer2"
def press_enter(event):
    if which_cube[0] == 1:
        evaluate_input(window, answer1, answer2, cube, cubies_list, error_label)
    if which_cube[0] == 2:
        evaluate_input(window, answer1, answer2, solved_cube, solved_cubies_list, error_label)


answer1.bind("<Return>", press_enter)
answer2.bind("<Return>", press_enter)


# Creating the Rotation buttons
def rotate_up_for_button():
    rotate_cube_up_cubies(cubies_list, cubies_id, rotations)
    set_colors(window, get_colors_from_cubies(cubies_list), cube)


button_rotate_up = Button(root, text="Up", command=rotate_up_for_button)
button_rotate_up.configure(width=5)
button_rotate_up.grid(row=7, column=9, sticky=W+E+N+S)


def rotate_down_for_button():
    rotate_cube_down_cubies(cubies_list, cubies_id, rotations)
    set_colors(window, get_colors_from_cubies(cubies_list), cube)


button_rotate_down = Button(root, text="Down", command=rotate_down_for_button)
button_rotate_down.configure(width=5)
button_rotate_down.grid(row=9, column=9, sticky=W+E+N+S)


def rotate_left_for_button():
    rotate_cube_left_cubies(cubies_list, cubies_id, rotations)
    set_colors(window, get_colors_from_cubies(cubies_list), cube)


button_rotate_left = Button(root, text="Left", command=rotate_left_for_button)
button_rotate_left.configure(width=5)
button_rotate_left.grid(row=8, column=8, sticky=W+E+N+S)


def rotate_right_for_button():
    rotate_cube_right_cubies(cubies_list, cubies_id, rotations)
    set_colors(window, get_colors_from_cubies(cubies_list), cube)


button_rotate_right = Button(root, text="Right", command=rotate_right_for_button)
button_rotate_right.configure(width=5)
# 3
button_rotate_right.grid(row=8, column=10, sticky=W+E+N+S, padx=(0, 9))


# Binding the arrow key to the corresponding rotation
def rotate_up_for_key(event):
    rotate_cube_up_cubies(cubies_list, cubies_id, rotations)
    set_colors(window, get_colors_from_cubies(cubies_list), cube)


root.bind('<Up>', rotate_up_for_key)


def rotate_down_for_key(event):
    rotate_cube_down_cubies(cubies_list, cubies_id, rotations)
    set_colors(window, get_colors_from_cubies(cubies_list), cube)


root.bind('<Down>', rotate_down_for_key)


def rotate_left_for_key(event):
    rotate_cube_left_cubies(cubies_list, cubies_id, rotations)
    set_colors(window, get_colors_from_cubies(cubies_list), cube)


root.bind('<Left>', rotate_left_for_key)


def rotate_right_for_key(event):
    rotate_cube_left_cubies(cubies_list, cubies_id, rotations)
    set_colors(window, get_colors_from_cubies(cubies_list), cube)


root.bind('<Right>', rotate_right_for_key)


# Import and export of the cube
def button_import_func(list_of_cubies):
    import_cube_from_csv(list_of_cubies, "IMPORT_EXAMPLE.csv")
    set_colors(window, get_colors_from_cubies(list_of_cubies), cube)


button_import = Button(root, text="Import", command=lambda: button_import_func(cubies_list))
button_import.configure(width=12)
button_import.grid(row=7, column=0, padx=(5, 0))


def button_export_func():
    export_cube_to_csv(cubies_list, "EXPORT.csv")


button_export = Button(root, text="Export", command=button_export_func)
button_export.configure(width=12)
button_export.grid(row=7, column=1)

#____________________________________________________________________________________________________________________________________________________________________


def submit(list_of_cubies):
    cubies_colors2 = get_colors_from_cubies(list_of_cubies)
    actualize_id_array(list_of_cubies, solved_cubies_list, cubies_id, cubies_colors2)

submit_button = Button(root, text="Submit Input", command=lambda: submit(cubies_list))
submit_button.configure(width=12)
submit_button.grid(row=2, column=5)


def scramble_func():
    scramble(cubies_list, cubies_id, scramble_rotations)
    set_colors(window, get_colors_from_cubies(cubies_list), cube)


scramble_button = Button(root, text="Scramble", command=scramble_func)
scramble_button.configure(width=12)
scramble_button.grid(row=9, column=0, padx=(5, 0))


# # TEST BUTTON
# def button_test_func():
#     scramble(cubies_list, cubies_id, scramble_rotations)
#     # print("scramble")
#     # print(scramble_rotations)
#     set_colors(window, get_colors_from_cubies(cubies_list), cube)


# test_button = Button(root, text="Click Me!\n I wanna test something. \n I don't know what but it may work.", command=button_test_func)
# test_button.grid(row=12, column=0)


# def other_test():
#     white_cross(cubies_list, cubies_id, rotations)
#     set_colors(window, get_colors_from_cubies(cubies_list), cube)


# other_test_button = Button(root, text="White Cross", command=other_test)
# other_test_button.grid(row=12, column=1)


# def corner_test():
#     white_corners(cubies_list, cubies_id, rotations)
#     set_colors(window, get_colors_from_cubies(cubies_list), cube)


# corner_test_button = Button(root, text="White Corners", command=corner_test)
# corner_test_button.grid(row=12, column=2)


# def second_layer_test():
#     second_layer(cubies_list, cubies_id, rotations)
#     set_colors(window, get_colors_from_cubies(cubies_list), cube)


# second_layer_test_button = Button(root, text="Second Layer", command=second_layer_test)
# second_layer_test_button.grid(row=12, column=3)


# def top_cross_test():
#     top_cross(cubies_list, cubies_id, rotations)
#     set_colors(window, get_colors_from_cubies(cubies_list), cube)


# top_cross_test_button = Button(root, text="Top Cross", command=top_cross_test)
# top_cross_test_button.grid(row=12, column=4)


# def correct_top_cross_test():
#     correct_top_cross(cubies_list, cubies_id, rotations)
#     set_colors(window, get_colors_from_cubies(cubies_list), cube)


# correct_top_cross_test_button = Button(root, text="Correct Top Cross", command=correct_top_cross_test)
# correct_top_cross_test_button.grid(row=12, column=5)


# def sort_corners_test():
#     sort_corners(cubies_list, cubies_id, rotations)
#     set_colors(window, get_colors_from_cubies(cubies_list), cube)


# sort_corners_test_button = Button(root, text="Sort Corners", command=sort_corners_test)
# sort_corners_test_button.grid(row=12, column=6)


# def correct_corners_test():
#     correct_corners(cubies_list, cubies_id, rotations)
#     set_colors(window, get_colors_from_cubies(cubies_list), cube)


# correct_corners_test_button = Button(root, text="Correct Corners", command=correct_corners_test)
# correct_corners_test_button.grid(row=12, column=7)


# def rotations_test():
#     rotate_by_side_idx(cubies_list, cubies_id, 2, rotations)
#     set_colors(window, get_colors_from_cubies(cubies_list), cube)
#     print(rotations)


# rotations_test_button = Button(root, text="Rotation Array", command=rotations_test)
# rotations_test_button.grid(row=12, column=8)


def solve_optimize_func():
    solve_cube(cubies_list, cubies_id, rotations)
    optimize_solver(rotations)
    print(rotations)


solve_optimize_button = Button(root, text="Generate Solution", command=solve_optimize_func)
solve_optimize_button.configure(width=12)
solve_optimize_button.grid(row=7, column=4, columnspan=2)


lauf_idx = [0]

def previous_step_func(start_idx):
    print("previous_step")
    print(cubies_colors)
    print(rotations)

    if start_idx[0] >= len(rotations):
        start_idx[0] = len(rotations)

    if start_idx[0] > 0:
        start_idx[0] -= 1
        previous_step(window, cubies_colors, cube, rotations, start_idx)

    print(start_idx)


previous_step_button = Button(root, text="previous", command=lambda: previous_step_func(lauf_idx))
previous_step_button.configure(width=12)
previous_step_button.grid(row=8, column=4, sticky=W+E)


def next_step_func(start_idx):
    print("next_step")
    print(cubies_colors)
    print(rotations)

    if start_idx[0] < 0:
        start_idx[0] = 0

    if start_idx[0] < len(rotations):
        next_step(window, cubies_colors, cube, rotations, start_idx)
        start_idx[0] += 1

    print(start_idx)

next_step_button = Button(root, text="next", command=lambda: next_step_func(lauf_idx))
next_step_button.configure(width=12)
next_step_button.grid(row=8, column=5, sticky=W+E)


def solve_complete_func():
    print("solve complete")
    solve_cube(cubies_list, cubies_id, rotations)
    set_colors(window, get_colors_from_cubies(cubies_list), cube)

solve_complete_button = Button(root, text="solve complete", command=solve_complete_func)
solve_complete_button.configure(width=12)
solve_complete_button.grid(row=8, column=3)


def set_which_cube_to_1(select_cube):
    select_cube[0] = 1


def set_which_cube_to_2(select_cube):
    select_cube[0] = 2


# Radiobuttons to select which cube shall be colored
cube1_button = Radiobutton(root, text="Cube to solve (left)", value=1, command=lambda: set_which_cube_to_1(which_cube))
cube2_button = Radiobutton(root, text="Solved Cube (right)", value=2, command=lambda: set_which_cube_to_2(which_cube))

cube1_button.select()
cube1_button.grid(row=1, column=7)
cube2_button.grid(row=2, column=7)

# def optimize_solve_cube_test():
#     optimize_solver(rotations)
#     set_colors(window, get_colors_from_cubies(cubies_list), cube)
#     print("optimize")
#     print(rotations)


# optimize_solve_cube_test_button = Button(root, text="Optimize", command=optimize_solve_cube_test)
# optimize_solve_cube_test_button.grid(row=13, column=3)


# def temp_test():
#     test_function()
#     set_colors(window, get_colors_from_cubies(cubies_list), cube)
#     print("TEST")


# temp_test_button = Button(root, text="TEST", command=temp_test)
# temp_test_button.grid(row=13, column=4)


# def loop_test():
#     for i in range(1000):
#         print(i + 1)
#         button_test_func()
#         solve_cube_test()
#     set_colors(window, get_colors_from_cubies(cubies_list), cube)


# lopp_test_button = Button(root, text="LOOP TEST", command=loop_test)
# lopp_test_button.grid(row=15, column=4)


root.mainloop()
