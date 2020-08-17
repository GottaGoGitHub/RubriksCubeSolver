from Solver import *

def optimize_solver(rotations):
    print("hallo")
    
    i = len(rotations) - 1

    while (i != 2):
        if (rotations[i] == rotations[i - 1]) and (rotations[i - 1] == rotations[i - 2]):

            del rotations[i - 2]
            del rotations[i - 2] 
            
            if rotations[i - 2] == "x":
                rotations[i - 2] = "x'"

            elif rotations[i - 2] == "x'":
                rotations[i - 2] = "x"

            elif rotations[i - 2] == "y":
                rotations[i - 2] = "y'"

            elif rotations[i - 2] == "y'":
                rotations[i - 2] = "y"

            elif rotations[i - 2] == "F":
                rotations[i - 2] = "F'"

            elif rotations[i - 2] == "F'":
                rotations[i - 2] = "F"

            elif rotations[i - 2] == "B":
                rotations[i - 2] = "B'"

            elif rotations[i - 2] == "B'":
                rotations[i - 2] = "B"

            elif rotations[i - 2] == "R":
                rotations[i - 2] = "R'"

            elif rotations[i - 2] == "R'":
                rotations[i - 2] = "R"

            elif rotations[i - 2] == "L":
                rotations[i - 2] = "L'"

            elif rotations[i - 2] == "L'":
                rotations[i - 2] = "L"

            elif rotations[i - 2] == "U":
                rotations[i - 2] = "U'"

            elif rotations[i - 2] == "U'":
                rotations[i - 2] = "U"

            elif rotations[i - 2] == "D":
                rotations[i - 2] = "D'"

            elif rotations[i - 2] == "D'":
                rotations[i - 2] = "D"

        i = i - 1 
   

def test_function():
    temp = ["0", "1", "2", "3", "4", "5"]
    print(temp)

    i = len(temp) - 1
    print(i)

    i = i - 2
    print(i)

    del temp[i - 2]
    print(temp)

    del temp[i - 2]
    print(temp)

    temp[i - 2] = "8"
    print(temp)


def optimize_for_robot(rotations):
    print("hi")