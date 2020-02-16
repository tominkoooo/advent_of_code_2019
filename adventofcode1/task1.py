import math

file = open("input.txt", "r")

data = file.readlines()
data = map(lambda x: int(x), data)

file.close()

divided = map(lambda x: math.floor(x/3)-2, data)

print(sum(list(divided)))
