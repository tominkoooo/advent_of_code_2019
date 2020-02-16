import math


def one_module(mass):
    req_fuel = 0
    while mass >= 0:
        mass = math.floor(mass/3)-2
        if mass >= 0:
            req_fuel += mass
        else:
            continue
    return req_fuel


file = open("input.txt", "r")
data = file.readlines()
file.close()

data = list(map(lambda x: int(x), data))

total_fuel = sum(list(map(one_module, data)))
print(total_fuel)
