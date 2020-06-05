from tkinter import *


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


# Creating the workspace

# root is the whole working space; it defines the properties of the popup
root = Tk()

root.title("Rubik's Cube - Hexomino")
root.geometry("510x610")

# window defines the canvas on which the hexomino will be drawn
window = Canvas(root, width=500, height=500, bg="grey")
window.grid(row=4, column=0)


# Creating each side as a list which contains 9 rectangles.
up = grid3x3(window, 150, 94)
left = grid3x3(window, 45, 199)
front = grid3x3(window, 150, 199)
right = grid3x3(window, 255, 199)
back = grid3x3(window, 360, 199)
under = grid3x3(window, 150, 304)


# Combining all the sides to one single iterable list
cube = [up, left, front, right, back, under]


# Coloring the the fixed cross of the cube.
window.itemconfigure(cube[0][4], fill='yellow')
window.itemconfigure(cube[1][4], fill='blue')
window.itemconfigure(cube[2][4], fill='red')
window.itemconfigure(cube[3][4], fill='green')
window.itemconfigure(cube[4][4], fill='orange')
window.itemconfigure(cube[5][4], fill='white')

# Generating the user prompt
grid_prompt = grid3x3(window, 380, 60)

# TESTING UNIT
question1 = Label(root, text="Which side do you want to modify?")
question1.grid(row=0, column=0)

answer1 = Entry(root)
answer1.configure(width=30)
answer1.grid(row=1, column=0)

question2 = Label(root, text="How do you want to color your pieces? Please enter the number followed by the color. ")
question2.grid(row=2, column=0)

answer2 = Entry(root)
answer2.configure(width=30)
answer2.grid(row=3, column=0)


def evaluate_input(enter):
    # This function shall be called in the two entries (answer1, answer2) and evaluates their input

    # Depending on the input of answer1 and answer2 the corresponding face and piece of the cube will be selected
    # and colored.

    string_of_answer1 = answer1.get()
    string_of_answer2 = answer2.get()

    # Converting the strings for a less difficult evaluation


    # Lower case
    string_of_answer1.lower()
    string_of_answer2.lower()

    # Removing white spaces
    string_of_answer1.strip()
    string_of_answer2.strip()

    # defining side_idx as index for the side of the cube and piece_idx for the piece
    # color is a string which represents the color
    side_idx = 0
    piece_idx = 0
    color = ""

    # Evaluation of the first answer
    if "u" == string_of_answer1:
        side_idx = 0

    if "l" == string_of_answer1:
        side_idx = 1

    if "f" == string_of_answer1:
        side_idx = 2

    if "r" == string_of_answer1:
        side_idx = 3

    if "b" == string_of_answer1:
        side_idx = 4

    if "d" == string_of_answer1:
        side_idx = 5

    # Coloring the piece
    window.itemconfigure(cube[side_idx][piece_idx], fill=color)

    # answer2.delete(0, END)


answer1.bind("<Return>", evaluate_input)
answer2.bind("<Return>", evaluate_input)
root.mainloop()
