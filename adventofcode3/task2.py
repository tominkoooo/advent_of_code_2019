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


def read_file(string):
    file = open(string, "r")
    data = file.readlines()
    file.close()
    return data


first_wire = list(map(lambda x: x.strip("\n"), read_file("input.txt")[0].split(",")))
second_wire = list(map(lambda x: x.strip("\n"), read_file("input.txt")[1].split(",")))

first_points, second_points = [[0, 0]], [[0, 0]]

for i in range(len(first_wire)):
    first_points += next_point(first_points[-1], first_wire[i])

for i in range(len(second_wire)):
    second_points += next_point(second_points[-1], second_wire[i])

parsed_common_points = list(map(lambda x: int(x), read_file("common_points.txt")[0].replace("[", "").replace("]", "")
                                .split(", ")))
common_points = []

for i in range(0, len(parsed_common_points), 2):
    common_points.append([parsed_common_points[i], parsed_common_points[i+1]])

sum_intersections = []
for i in range(len(common_points)):
    a = first_points.index(common_points[i])
    b = second_points.index(common_points[i])
    sum_intersections.append(a+b)

print(min(sum_intersections))