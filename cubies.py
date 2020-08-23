class Cubie:

    def __init__(self, name, number, color1, pos1, id1, color2, pos2, id2, color3, pos3, id3):
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
        self.id1 = id1
        self.color2 = color2
        self.pos2 = pos2
        self.id2 = id2
        self.color3 = color3
        self.pos3 = pos3
        self.id3 = id3
        self.colors = []

        if number == 1:
            self.colors.append(color1)

        if number == 2:
            self.colors.append(color1)
            self.colors.append(color2)

        if number == 3:
            self.colors.append(color1)
            self.colors.append(color2)
            self.colors.append(color3)

    def __str__(self):
        return{"name = {" + str(self.name) + "} "
               + " number = {" + str(self.number) + "} "
               + " color1 = {" + str(self.color1) + "} "
               + " pos1 = {" + str(self.pos1) + "} "
               + " id1 = {" + str(self.id1) + "} "
               + " color2 = {" + str(self.color2) + "} "
               + " pos2 = {" + str(self.pos2) + "} "
               + " id2 = {" + str(self.id2) + "} "
               + " color3 = {" + str(self.color3) + "} "
               + " pos3 = {" + str(self.pos3) + "} "
               + " id3 = {" + str(self.id3) + "} "
               + " colors = {" + str(self.colors) + "}"}
