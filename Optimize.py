from Solver import *


def optimize_solver(rotations):
    # changing for example R R R to R' etc.
    # for doing 2 less steps for each 

    print(rotations)

    j = len(rotations) - 1

    # we iterate from the end of the array to the begin of the array
    # because the length of the array decreases in every step we change

    # for example delete R R R R 

    while j != 2:
        if (rotations[j] == rotations[j - 1]) and (rotations[j - 1] == rotations[j - 2] and
                                                   rotations[j - 2] == rotations[j - 3]):
            del rotations[j - 3]
            del rotations[j - 3]
            del rotations[j - 3]
            del rotations[j - 3]

        j = j - 1

    i = len(rotations) - 1

    # for example R R R to R'

    while i != 1:
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

    k = len(rotations) - 1

    # for example delete R R'

    while k != 0:
        if ((rotations[k] == "x" and rotations[k - 1] == "x'") or
                (rotations[k] == "x'" and rotations[k - 1] == "x")):

            del rotations[k - 1]
            del rotations[k - 1]

        elif ((rotations[k] == "y" and rotations[k - 1] == "y'") or
              (rotations[k] == "y'" and rotations[k - 1] == "y")):

            del rotations[k - 1]
            del rotations[k - 1]

        elif ((rotations[k] == "F" and rotations[k - 1] == "F'") or
              (rotations[k] == "F'" and rotations[k - 1] == "F")):

            del rotations[k - 1]
            del rotations[k - 1]

        elif ((rotations[k] == "B" and rotations[k - 1] == "B'") or
              (rotations[k] == "B'" and rotations[k - 1] == "B")):

            del rotations[k - 1]
            del rotations[k - 1]

        elif ((rotations[k] == "R" and rotations[k - 1] == "R'") or
              (rotations[k] == "R'" and rotations[k - 1] == "R")):

            del rotations[k - 1]
            del rotations[k - 1]

        elif ((rotations[k] == "L" and rotations[k - 1] == "L'") or
              (rotations[k] == "L'" and rotations[k - 1] == "L")):

            del rotations[k - 1]
            del rotations[k - 1]

        elif ((rotations[k] == "U" and rotations[k - 1] == "U'") or
              (rotations[k] == "U'" and rotations[k - 1] == "U")):

            del rotations[k - 1]
            del rotations[k - 1]

        elif ((rotations[k] == "D" and rotations[k - 1] == "D'") or
              (rotations[k] == "D'" and rotations[k - 1] == "D")):

            del rotations[k - 1]
            del rotations[k - 1]

        k = k - 1