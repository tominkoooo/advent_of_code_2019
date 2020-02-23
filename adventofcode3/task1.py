import matplotlib.pyplot as plt

def next_point(previous_point, operation):
    path = []
    if operation[0] == 'U':
        y = previous_point[1]
        for i in range(int(operation[1:])):
            y += 1
            path.append([previous_point[0], y])
        return path
    if operation[0] == 'D':
        y = previous_point[1]
        for i in range(int(operation[1:])):
            y -= 1
            path.append([previous_point[0], y])
        return path
    if operation[0] == 'L':
        x = previous_point[0]
        for i in range(int(operation[1:])):
            x -= 1
            path.append([x, previous_point[1]])
        return path
    if operation[0] == 'R':
        x = previous_point[0]
        for i in range(int(operation[1:])):
            x += 1
            path.append([x, previous_point[1]])
        return path

file = open("input.txt", "r")

data = file.readlines()

file.close()

first_wire = list(map(lambda x: x.strip("\n"), data[0].split(",")))
second_wire = list(map(lambda x: x.strip("\n"), data[1].split(",")))

first_points = [[0, 0]]
second_points = [[0, 0]]

for i in range(len(first_wire)):
    first_points += next_point(first_points[-1], first_wire[i])

for i in range(len(second_wire)):
    second_points += next_point(second_points[-1], second_wire[i])

common_points = []
for i in range(len(first_points)):
    print(i)
    if first_points[i] in second_points:
        common_points.append(first_points[i])

if [0, 0] in common_points:
    common_points.remove([0, 0])

file2 = open("common_points.txt", "w")
file2.write(str(common_points))
file2.close()

minimal_dist = min(list(map(lambda point: abs(point[0])+abs(point[1]), common_points)))
print(minimal_dist)

# fx, fy, sx, sy = [], [], [], []
# for i in range(len(first_points)):
#     fx.append(first_points[i][0])
#     fy.append(first_points[i][1])
#     sx.append(second_points[i][0])
#     sy.append(second_points[i][1])
#
# plt.plot(fx, fy, color='red')
# plt.plot(sx, sy, color='blue')
# plt.show()