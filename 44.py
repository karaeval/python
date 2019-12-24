import random

N = 11


def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(-3, 3))
        list_size = list_size - 1

    return list


def get_positive():
    return random.randint(0, 10)


def get_negative():
    return random.randint(-10, -1)


lst = init_random_list(N)
count_positive = 0
count_negative = 0

print("Исходный массив:        ", lst)

for element in lst:
    if element >= 0:
        count_positive += 1
    else:
        count_negative += 1

diff = count_positive - count_negative
need_negative = True

if diff < 0:
    need_negative = False
    diff *= -1

for i in range(0, diff):
    if need_negative:
        lst.append(get_negative())
    else:
        lst.append(get_positive())

print("Массив после модификации", lst)
