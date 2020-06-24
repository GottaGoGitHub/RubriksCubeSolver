filehandler = open('Cubies_table.csv')

content = filehandler.read()

cubes = []
cube_no = []
colors = []

rows = content.split('\n')

for i in range(len(rows)-1):
    cubes.append(rows[i+1].split(','))

for j in range(len(cubes)):
    cube_no.append(cubes[j][0])
    colors.append(cubes[j][1])

print(cube_no)
print(colors)
print(cubes[1])
