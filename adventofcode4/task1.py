import numpy as np


def password_checker(number):
    adjacent = same_adjacent_digits(number)
    increase = increasing_numbers(number)
    if adjacent and increase:
        return 1
    else:
        return 0


def same_adjacent_digits(number):
    number = str(number)
    if number[0] == number[1]:
        return True
    elif number[1] == number[2]:
        return True
    elif number[2] == number[3]:
        return True
    elif number[3] == number[4]:
        return True
    elif number[4] == number[5]:
        return True
    else:
        return False


def increasing_numbers(number):
    number = str(number)
    if int(number[0]) <= int(number[1]) <= int(number[2]) <= int(number[3]) <= int(number[4]) <= int(number[5]):
        return True
    else:
        return False


puzzle_input = "145852-616942"
numbers_to_check = np.arange(int(puzzle_input[0:6]), int(puzzle_input[7:])+1, 1).tolist()

print(sum(list(map(password_checker, numbers_to_check))))