import random

N = 11


def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(-3, 3))
        list_size = list_size - 1

    return list


lst = init_random_list(N)
count_divided_by_3 = 0
sum_even = 0
count_event = 0
print("Исходный массив:        ", lst)


i = 0
while i < len(lst):
    if lst[i] % 3 == 0 and lst[i] != 0:
        count_divided_by_3 += 1

    if lst[i] % 2 == 0:
        sum_even += lst[i]
        count_event += 1

    i += 1

lst.insert(0, count_divided_by_3)
lst.append(sum_even/count_event)

print("Модифицированный массив:", lst)
