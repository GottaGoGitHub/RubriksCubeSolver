from Solver import *

def optimize_solver(rotations):
    print("hallo")
    
    # changing for example R R R to R' etc.
    # for doing 2 less steps for each 

    i = len(rotations) - 1

    # we iterate from the end of the array to the begin of the array
    # because the length of the array decreases in every step we change
    # for example R R R to R'
    # so we do not have a fixed length 

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

    # TODO:
    # delete for example R R' from the array 
    # (R R' is not nessessary, because it happens nothing)





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


# TODO: optimize algorithm for the robot, so that the whole cube
# is not rotated anymore

def optimize_for_robot(rotations):
    print("hi")