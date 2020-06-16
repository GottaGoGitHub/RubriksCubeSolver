from tkinter import *
from tkinter.font import Font
from Cube import *
from GUI import *

# Creating the workspace
# root is the whole working space; it defines the properties of the popup
root = Tk()

root.title("Rubik's Cube - Hexomino")
root.geometry("510x610")


# Setting font styles
text_font = Font(family="Times New Roman", size=10)
text_font_bold = Font(family="Times New Roman", size=10, weight="bold")


# window defines the canvas on which the hexomino will be drawn
window = Canvas(root, width=500, height=500, bg="grey")
window.grid(row=5, column=0)


# Creation of the cube
cube = create_cube_hexomino(window, 45, 199)


# Generating the prompt in the upper right hand corner.
gernerate_prompt(window, text_font, text_font_bold)

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
def press_enter(event):
    evaluate_input(window, answer1, answer2, cube)


answer1.bind("<Return>", press_enter)
answer2.bind("<Return>", press_enter)


#TEST
button_rotate = Button(root, text="Test Rotate", command=rotate_cube_up)
button_rotate.grid(row=6, column=0)

root.mainloop()
