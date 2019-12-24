import random
import math


def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(1, 100))
        list_size = list_size - 1

    return list


lst = init_random_list(7)
print("Исходный массив:", lst)

# если количество элементов нечетное,
# нужно как то разделить массив на две половины
# c помощью функции floor первая половина будет меньше
# c помощью функции ceil первая половина будет больше
# centre = math.floor(len(lst) / 2)
centre = math.ceil(len(lst) / 2)
lst = lst[centre:] + lst[:centre]

print("Модифицированный массив:", lst)
