import random

N = 11


def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(-3, 3))
        list_size = list_size - 1

    return list


lst = init_random_list(N)
is_double_zero = False
print("Исходный массив:        ", lst)


i = 0
while i < len(lst):
    if(i > 0):
        if lst[i-1] == 0 and lst[i] == 0:
            is_double_zero = True
            break

    i += 1

if is_double_zero:
    print("В массиве имеются два подряд идущих нуля")
else:
    print("В массиве нет нулей идущих подряд")
