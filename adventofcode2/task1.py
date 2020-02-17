file = open("input.txt", "r")
data = file.readlines()
file.close()
data = list(map(lambda x: int(x), data[0].split(",")))

data[1] = 12
data[2] = 2

for i in range(0, len(data), 4):
    if data[i] == 1 and i % 4 == 0:
        try:
            data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
            i += 4
            continue
        except:
            print("1202 Program Alarm - sum")
            break
    if data[i] == 2 and i % 4 == 0:
        try:
            data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
            i += 4
            continue
        except:
            print("1202 Program Alarm - mult")
            break
    if data[i] == 99:
        print("Halt")
        break
    else:
        print("1202 Program Alarm")
        break

print(data[0])
