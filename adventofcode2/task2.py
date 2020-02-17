def finding_output(data):
    for noun in range(100):
        data[1] = noun
        for verb in range(100):
            data[2] = verb
            temp = data[:]

            for i in range(0, len(temp), 4):
                if temp[i] == 1 and i % 4 == 0:
                    temp[temp[i + 3]] = temp[temp[i + 1]] + temp[temp[i + 2]]
                    continue
                if temp[i] == 2 and i % 4 == 0:
                    temp[temp[i + 3]] = temp[temp[i + 1]] * temp[temp[i + 2]]
                    continue
                if temp[i] == 99:
                    if temp[0] == 19690720:
                        return noun, verb
                    else:
                        break
                else:
                    break


file = open("input.txt", "r")
data = file.readlines()
file.close()
data = list(map(lambda x: int(x), data[0].split(",")))

noun, verb = finding_output(data)

print("noun = {}, verb = {}".format(noun, verb))
print(100*noun+verb)