from cubies import *


def import_cube_from_csv(filepath):
    filehandler = open(filepath)

    content = filehandler.read()

    cubies = []

    rows = content.split('\n')
    for i in range(1, len(rows)-2):
        temp = rows[i].split(',')

        temp_cubie = Cubie(temp[0],
                           int(temp[1]),
                           temp[2],
                           [int(temp[3]), int(temp[4])],
                           temp[5],
                           temp[6],
                           [int(temp[7]), int(temp[8])],
                           temp[9],
                           temp[10],
                           [int(temp[11]), int(temp[12])],
                           temp[13])
        cubies.append(temp_cubie)
    return cubies
