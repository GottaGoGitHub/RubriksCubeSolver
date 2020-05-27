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
        redtemp0 = self.cube[1][0]
        redtemp1 = self.cube[1][1]
        redtemp2 = self.cube[1][2]
        redtemp3 = self.cube[1][3]
        redtemp4 = self.cube[1][4]
        redtemp5 = self.cube[1][5]
        redtemp6 = self.cube[1][6]
        redtemp7 = self.cube[1][7]
        redtemp8 = self.cube[1][8]
        self.cube[1][0] = redtemp6
        self.cube[1][1] = redtemp3
        self.cube[1][2] = redtemp0
        self.cube[1][3] = redtemp7
        self.cube[1][4] = redtemp4
        self.cube[1][5] = redtemp1
        self.cube[1][6] = redtemp8
        self.cube[1][7] = redtemp5
        self.cube[1][8] = redtemp2
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


def main():
    cube = RubriksCube()
    cube.print_cube()
    print()
    cube.rotate_front()
    cube.print_cube()


if __name__ == '__main__':
    main()
