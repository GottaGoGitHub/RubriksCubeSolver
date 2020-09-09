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
root.geometry("1000x900")


# Setting font styles
text_font = Font(family="Times New Roman", size=10)
text_font_bold = Font(family="Times New Roman", size=10, weight="bold")


# window defines the canvas on which the hexomino will be drawn
window = Canvas(root, width=1000, height=500, bg="grey")
window.grid(row=5, column=0, columnspan=5, sticky=W)


# Creation of the cube
cube = create_cube_hexomino(window, 45, 199)
cubies_list = create_cubie_list_from_csv("IMPORT.csv")
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


# Binding the ENTER Key as event to the Entries "answer1" and "answer2"
def press_enter(event):
    evaluate_input(window, answer1, answer2, cube, cubies_list, error_label)


answer1.bind("<Return>", press_enter)
answer2.bind("<Return>", press_enter)


# Creating the Rotation buttons
def rotate_up_for_button():
    rotate_cube_up_cubies(cubies_list, cubies_id, rotations)
    set_colors(window, get_colors_from_cubies(cubies_list), cube)


button_rotate_up = Button(root, text="Up", command=rotate_up_for_button)
button_rotate_up.configure(width=5)
button_rotate_up.grid(row=6, column=2, sticky=S)


def rotate_down_for_button():
    rotate_cube_down_cubies(cubies_list, cubies_id, rotations)
    set_colors(window, get_colors_from_cubies(cubies_list), cube)


button_rotate_down = Button(root, text="Down", command=rotate_down_for_button)
button_rotate_down.configure(width=5)
button_rotate_down.grid(row=8, column=2, sticky=N)


def rotate_left_for_button():
    rotate_cube_left_cubies(cubies_list, cubies_id, rotations)
    set_colors(window, get_colors_from_cubies(cubies_list), cube)


button_rotate_left = Button(root, text="Left", command=rotate_left_for_button)
button_rotate_left.configure(width=5)
button_rotate_left.grid(row=7, column=1, sticky=E)


def rotate_right_for_button():
    rotate_cube_right_cubies(cubies_list, cubies_id, rotations)
    set_colors(window, get_colors_from_cubies(cubies_list), cube)


button_rotate_right = Button(root, text="Right", command=rotate_right_for_button)
button_rotate_right.configure(width=5)
button_rotate_right.grid(row=7, column=3, sticky=W)


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
    import_cube_from_csv(list_of_cubies, "IMPORT.csv")
    set_colors(window, get_colors_from_cubies(list_of_cubies), cube)


button_import = Button(root, text="Import", command=lambda: button_import_func(cubies_list))
button_import.configure(width=5)
button_import.grid(row=10, column=0, sticky=W)


def button_export_func():
    export_cube_to_csv(cubies_list, "EXPORT.csv")


button_export = Button(root, text="Export", command=button_export_func)
button_export.configure(width=5)
button_export.grid(row=10, column=0, sticky=E)

# actualize cubies_list
def actualize_cubies_list(list_of_cubies):
    cubies_colors2 = get_colors_from_cubies(list_of_cubies)
    list_of_cubies = actualize_id_array(solved_cubies_list, cubies_id, cubies_colors2)

    # print("cubies_id:")
    # print(cubies_id)

    # print("cubies_list:")
    # for i in list_of_cubies:
    #     print(i.__str__())

    return list_of_cubies

cubies_list = actualize_cubies_list(cubies_list)


# TEST BUTTON
def button_test_func():
    scramble(cubies_list, cubies_id, scramble_rotations)
    # print("scramble")
    # print(scramble_rotations)
    set_colors(window, get_colors_from_cubies(cubies_list), cube)


test_button = Button(root, text="Click Me!\n I wanna test something. \n I don't know what but it may work.", command=button_test_func)
test_button.grid(row=12, column=0)


def other_test():
    white_cross(cubies_list, cubies_id, rotations)
    set_colors(window, get_colors_from_cubies(cubies_list), cube)


other_test_button = Button(root, text="White Cross", command=other_test)
other_test_button.grid(row=12, column=1)


def corner_test():
    white_corners(cubies_list, cubies_id, rotations)
    set_colors(window, get_colors_from_cubies(cubies_list), cube)


corner_test_button = Button(root, text="White Corners", command=corner_test)
corner_test_button.grid(row=12, column=2)


def second_layer_test():
    second_layer(cubies_list, cubies_id, rotations)
    set_colors(window, get_colors_from_cubies(cubies_list), cube)


second_layer_test_button = Button(root, text="Second Layer", command=second_layer_test)
second_layer_test_button.grid(row=12, column=3)


def top_cross_test():
    top_cross(cubies_list, cubies_id, rotations)
    set_colors(window, get_colors_from_cubies(cubies_list), cube)


top_cross_test_button = Button(root, text="Top Cross", command=top_cross_test)
top_cross_test_button.grid(row=12, column=4)


def correct_top_cross_test():
    correct_top_cross(cubies_list, cubies_id, rotations)
    set_colors(window, get_colors_from_cubies(cubies_list), cube)


correct_top_cross_test_button = Button(root, text="Correct Top Cross", command=correct_top_cross_test)
correct_top_cross_test_button.grid(row=12, column=5)


def sort_corners_test():
    sort_corners(cubies_list, cubies_id, rotations)
    set_colors(window, get_colors_from_cubies(cubies_list), cube)


sort_corners_test_button = Button(root, text="Sort Corners", command=sort_corners_test)
sort_corners_test_button.grid(row=12, column=6)


def correct_corners_test():
    correct_corners(cubies_list, cubies_id, rotations)
    set_colors(window, get_colors_from_cubies(cubies_list), cube)


correct_corners_test_button = Button(root, text="Correct Corners", command=correct_corners_test)
correct_corners_test_button.grid(row=12, column=7)


def rotations_test():
    rotate_by_side_idx(cubies_list, cubies_id, 2, rotations)
    set_colors(window, get_colors_from_cubies(cubies_list), cube)
    print(rotations)


rotations_test_button = Button(root, text="Rotation Array", command=rotations_test)
rotations_test_button.grid(row=12, column=8)


def solve_cube_test():
    solve_cube(cubies_list, cubies_id, rotations)
    set_colors(window, get_colors_from_cubies(cubies_list), cube)
    print("solve")
    print(rotations)
    # optimize_solver(rotations)
    # print(rotations)


solve_cube_test_button = Button(root, text="Solve", command=solve_cube_test)
solve_cube_test_button.grid(row=13, column=2)


def optimize_solve_cube_test():
    optimize_solver(rotations)
    set_colors(window, get_colors_from_cubies(cubies_list), cube)
    print("optimize")
    print(rotations)


optimize_solve_cube_test_button = Button(root, text="Optimize", command=optimize_solve_cube_test)
optimize_solve_cube_test_button.grid(row=13, column=3)


def temp_test():
    test_function()
    set_colors(window, get_colors_from_cubies(cubies_list), cube)
    print("TEST")


temp_test_button = Button(root, text="TEST", command=temp_test)
temp_test_button.grid(row=13, column=4)


def loop_test():
    for i in range(1000):
        print(i + 1)
        button_test_func()
        solve_cube_test()
    set_colors(window, get_colors_from_cubies(cubies_list), cube)


lopp_test_button = Button(root, text="LOOP TEST", command=loop_test)
lopp_test_button.grid(row=15, column=4)


root.mainloop()
