import random

N = 11

def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(-3, 3))
        list_size = list_size - 1

    return list


lst = init_random_list(N)
print("Массив:        ", lst)

is_up = True
prev = lst[0]

i = 0
while i < len(lst):
    element = lst[i]

    if element < 0:
        break

    if element < prev:
        is_up = False

    prev = element
    i += 1


if i == 0:
    print("Последовательность не успела начаться")
elif i == 1:
    print("Последовательность состоит из 1 элемента")
elif is_up:
    print("Последовательность возрастает")
else:
    print("Последовательность не возрастает")
