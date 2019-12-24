import random

N = 11

def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(-3, 3))
        list_size = list_size - 1

    return list


lst = init_random_list(N)
lst_negative = []
lst_positive = []
print("Исходный массив:        ", lst)

for element in lst:
    if element >= 0:
        lst_positive.append(element)
    else:
        lst_negative.append(element)

print("Массив с положительными элементами", lst_positive)
print("Массив с отрицательными элементами", lst_negative)
