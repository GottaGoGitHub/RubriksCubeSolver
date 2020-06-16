from tkinter import *
from tkinter.font import Font
from Cube import *


def rectangle(canvas, x1, x2, y1, y2):
    rect = canvas.create_rectangle(x1, x2, y1, y2)
    return rect


def grid3x3(canvas, origin_x, origin_y):
    """
    Creates a 3x3 grid of uncolored squares with a black rim.

    ├───99px────┤

    ┌───┬───┬───┐  ┬
    │ 0 │ 1 │ 2 │  │
    ├───┼───┼───┤  │
    │ 3 │ 4 │ 5 │  99px
    ├───┼───┼───┤  │
    │ 6 │ 7 │ 8 │  │
    └───┴───┴───┘  ┴

    The Origin consists of a x and y coordinate and represents the upper left hand corner,
    from which the grid will be created. Every square will be 33x33px with a border width of 1px.

    """
    grid = [None] * 9
    y = origin_y
    x = origin_x

    for idx, item in enumerate(grid):
        if idx == 3 or idx == 6:
            y += 33
        if idx % 3 == 0:
            x = origin_x
        else:
            x += 33

        item = canvas.create_rectangle(x, y, x + 33, y + 33)
        grid[idx] = item
    return grid


def evaluate_input(enter):
    # This function shall be called in the two entries (answer1, answer2) and evaluates their input

    # Depending on the input of answer1 and answer2 the corresponding face and piece of the cube will be selected
    # and colored.

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

        # Error label for the invalid index
        error_label = Label()
        error_label.grid_forget()

        # Evaluation of the first answer
        if "u" == list_of_answer1[0]:
            side_idx = 0

        if "l" == list_of_answer1[0]:
            side_idx = 1

        if "f" == list_of_answer1[0]:
            side_idx = 2

        if "r" == list_of_answer1[0]:
            side_idx = 3

        if "b" == list_of_answer1[0]:
            side_idx = 4

        if "d" == list_of_answer1[0]:
            side_idx = 5

        # Evaluation of the second answer

        # Which piece shall be chosen?
        if "0" == list_of_answer2[0]:
            piece_idx = 0

        if "1" == list_of_answer2[0]:
            piece_idx = 1

        if "2" == list_of_answer2[0]:
            piece_idx = 2

        if "3" == list_of_answer2[0]:
            piece_idx = 3

        if "4" == list_of_answer2[0]:
            error_label.configure(text="The index 4 is invalid. The cross of the cube can not be modified!", fg="red", state=NORMAL)
            error_label.grid(row=4, column=0)

        if "5" == list_of_answer2[0]:
            piece_idx = 5

        if "6" == list_of_answer2[0]:
            piece_idx = 6

        if "7" == list_of_answer2[0]:
            piece_idx = 7

        if "8" == list_of_answer2[0]:
            piece_idx = 8

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
            window.itemconfigure(cube[side_idx][piece_idx], fill=color)
            error_label.configure(state=DISABLED)

        # Deleting answer 2 for better user experience
        answer2.delete(0, END)


# Creating the workspace

# root is the whole working space; it defines the properties of the popup
root = Tk()

root.title("Rubik's Cube - Hexomino")
root.geometry("510x610")

# window defines the canvas on which the hexomino will be drawn
window = Canvas(root, width=500, height=500, bg="grey")
window.grid(row=5, column=0)

# Setting font styles
text_font = Font(family="Times New Roman", size=10)
text_font_bold = Font(family="Times New Roman", size=10, weight="bold")

# Creating each side as a list which contains 9 rectangles.
up = grid3x3(window, 150, 94)
left = grid3x3(window, 45, 199)
front = grid3x3(window, 150, 199)
right = grid3x3(window, 255, 199)
back = grid3x3(window, 360, 199)
under = grid3x3(window, 150, 304)

# Combining all the sides to one single iterable list
cube = [up, front, right, back, left, under]

# Coloring the the fixed cross of the cube.
window.itemconfigure(cube[0][4], fill='yellow')
window.itemconfigure(cube[1][4], fill='blue')
window.itemconfigure(cube[2][4], fill='red')
window.itemconfigure(cube[3][4], fill='green')
window.itemconfigure(cube[4][4], fill='orange')
window.itemconfigure(cube[5][4], fill='white')

# Coloring the cube.
for idx, item in enumerate(cube[0]):
    window.itemconfigure(cube[0][idx], fill='yellow')
for idx, item in enumerate(cube[1]):
    window.itemconfigure(cube[1][idx], fill='red')
for idx, item in enumerate(cube[2]):
    window.itemconfigure(cube[2][idx], fill='green')
for idx, item in enumerate(cube[3]):
    window.itemconfigure(cube[3][idx], fill='orange')
for idx, item in enumerate(cube[4]):
    window.itemconfigure(cube[4][idx], fill='blue')
for idx, item in enumerate(cube[5]):
    window.itemconfigure(cube[5][idx], fill='white')


def rotate():
    colors = get_colors(window, cube)
    colors = rotate_front(colors)

    for side_idx, side in enumerate(colors):
        for piece_idx, piece in enumerate(side):
            window.itemconfigure(cube[side_idx][piece_idx], fill=piece)


# Generating the user prompt
grid_prompt = grid3x3(window, 380, 65)
line_1 = window.create_text(188, 10, text="The faces of the cube can be accessed via: front, left, right, up, down")
line_2 = window.create_text(228, 25, text="To access the pieces, have a look for the numeration in the upper right hand corner.")
line_3 = window.create_text(196, 40, text="The following colors are allowed: orange, blue, red, white, green, yellow")
line_4 = window.create_text(218, 55, text="The input is not case sensitive and works also with just the first letter of a word.")

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
window.itemconfigure(line_1, font=text_font)
window.itemconfigure(line_2, font=text_font)
window.itemconfigure(line_3, font=text_font)
window.itemconfigure(line_4, font=text_font)
window.itemconfigure(text_0, font=text_font_bold)
window.itemconfigure(text_1, font=text_font_bold)
window.itemconfigure(text_2, font=text_font_bold)
window.itemconfigure(text_3, font=text_font_bold)
window.itemconfigure(text_5, font=text_font_bold)
window.itemconfigure(text_6, font=text_font_bold)
window.itemconfigure(text_7, font=text_font_bold)
window.itemconfigure(text_8, font=text_font_bold)


# Creating the questions and input fields
question1 = Label(root,  font=text_font, text="Which side do you want to modify?")
question1.grid(row=0, column=0)

answer1 = Entry(root)
answer1.configure(width=30)
answer1.grid(row=1, column=0)

question2 = Label(root, font=text_font, text="How do you want to color your pieces? Please enter the number followed by the color. ")
question2.grid(row=2, column=0)

answer2 = Entry(root)
answer2.configure(width=30)
answer2.grid(row=3, column=0)


# Binding the ENTER Key as event to the Entries "answer1" and "answer2"
answer1.bind("<Return>", evaluate_input)
answer2.bind("<Return>", evaluate_input)

#TEST
button_rotate = Button(root, text="Test Rotate", command=rotate)
button_rotate.grid(row=6, column=0)

root.mainloop()
