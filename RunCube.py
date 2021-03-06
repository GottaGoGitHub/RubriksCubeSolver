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


# Setting a default value for the column and row size
for col in range(51):
    root.grid_columnconfigure(col, minsize=50)

for row in range(51):
    root.grid_rowconfigure(row, minsize=20)

# Creating font styles
text_font = Font(family="Times New Roman", size=10)
text_font_bold = Font(family="Times New Roman", size=10, weight="bold")

hint_font = Font(family="Times New Roman", size=15)
hint_font_bold = Font(family="Times New Roman", size=15, weight="bold")


# window defines the canvas on which the cubes will be drawn
window = Canvas(root, width=1000, height=500, bg="grey")
window.grid(row=5, column=0, columnspan=11, rowspan=11, sticky=W+E, padx=(5, 0))

# Creation of the unsolved cube
cube = create_cube_hexomino(window, 45, 199)
cubies_list = create_cubie_list_from_csv("Files_Import/DEFAULT.csv")
cubies_id = get_id_from_cubies(cubies_list)
cubies_colors = get_colors_from_cubies(cubies_list)
set_colors(window, cubies_colors, cube)


# Creation of a second cube, which is treated as solved
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


# Variable to switch between solved and unsolved cube
which_cube = [1]


# Binding the ENTER Key as event to the Entries "answer1" and "answer2"
# the "event" parameter is not used but expected for calls which are bound to keys
def press_enter(event):
    """
    When bound to a key it's going to call the evaluate_input function.
    """
    if which_cube[0] == 1:
        evaluate_input(window, answer1, answer2, cube, cubies_list)
    if which_cube[0] == 2:
        evaluate_input(window, answer1, answer2, solved_cube, solved_cubies_list)


answer1.bind("<Return>", press_enter)
answer2.bind("<Return>", press_enter)


# Creating the Rotation buttons
def rotate_up_for_button():
    """
    Wrapper function to rotate the cube upwards. (supposed to be bound to a button)
    """
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
    """
    Wrapper function to rotate the cube downwards. (supposed to be bound to a button)
    """
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
    """
    Wrapper function to rotate the cube to the left side. (supposed to be bound to a button)
    """
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
    """
    Wrapper function to rotate the cube to the right side. (supposed to be bound to a button)
    """
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
    """
      Wrapper function to rotate the cube upwards. (supposed to be bound to a key)
    """
    if which_cube[0] == 1:
        rotate_cube_up_cubies(cubies_list, cubies_id, rotations)
        set_colors(window, get_colors_from_cubies(cubies_list), cube)
    if which_cube[0] == 2:
        rotate_cube_up_cubies(solved_cubies_list, solved_cubies_id, solved_rotations)
        set_colors(window, get_colors_from_cubies(solved_cubies_list), solved_cube)


root.bind('<Up>', rotate_up_for_key)


def rotate_down_for_key(event):
    """
      Wrapper function to rotate the cube downwards. (supposed to be bound to a key)
    """
    if which_cube[0] == 1:
        rotate_cube_down_cubies(cubies_list, cubies_id, rotations)
        set_colors(window, get_colors_from_cubies(cubies_list), cube)
    if which_cube[0] == 2:
        rotate_cube_down_cubies(solved_cubies_list, solved_cubies_id, solved_rotations)
        set_colors(window, get_colors_from_cubies(solved_cubies_list), solved_cube)


root.bind('<Down>', rotate_down_for_key)


def rotate_left_for_key(event):
    """
      Wrapper function to rotate the cube to the left side. (supposed to be bound to a key)
    """
    if which_cube[0] == 1:
        rotate_cube_left_cubies(cubies_list, cubies_id, rotations)
        set_colors(window, get_colors_from_cubies(cubies_list), cube)
    if which_cube[0] == 2:
        rotate_cube_left_cubies(solved_cubies_list, solved_cubies_id, solved_rotations)
        set_colors(window, get_colors_from_cubies(solved_cubies_list), solved_cube)


root.bind('<Left>', rotate_left_for_key)


def rotate_right_for_key(event):
    """
      Wrapper function to rotate the cube to the right side. (supposed to be bound to a key)
    """
    if which_cube[0] == 1:
        rotate_cube_right_cubies(cubies_list, cubies_id, rotations)
        set_colors(window, get_colors_from_cubies(cubies_list), cube)
    if which_cube[0] == 2:
        rotate_cube_right_cubies(solved_cubies_list, solved_cubies_id, solved_rotations)
        set_colors(window, get_colors_from_cubies(solved_cubies_list), solved_cube)


root.bind('<Right>', rotate_right_for_key)


# Import and export of the cube
# Entry widgets to get the user specified input filename
import_filepath = Entry(root)
import_filepath.insert(END, "Filename")     # Default text
import_filepath.configure(width=20)
import_filepath.grid(row=18, column=1, padx=(5, 0))


def button_import_func(list_of_cubies, solved_list_of_cubies, rotation_list):
    """
    Gets the userinput of the previously created Entry widget and imports the file.
    """

    file = import_filepath.get()

    # The expected file format is ".csv"
    if file[-4:] != ".csv":
        file = "Files_Import/" + file + ".csv"
    else:
        file = "Files_Import/" + file

    # Calling the import function for the different cubes
    if which_cube[0] == 1:
        import_cube_from_csv(list_of_cubies, file)
        set_colors(window, get_colors_from_cubies(list_of_cubies), cube)
    if which_cube[0] == 2:
        import_cube_from_csv(solved_list_of_cubies, file)
        set_colors(window, get_colors_from_cubies(solved_list_of_cubies), solved_cube)

    # Disabling the buttons
    button_rotations_export_to_file.configure(state=DISABLED)
    solve_optimize_button.configure(state=DISABLED)
    previous_step_button.configure(state=DISABLED)
    next_step_button.configure(state=DISABLED)
    reset_button.configure(state=DISABLED)
    set_prev_and_next_label(previous_text_label, next_text_label, 1, rotation_list, start_idx=[-1])


# Setting up the button
button_import = Button(root, text="Import", command=lambda: button_import_func(cubies_list, solved_cubies_list,
                                                                               rotations))
button_import.configure(width=12)
button_import.grid(row=18, column=0, padx=(5, 0))

# Entry widgets to get the user specified export filename
export_filepath = Entry(root)
export_filepath.insert(END, "Filename")
export_filepath.configure(width=20)
export_filepath.grid(row=19, column=1, padx=(5, 0))


def button_export_func():
    """
    Gets the userinput of the previously created Entry widget and exports the cube to the named file.
    """

    file = export_filepath.get()

    # The expected file format is ".csv"
    if file[-4:] != ".csv":
        file = "Files_Export/" + file + ".csv"
    else:
        file = "Files_Export/" + file

    # Calling the import function for the different cubes
    if which_cube[0] == 1:
        export_cube_to_csv(cubies_list, file)
    if which_cube[0] == 2:
        export_cube_to_csv(solved_cubies_list, file)


# Setting up the button
button_export = Button(root, text="Export", command=button_export_func)
button_export.configure(width=12)
button_export.grid(row=19, column=0)

# Entry widgets to get the user specified filename to export the rotations
rotations_filepath = Entry(root)
rotations_filepath.insert(END, "Filename")
rotations_filepath.configure(width=20)
rotations_filepath.grid(row=20, column=1, padx=(5, 0))


def export_rotations_to_file(rotations_, error_):
    """
    Gets the userinput of the previously created Entry widget and exports the rotations to the file.
    """

    if not error_[0]:
        file = rotations_filepath.get()

        # The expected file format is ".txt"
        if file[-4:] != ".txt":
            file = "Files_Export/" + file + ".txt"
        else:
            file = "Files_Export/" + file

        # writing the rotations to the file.
        filehandler = open(file, "w")
        filehandler.write(str(rotations_))
        filehandler.close()


# Setting up the button
button_rotations_export_to_file = Button(root, text="Export Rotations",
                                         command=lambda: export_rotations_to_file(rotations, error))
button_rotations_export_to_file.configure(width=12, state=DISABLED)
button_rotations_export_to_file.grid(row=20, column=0)

# ____________________________________________________________________________________________________________________________________________________________________
error = [False]     # Error variable which is used to keep track whether an error occurred
lauf_idx = [0]      # Index which is used to step through the rotations


def orientate_cube(rotation_list, list_of_cubies):
    """
    Asserts the correct orientation of the cube.
    """
    if not(cubies_id[0][4] == "0501" and cubies_id[1][4] == "1601" and cubies_id[4][4] == "1101" ):
        if not cubies_id[1][4] == "1601":
            for _ in range(3):
                rotate_cube_right_cubies(list_of_cubies, cubies_id, rotation_list)
                if cubies_id[1][4] == "1601":
                    break

            if not cubies_id[1][4] == "1601":
                for _ in range(3):
                    rotate_cube_up_cubies(list_of_cubies, cubies_id, rotation_list)
                    if cubies_id[1][4] == "1601":
                        break

        if cubies_id[0][4] == "2601":
            rotate_cube_right_cubies(list_of_cubies, cubies_id, rotation_list)
            rotate_cube_right_cubies(list_of_cubies, cubies_id, rotation_list)
            rotate_cube_up_cubies(list_of_cubies, cubies_id, rotation_list)
            rotate_cube_up_cubies(list_of_cubies, cubies_id, rotation_list)

        if cubies_id[4][4] == "0501":
            rotate_cube_down_cubies(list_of_cubies, cubies_id, rotation_list)
            rotate_cube_right_cubies(list_of_cubies, cubies_id, rotation_list)
            rotate_cube_up_cubies(list_of_cubies, cubies_id, rotation_list)

        if cubies_id[4][4] == "2601":
            rotate_cube_down_cubies(list_of_cubies, cubies_id, rotation_list)
            rotate_cube_left_cubies(list_of_cubies, cubies_id, rotation_list)
            rotate_cube_up_cubies(list_of_cubies, cubies_id, rotation_list)

        set_colors(window, get_colors_from_cubies(list_of_cubies), cube)
        rotation_list.clear()


def solve_optimize_func(rotation_list, list_of_cubies, temp_error, window_, cube_, start_idx):
    """
    Wrapper function which calls the solve function to run the solving algorithm and optimizes the rotations afterwards.
    """
    orientate_cube(rotation_list, list_of_cubies)

    # Clearing the rotations (necessary when multiple cubes will be solved in one session)
    rotation_list.clear()
    # Resetting the index
    start_idx[0] = 0
    # Calling the solving algorithm
    solve_cube(list_of_cubies, cubies_id, rotation_list, temp_error, window_, cube_)
    # If no error occured while solving
    if not temp_error[0]:
        # optimize the rotations
        optimize_solver(rotation_list)
        # actualizing the labels which show the next and previous rotation
        set_prev_and_next_label(previous_text_label, next_text_label, 1, rotation_list, start_idx=[-1])
        # State management of the Buttons
        next_step_button.configure(state=NORMAL)
        reset_button.configure(state=NORMAL)
        button_rotations_export_to_file.configure(state=NORMAL)
        # If the user enters a solved cube
        if len(rotation_list) == 0:
            next_text_label.configure(text="Your cube is already solved.")
            next_step_button.configure(state=DISABLED)

    # Disabling buttons if an error occured
    if temp_error[0]:
        solve_optimize_button.configure(state=DISABLED)
        button_rotations_export_to_file.configure(state=DISABLED)

    button_rotate_left.configure(state=DISABLED)
    button_rotate_right.configure(state=DISABLED)
    button_rotate_up.configure(state=DISABLED)
    button_rotate_down.configure(state=DISABLED)
    scramble_button.configure(state=DISABLED)


# Setting up the button which calls the solving function
solve_optimize_button = Button(root, text="Generate Solution",
                               command=lambda: solve_optimize_func(rotations, cubies_list, error, window, cube, lauf_idx))
solve_optimize_button.configure(width=12, state=DISABLED)
solve_optimize_button.grid(row=18, column=4, columnspan=2)


def submit(list_of_cubies, list_of_solved_cubies, list_of_cubies_ids, rotation_list, error_):
    """
    Compares the cubies of the unsolved with the solved cube and actualizes the id_array and the cubies
    based on matching colors.
    """

    error_[0] = False

    # Assert that the cube is correctly orientated
    orientate_cube(rotation_list, list_of_cubies)

    list_of_colors = get_colors_from_cubies(list_of_cubies)
    # Assert that the cube is complete
    for side in list_of_colors:
        if "grey" in side:
            error_[0] = True

    if error_[0]:
        messagebox.showerror("Incomplete cube", "Please color the whole cube.")

    if not error_[0]:
        # Creating autosave files which are needet to reset the cube to the start if an error occurs
        export_cube_to_csv(list_of_cubies, "Files_Export/AUTOSAVE/AUTOSAVE.csv")
        export_cube_to_csv(list_of_cubies, "Files_Export/AUTOSAVE/AUTOSAVE_START.csv")
        # Getting the colors of the cubies
        cubies_colors2 = get_colors_from_cubies(list_of_cubies)
        # Actualizing the id_array based on the colors.
        actualize_id_array(list_of_cubies, solved_cubies_list, cubies_id, cubies_colors2, error_)
        # Correcting the unsolved cubies based on the id_array and the solved cubies.
        correct_cubies_list(list_of_cubies_ids, list_of_cubies, list_of_solved_cubies, error_)
        # Getting the actualized colors (may have turned grey)
        list_of_colors = get_colors_from_cubies(list_of_cubies)

        # Actualizing the colors list
        for i, item in enumerate(list_of_colors):
            cubies_colors[i] = item

        # Coloring the GUI
        set_colors(window, get_colors_from_cubies(list_of_cubies), cube)

        # enabling the buttons
        if solve_optimize_button["state"] == "disabled":
            solve_optimize_button.configure(state=NORMAL)

        if scramble_button["state"] == "disabled":
            scramble_button.configure(state=NORMAL)

        next_step_button.configure(state=DISABLED)
        previous_step_button.configure(state=DISABLED)
        reset_button.configure(state=DISABLED)


# Setting up the submit button
submit_button = Button(root, text="Submit Input", command=lambda: submit(cubies_list, solved_cubies_list,
                                                                         cubies_id, rotations, error))
submit_button.configure(width=12)
submit_button.grid(row=2, column=5)


def scramble_func():
    """
    Wrapper function to scramble the cube and coloring the GUI accordingly afterwards
    """

    scramble(cubies_list, cubies_id, scramble_rotations)
    set_colors(window, get_colors_from_cubies(cubies_list), cube)


# Setting up the scramble button
scramble_button = Button(root, text="Scramble", command=scramble_func)
scramble_button.configure(width=5, state=DISABLED)
scramble_button.grid(row=23, column=9)

# Setting up the previous labels
previous_label = Label(root, font=hint_font_bold, text="Previous step:")
previous_text_label = Label(root, font=hint_font, text="There is no previous step.")

# Setting up the next labels
next_label = Label(root, font=hint_font_bold, text="Next step:")
next_text_label = Label(root, font=hint_font, text="You have to generate a solution first to see the correct steps.")

# Grid alignment
previous_label.grid(row=6, column=12, sticky=W)
previous_text_label.grid(row=7, column=12, sticky=W)
next_label.grid(row=8, column=12, sticky=W)
next_text_label.grid(row=9, column=12, sticky=W)


def previous_step_func(start_idx):
    """
    Wrapper function to handle the previous step. (Supposed to be bound to a button)
    """

    # if the start index should be greater/equal to the length of the rotations lost
    # then the start_idy shall be set to the length
    if start_idx[0] >= len(rotations):
        start_idx[0] = len(rotations)

    # if the index is greater than 0, a valid previous operation can be performed
    if start_idx[0] > 0:
        # decreasing the index
        start_idx[0] -= 1
        # calling previous operation to handle the rotation
        previous_step(window, cubies_colors, cube, rotations, start_idx)
        # actualizing the lables
        set_prev_and_next_label(previous_text_label, next_text_label, -1, rotations, start_idx)

    # Disabling the button if there is no previous step
    if lauf_idx[0] <= 0:
        previous_step_button.configure(state=DISABLED)

    # activating the next button if the index is len(rotations)-1 because it was disabled when idx = len(rotations)
    if start_idx[0] == len(rotations)-1:
        next_step_button.configure(state=NORMAL)


# Setting up the previous button
previous_step_button = Button(root, text="previous", command=lambda: previous_step_func(lauf_idx))
previous_step_button.configure(width=12, state=DISABLED)
previous_step_button.grid(row=19, column=4, sticky=W+E)


def next_step_func(start_idx):
    """
    Wrapper function to handle the next step. (Supposed to be bound to a button)
    """

    # if the index is less than 0, the index has to be set to 0 to ensure a valid operation
    if start_idx[0] < 0:
        start_idx[0] = 0

    # if the index is smaller than the length of the roation list a next step operation can be performed
    if start_idx[0] < len(rotations):
        # calling next operation to handle the rotation
        next_step(window, cubies_colors, cube, rotations, start_idx)
        # actualizing the lables
        set_prev_and_next_label(previous_text_label, next_text_label, 1, rotations, start_idx)
        # increasing the index
        start_idx[0] += 1

    # Disabling the next button if there is no next step
    if start_idx[0] == len(rotations):
        next_step_button.configure(state=DISABLED)

    # if the previous button was disabled, enable it
    if previous_step_button["state"] == "disabled":
        previous_step_button.configure(state=NORMAL)


# Setting up the next button
next_step_button = Button(root, text="next", command=lambda: next_step_func(lauf_idx))
next_step_button.configure(width=12, state=DISABLED)
next_step_button.grid(row=19, column=5, sticky=W+E)


def set_which_cube_to_1(select_cube):
    """
    Auxiliary function to select the first cube.
    """
    select_cube[0] = 1


def set_which_cube_to_2(select_cube):
    """
    Auxiliary function to select the second cube.
    """
    select_cube[0] = 2


# Radiobuttons to select which cube shall be colored
cube1_button = Radiobutton(root, text="Cube to solve (left)", value=1, command=lambda: set_which_cube_to_1(which_cube))
cube2_button = Radiobutton(root, text="Solved Cube (right)", value=2, command=lambda: set_which_cube_to_2(which_cube))

# Select cube 1 per default
cube1_button.select()

# Grid management
cube1_button.grid(row=1, column=7)
cube2_button.grid(row=2, column=7)


def reset(list_of_cubies, start_idx, rotation_list):
    """
    Resetting the GUI to to the state where the input was submitted.
    """

    # importing the AUTOSAVE_START file which contains the necessary start information
    import_cube_from_csv(list_of_cubies, "Files_Export/AUTOSAVE/AUTOSAVE_START.csv")
    # Coloring the GUI accordingly
    set_colors(window, get_colors_from_cubies(list_of_cubies), cube)
    # resetting the index
    start_idx[0] = 0
    # getting colors to actualize the colors list
    list_of_colors = get_colors_from_cubies(list_of_cubies)

    # actualizing the colors list
    for i, item in enumerate(list_of_colors):
        cubies_colors[i] = item

    # resetting the labels
    set_prev_and_next_label(previous_text_label, next_text_label, 1, rotation_list, start_idx=[-1])
    previous_step_button.configure(state=DISABLED)


# Setting up the reset button
reset_button = Button(root, text="Reset", command=lambda: reset(cubies_list, lauf_idx, rotations))
reset_button.configure(width=12, state=DISABLED)
reset_button.grid(row=20, column=4, columnspan=2)


def reset_to_default(list_of_cubies, start_idx, prev_text, next_text):
    """
    Resetting the GUI to to the  default state.
    """

    # Importing the default values
    import_cube_from_csv(list_of_cubies, "Files_Import/DEFAULT.csv")
    # Setting the default colors
    set_colors(window, get_colors_from_cubies(list_of_cubies), cube)
    # resetting the index and color list
    start_idx[0] = 0
    list_of_colors = get_colors_from_cubies(list_of_cubies)

    for i, item in enumerate(list_of_colors):
        cubies_colors[i] = item

    # resetting the labels
    prev_text.configure(text="There is no previous step.")
    next_text.configure(text="You have to generate a solution first to see the correct steps.")

    button_rotate_left.configure(state=NORMAL)
    button_rotate_right.configure(state=NORMAL)
    button_rotate_up.configure(state=NORMAL)
    button_rotate_down.configure(state=NORMAL)
    scramble_button.configure(state=NORMAL)


# Setting up the default reset button
reset_to_default_button = Button(root, text="Reset to Default",
                                 command=lambda: reset_to_default(cubies_list, lauf_idx,
                                                                  previous_text_label, next_text_label))
reset_to_default_button.configure(width=12)
reset_to_default_button.grid(row=2, column=11)

root.mainloop()
