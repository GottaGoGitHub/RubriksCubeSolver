class Cubie:

    def __init__(self, name, number, color1, pos1, color2="None", pos2=[-1, -1], color3="None", pos3=[-1, -1]):
        """
        A single cubie consists of one, two or three colored sides, each is given by a color and position.

        @name sets the name of the cubie, it is supposed to be a number according to the given numeration
        @number is the number of colored sides
        @colorX is the color as a string
        @posX list of two int values; corresponding to the position in the cube
        @idX unique ID, which shall be used in the array to find the corresponding cubie
        """
        self.name = name
        self.number = number
        self.color1 = color1
        self.pos1 = pos1
        self.id1 = name + '01'
        self.color2 = color2
        self.pos2 = pos2
        self.id2 = name + '02'
        self.color3 = color3
        self.pos3 = pos3
        self.id3 = name + '03'
