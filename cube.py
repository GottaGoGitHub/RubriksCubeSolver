class RubriksCube:
    def __init__(self):
        self.cube = [
        ['y', 'y', 'y',
         'y', 'y', 'y',
         'y', 'y', 'y'],
        ['r', 'r', 'r',
         'r', 'r', 'r',
         'r', 'r', 'r'],
        ['g', 'g', 'g',
         'g', 'g', 'g',
         'g', 'g', 'g'],
        ['o', 'o', 'o',
         'o', 'o', 'o',
         'o', 'o', 'o'],
        ['b', 'b', 'b',
         'b', 'b', 'b',
         'b', 'b', 'b'],
        ['w', 'w', 'w',
         'w', 'w', 'w',
         'w', 'w', 'w']]

    def print_cube(self):
        for e in self.cube:
            print(e)
            print()

    def rotate_front(self):
        fronttemp0 = self.cube[1][0]
        fronttemp1 = self.cube[1][1]
        fronttemp2 = self.cube[1][2]
        fronttemp3 = self.cube[1][3]
        fronttemp4 = self.cube[1][4]
        fronttemp5 = self.cube[1][5]
        fronttemp6 = self.cube[1][6]
        fronttemp7 = self.cube[1][7]
        fronttemp8 = self.cube[1][8]
        self.cube[1][0] = fronttemp6
        self.cube[1][1] = fronttemp3
        self.cube[1][2] = fronttemp0
        self.cube[1][3] = fronttemp7
        self.cube[1][4] = fronttemp4
        self.cube[1][5] = fronttemp1
        self.cube[1][6] = fronttemp8
        self.cube[1][7] = fronttemp5
        self.cube[1][8] = fronttemp2
        obentemp1 = self.cube[0][6]
        obentemp2 = self.cube[0][7]
        obentemp3 = self.cube[0][8]
        rechtstemp1 = self.cube[2][0]
        rechtstemp2 = self.cube[2][3]
        rechtstemp3 = self.cube[2][6]
        untentemp1 = self.cube[5][0]
        untentemp2 = self.cube[5][1]
        untentemp3 = self.cube[5][2]
        linkstemp1 = self.cube[4][2]
        linkstemp2 = self.cube[4][5]
        linkstemp3 = self.cube[4][8]
        self.cube[0][6] = linkstemp3
        self.cube[0][7] = linkstemp2
        self.cube[0][8] = linkstemp1
        self.cube[2][0] = obentemp1
        self.cube[2][3] = obentemp2
        self.cube[2][6] = obentemp3
        self.cube[5][0] = rechtstemp3
        self.cube[5][1] = rechtstemp2
        self.cube[5][2] = rechtstemp1
        self.cube[4][2] = untentemp1
        self.cube[4][5] = untentemp2
        self.cube[4][8] = untentemp3

    def rotate_cube_right(self):
        fronttemp = self.cube[1]
        righttemp = self.cube[2]
        backtemp = self.cube[3]
        lefttemp = self.cube[4]
        uptemp0 = self.cube[0][0]
        uptemp1 = self.cube[0][1]
        uptemp2 = self.cube[0][2]
        uptemp3 = self.cube[0][3]
        uptemp4 = self.cube[0][4]
        uptemp5 = self.cube[0][5]
        uptemp6 = self.cube[0][6]
        uptemp7 = self.cube[0][7]
        uptemp8 = self.cube[0][8]
        downtemp0 = self.cube[5][0]
        downtemp1 = self.cube[5][1]
        downtemp2 = self.cube[5][2]
        downtemp3 = self.cube[5][3]
        downtemp4 = self.cube[5][4]
        downtemp5 = self.cube[5][5]
        downtemp6 = self.cube[5][6]
        downtemp7 = self.cube[5][7]
        downtemp8 = self.cube[5][8]
        self.cube[2] = fronttemp
        self.cube[3] = righttemp
        self.cube[4] = backtemp
        self.cube[1] = lefttemp
        self.cube[0][0] = uptemp2
        self.cube[0][1] = uptemp5
        self.cube[0][2] = uptemp8
        self.cube[0][3] = uptemp1
        self.cube[0][4] = uptemp4
        self.cube[0][5] = uptemp7
        self.cube[0][6] = uptemp0
        self.cube[0][7] = uptemp3
        self.cube[0][8] = uptemp6
        self.cube[5][0] = downtemp6
        self.cube[5][1] = downtemp3
        self.cube[5][2] = downtemp0
        self.cube[5][3] = downtemp7
        self.cube[5][4] = downtemp4
        self.cube[5][5] = downtemp1
        self.cube[5][6] = downtemp8
        self.cube[5][7] = downtemp5
        self.cube[5][8] = downtemp2

    def rotate_cube_left(self):
        self.rotate_cube_right()
        self.rotate_cube_right()
        self.rotate_cube_right()

    def rotate_cube_up(self):
        uptemp = self.cube[0]
        fronttemp = self.cube[1]
        backtemp = self.cube[3]
        downtemp = self.cube[5]
        righttemp0 = self.cube[2][0]
        righttemp1 = self.cube[2][1]
        righttemp2 = self.cube[2][2]
        righttemp3 = self.cube[2][3]
        righttemp4 = self.cube[2][4]
        righttemp5 = self.cube[2][5]
        righttemp6 = self.cube[2][6]
        righttemp7 = self.cube[2][7]
        righttemp8 = self.cube[2][8]
        lefttemp0 = self.cube[4][0]
        lefttemp1 = self.cube[4][1]
        lefttemp2 = self.cube[4][2]
        lefttemp3 = self.cube[4][3]
        lefttemp4 = self.cube[4][4]
        lefttemp5 = self.cube[4][5]
        lefttemp6 = self.cube[4][6]
        lefttemp7 = self.cube[4][7]
        lefttemp8 = self.cube[4][8]
        self.cube[0] = fronttemp
        self.cube[1] = downtemp
        self.cube[5] = backtemp
        self.cube[3] = uptemp
        self.cube[2][0] = righttemp6
        self.cube[2][1] = righttemp3
        self.cube[2][2] = righttemp0
        self.cube[2][3] = righttemp7
        self.cube[2][4] = righttemp4
        self.cube[2][5] = righttemp1
        self.cube[2][6] = righttemp8
        self.cube[2][7] = righttemp5
        self.cube[2][8] = righttemp2
        self.cube[4][0] = lefttemp2
        self.cube[4][1] = lefttemp5
        self.cube[4][2] = lefttemp8
        self.cube[4][3] = lefttemp1
        self.cube[4][4] = lefttemp4
        self.cube[4][5] = lefttemp7
        self.cube[4][6] = lefttemp0
        self.cube[4][7] = lefttemp3
        self.cube[4][8] = lefttemp6

    def rotate_cube_down(self):
        self.rotate_cube_up()
        self.rotate_cube_up()
        self.rotate_cube_up()

    def rotate_front_prime(self):
        self.rotate_front()
        self.rotate_front()
        self.rotate_front()

    def rotate_right(self):
        self.rotate_cube_left()
        self.rotate_front()
        self.rotate_cube_right()

    def rotate_right_prime(self):
        self.rotate_cube_left()
        self.rotate_front_prime()
        self.rotate_cube_right()

    def rotate_left(self):
        self.rotate_cube_right()
        self.rotate_front()
        self.rotate_cube_left()

    def rotate_left_prime(self):
        self.rotate_cube_right()
        self.rotate_front_prime()
        self.rotate_cube_left()

    def rotate_back(self):
        self.rotate_cube_right()
        self.rotate_cube_right()
        self.rotate_front()
        self.rotate_cube_right()
        self.rotate_cube_right()

    def rotate_back_prime(self):
        self.rotate_cube_right()
        self.rotate_cube_right()
        self.rotate_front_prime()
        self.rotate_cube_right()
        self.rotate_cube_right()

    def rotate_up(self):
        self.rotate_cube_down()
        self.rotate_front()
        self.rotate_cube_up()

    def rotate_up_prime(self):
        self.rotate_cube_down()
        self.rotate_front_prime()
        self.rotate_cube_up()

    def rotate_down(self):
        self.rotate_cube_up()
        self.rotate_front()
        self.rotate_cube_down()

    def rotate_down_prime(self):
        self.rotate_cube_up()
        self.rotate_front_prime()
        self.rotate_cube_down()


def main():
    cube = RubriksCube()
    cube.print_cube()
    print()
    # cube.rotate_front()
    cube.rotate_right()
    cube.print_cube()


if __name__ == '__main__':
    main()
