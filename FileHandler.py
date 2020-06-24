filehandler = open('Cubies_table.csv')

content = filehandler.read()

cubes = []

rows = content.split('\n')

for i in range(len(rows)-1):
    cubes.append(rows[i+1].split(','))

for j in range(len(cubes)):
    cubes_no = cubes[j][0]
    colors = cubes[j][1]

print(cubes)