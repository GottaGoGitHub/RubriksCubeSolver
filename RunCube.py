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

hint_font = Font(family="Times New Roman", size=15)
hint_font_bold = Font(family="Times New Roman", size=15, weight="bold")


# window defines the canvas on which the hexomino will be drawn
window = Canvas(root, width=1000, height=500, bg="grey")
window.grid(row=5, column=0, columnspan=11, rowspan=11, sticky=W+E, padx=(5, 0))

# Creation of the cube
cube = create_cube_hexomino(window, 45, 199)
cubies_list = create_cubie_list_from_csv("Files_Import/IMPORT_EXAMPLE.csv")
cubies_id = get_id_from_cubies(cubies_list)
cubies_colors = get_colors_from_cubies(cubies_list)
set_colors(window, cubies_colors, cube)


# Creation of a second cube, which is supposed to be solved
solved_cube = create_cube_hexomino(window, 550, 199)
solved_cubies_list = create_cubie_list_from_csv("Files_Import/IMPORT.csv")
solved_cubies_id = get_id_from_cubies(solved_cubies_list)
solved_cubies_colors = get_colors_from_cubies(solved_cubies_list)
set_colors(window, solved_cubies_colors, solved_cube)

# initialize array for every step of rotation
scramble_rotations = []
rotations = [] 
solved_rotations = []

# Generating the prompt in the upper right hand corner.
generate_prompt(window, text_font, text_font_bold)

# Creating the questions and input fields
question1 = Label(root,  font=text_font, text="Which side do you want to modify?")
question1.grid(row=0, column=0, columnspan=5)

answer1 = Entry(root)
answer1.configure(width=30)
answer1.grid(row=1, column=0, columnspan=5)

question2 = Label(root, font=text_font,
                  text="How do you want to color your pieces? Please enter the number followed by the color. ")
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
    if which_cube[0] == 1:
        rotate_cube_up_cubies(cubies_list, cubies_id, rotations)
        set_colors(window, get_colors_from_cubies(cubies_list), cube)
    if which_cube[0] == 2:
        rotate_cube_up_cubies(solved_cubies_list, solved_cubies_id, solved_rotations)
        set_colors(window, get_colors_from_cubies(solved_cubies_list), solved_cube)

button_rotate_up = Button(root, text="Up", command=rotate_up_for_button)
button_rotate_up.configure(width=5)
button_rotate_up.grid(row=18, column=9, sticky=W+E+N+S)


def rotate_down_for_button():
    if which_cube[0] == 1:
        rotate_cube_down_cubies(cubies_list, cubies_id, rotations)
        set_colors(window, get_colors_from_cubies(cubies_list), cube)
    if which_cube[0] == 2:
        rotate_cube_down_cubies(solved_cubies_list, solved_cubies_id, solved_rotations)
        set_colors(window, get_colors_from_cubies(solved_cubies_list), solved_cube)


button_rotate_down = Button(root, text="Down", command=rotate_down_for_button)
button_rotate_down.configure(width=5)
button_rotate_down.grid(row=20, column=9, sticky=W+E+N+S)


def rotate_left_for_button():
    if which_cube[0] == 1:
        rotate_cube_left_cubies(cubies_list, cubies_id, rotations)
        set_colors(window, get_colors_from_cubies(cubies_list), cube)
    if which_cube[0] == 2:
        rotate_cube_left_cubies(solved_cubies_list, solved_cubies_id, solved_rotations)
        set_colors(window, get_colors_from_cubies(solved_cubies_list), solved_cube)


button_rotate_left = Button(root, text="Left", command=rotate_left_for_button)
button_rotate_left.configure(width=5)
button_rotate_left.grid(row=19, column=8, sticky=W+E+N+S)


def rotate_right_for_button():
    if which_cube[0] == 1:
        rotate_cube_right_cubies(cubies_list, cubies_id, rotations)
        set_colors(window, get_colors_from_cubies(cubies_list), cube)
    if which_cube[0] == 2:
        rotate_cube_right_cubies(solved_cubies_list, solved_cubies_id, solved_rotations)
        set_colors(window, get_colors_from_cubies(solved_cubies_list), solved_cube)


button_rotate_right = Button(root, text="Right", command=rotate_right_for_button)
button_rotate_right.configure(width=5)
# 3
button_rotate_right.grid(row=19, column=10, sticky=W+E+N+S)


# Binding the arrow key to the corresponding rotation
def rotate_up_for_key(event):
    if which_cube[0] == 1:
        rotate_cube_up_cubies(cubies_list, cubies_id, rotations)
        set_colors(window, get_colors_from_cubies(cubies_list), cube)
    if which_cube[0] == 2:
        rotate_cube_up_cubies(solved_cubies_list, solved_cubies_id, solved_rotations)
        set_colors(window, get_colors_from_cubies(solved_cubies_list), solved_cube)


root.bind('<Up>', rotate_up_for_key)


def rotate_down_for_key(event):
    if which_cube[0] == 1:
        rotate_cube_down_cubies(cubies_list, cubies_id, rotations)
        set_colors(window, get_colors_from_cubies(cubies_list), cube)
    if which_cube[0] == 2:
        rotate_cube_down_cubies(solved_cubies_list, solved_cubies_id, solved_rotations)
        set_colors(window, get_colors_from_cubies(solved_cubies_list), solved_cube)


root.bind('<Down>', rotate_down_for_key)


def rotate_left_for_key(event):
    if which_cube[0] == 1:
        rotate_cube_left_cubies(cubies_list, cubies_id, rotations)
        set_colors(window, get_colors_from_cubies(cubies_list), cube)
    if which_cube[0] == 2:
        rotate_cube_left_cubies(solved_cubies_list, solved_cubies_id, solved_rotations)
        set_colors(window, get_colors_from_cubies(solved_cubies_list), solved_cube)


root.bind('<Left>', rotate_left_for_key)


def rotate_right_for_key(event):
    if which_cube[0] == 1:
        rotate_cube_right_cubies(cubies_list, cubies_id, rotations)
        set_colors(window, get_colors_from_cubies(cubies_list), cube)
    if which_cube[0] == 2:
        rotate_cube_right_cubies(solved_cubies_list, solved_cubies_id, solved_rotations)
        set_colors(window, get_colors_from_cubies(solved_cubies_list), solved_cube)


root.bind('<Right>', rotate_right_for_key)


# Import and export of the cube
import_filepath = Entry(root)
import_filepath.insert(END, "Filename")
import_filepath.configure(width=20)
import_filepath.grid(row=18, column=1, padx=(5, 0))


def button_import_func(list_of_cubies, solved_list_of_cubies):
    file = import_filepath.get()

    if file[-4:] != ".csv":
        file = "Files_Import/" + file + ".csv"
    else:
        file = "Files_Import/" + file

    if which_cube[0] == 1:
        import_cube_from_csv(list_of_cubies, file)
        set_colors(window, get_colors_from_cubies(list_of_cubies), cube)
    if which_cube[0] == 2:
        import_cube_from_csv(solved_list_of_cubies, file)
        set_colors(window, get_colors_from_cubies(solved_list_of_cubies), solved_cube)


button_import = Button(root, text="Import", command=lambda: button_import_func(cubies_list, solved_cubies_list))
button_import.configure(width=12)
button_import.grid(row=18, column=0, padx=(5, 0))


export_filepath = Entry(root)
export_filepath.insert(END, "Filename")
export_filepath.configure(width=20)
export_filepath.grid(row=19, column=1, padx=(5, 0))


def button_export_func():
    file = export_filepath.get()

    if file[-4:] != ".csv":
        file = "Files_Export/" + file + ".txt"
    else:
        file = "Files_Export/" + file

    if which_cube[0] == 1:
        export_cube_to_csv(cubies_list, file)
    if which_cube[0] == 2:
        export_cube_to_csv(solved_cubies_list, file)


button_export = Button(root, text="Export", command=button_export_func)
button_export.configure(width=12)
button_export.grid(row=19, column=0)


rotations_filepath = Entry(root)
rotations_filepath.insert(END, "Filename")
rotations_filepath.configure(width=20)
rotations_filepath.grid(row=20, column=1, padx=(5, 0))


def export_rotations_to_file(rotations_, error_):
    if not error_[0]:
        file = rotations_filepath.get()

        if file[-4:] != ".txt":
            file = "Export_Output/" + file + ".txt"
        else:
            file = "Files_Export/" + file

        filehandler = open(file, "w")
        filehandler.write(str(rotations_))
        filehandler.close()


button_rotations_export_to_file = Button(root, text="Export Rotations",
                                         command=lambda: export_rotations_to_file(rotations, error))
button_rotations_export_to_file.configure(width=12, state=DISABLED)
button_rotations_export_to_file.grid(row=20, column=0)

# ____________________________________________________________________________________________________________________________________________________________________
# def actualize_color():
#     set_colors(window, get_colors_from_cubies(cubies_list), cube)


# color_button = Button(root, text="Colors", command=actualize_color)
# color_button.configure(width=12)
# color_button.grid(row=2, column=11)

error = [False]

lauf_idx = [0]


def solve_optimize_func(rotation_list, list_of_cubies, temp_error, window_, cube_, start_idx):
    rotation_list.clear()
    start_idx[0] = 0
    solve_cube(list_of_cubies, cubies_id, rotation_list, temp_error, window_, cube_)
    if not temp_error[0]:
        optimize_solver(rotation_list)
        set_prev_and_next_label(previous_text_label, next_text_label, 1, rotation_list, start_idx=[-1])
        next_step_button.configure(state=NORMAL)
        reset_button.configure(state=NORMAL)
        button_rotations_export_to_file.configure(state=NORMAL)
    if temp_error[0]:
        solve_optimize_button.configure(state=DISABLED)
        button_rotations_export_to_file.configure(state=DISABLED)


solve_optimize_button = Button(root, text="Generate Solution",
                               command=lambda: solve_optimize_func(rotations, cubies_list, error, window, cube, lauf_idx))
solve_optimize_button.configure(width=12, state=DISABLED)
solve_optimize_button.grid(row=18, column=4, columnspan=2)


def submit(list_of_cubies, list_of_solved_cubies, list_of_cubies_ids, error_):
    error_[0] = False
    export_cube_to_csv(list_of_cubies, "AUTOSAVE.csv")
    export_cube_to_csv(list_of_cubies, "AUTOSAVE_START.csv")
    cubies_colors2 = get_colors_from_cubies(list_of_cubies)
    actualize_id_array(list_of_cubies, solved_cubies_list, cubies_id, cubies_colors2, error_)
    correct_cubies_list(list_of_cubies_ids, list_of_cubies, list_of_solved_cubies, error_)
    list_of_colors = get_colors_from_cubies(list_of_cubies)

    for i, item in enumerate(list_of_colors):
        cubies_colors[i] = item

    set_colors(window, get_colors_from_cubies(list_of_cubies), cube)

    if solve_optimize_button["state"] == "disabled":
        solve_optimize_button.configure(state=NORMAL)

    if scramble_button["state"] == "disabled":
        scramble_button.configure(state=NORMAL)

    print(list_of_cubies[6].__str__())
    print(list_of_solved_cubies[6].__str__())
    print(list_of_cubies_ids)


submit_button = Button(root, text="Submit Input", command=lambda: submit(cubies_list, solved_cubies_list, cubies_id, error))
submit_button.configure(width=12)
submit_button.grid(row=2, column=5)


def scramble_func():
    scramble(cubies_list, cubies_id, scramble_rotations)
    set_colors(window, get_colors_from_cubies(cubies_list), cube)


scramble_button = Button(root, text="Scramble", command=scramble_func)
scramble_button.configure(width=5, state=DISABLED)
scramble_button.grid(row=23, column=9)


previous_label = Label(root, font=hint_font_bold, text="Previous step:")
previous_text_label = Label(root, font=hint_font, text="There is no previous step.")

next_label = Label(root, font=hint_font_bold, text="Next step:")
next_text_label = Label(root, font=hint_font, text="You have to generate a solution first to see the correct steps.")

previous_label.grid(row=6, column=12, sticky=W)
previous_text_label.grid(row=7, column=12, sticky=W)
next_label.grid(row=8, column=12, sticky=W)
next_text_label.grid(row=9, column=12, sticky=W)


def previous_step_func(start_idx):
    if start_idx[0] >= len(rotations):
        start_idx[0] = len(rotations)

    if start_idx[0] > 0:
        start_idx[0] -= 1
        previous_step(window, cubies_colors, cube, rotations, start_idx)
        set_prev_and_next_label(previous_text_label, next_text_label, -1, rotations, start_idx)

    # State management
    if lauf_idx[0] <= 0:
        previous_step_button.configure(state=DISABLED)

    if start_idx[0] == len(rotations)-1:
        next_step_button.configure(state=NORMAL)


previous_step_button = Button(root, text="previous", command=lambda: previous_step_func(lauf_idx))
previous_step_button.configure(width=12, state=DISABLED)
previous_step_button.grid(row=19, column=4, sticky=W+E)


def next_step_func(start_idx):

    if start_idx[0] < 0:
        start_idx[0] = 0

    if start_idx[0] < len(rotations):
        next_step(window, cubies_colors, cube, rotations, start_idx)
        set_prev_and_next_label(previous_text_label, next_text_label, 1, rotations, start_idx)
        start_idx[0] += 1

    if start_idx[0] == len(rotations):
        next_step_button.configure(state=DISABLED)

    if previous_step_button["state"] == "disabled":
        previous_step_button.configure(state=NORMAL)


next_step_button = Button(root, text="next", command=lambda: next_step_func(lauf_idx))
next_step_button.configure(width=12, state=DISABLED)
next_step_button.grid(row=19, column=5, sticky=W+E)


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


def reset(list_of_cubies, start_idx, rotation_list):
    import_cube_from_csv(list_of_cubies, "AUTOSAVE_START.csv")
    set_colors(window, get_colors_from_cubies(list_of_cubies), cube)
    start_idx[0] = 0
    list_of_colors = get_colors_from_cubies(list_of_cubies)

    for i, item in enumerate(list_of_colors):
        cubies_colors[i] = item

    set_prev_and_next_label(previous_text_label, next_text_label, 1, rotation_list, start_idx=[-1])
    previous_step_button.configure(state=DISABLED)


reset_button = Button(root, text="Reset", command=lambda: reset(cubies_list, lauf_idx, rotations))
reset_button.configure(width=12, state=DISABLED)
reset_button.grid(row=20, column=4, columnspan=2)


def reset_to_default(list_of_cubies, start_idx, prev_text, next_text):
    import_cube_from_csv(list_of_cubies, "DEFAULT.csv")
    set_colors(window, get_colors_from_cubies(list_of_cubies), cube)
    start_idx[0] = 0
    list_of_colors = get_colors_from_cubies(list_of_cubies)

    for i, item in enumerate(list_of_colors):
        cubies_colors[i] = item

    prev_text.configure(text="There is no previous step.")
    next_text.configure(text="You have to generate a solution first to see the correct steps.")


reset_to_default_button = Button(root, text="Reset to Default",
                                 command=lambda: reset_to_default(cubies_list, lauf_idx,
                                                                  previous_text_label, next_text_label))
reset_to_default_button.configure(width=12)
reset_to_default_button.grid(row=2, column=11)

root.mainloop()
