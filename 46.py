import random

N = 11
T = random.randint(0, 100)


def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(-3, 3))
        list_size = list_size - 1

    return list


lst = init_random_list(N)
count_positive = 0
print("Исходный массив:        ", lst)
print("Число T:", T)

for element in lst:
    if element >= 0:
        count_positive += 1

i = 0
while i < len(lst):
    if lst[i] >= 0:
        lst[i] += T/count_positive

    i += 1

print("Количество положительных чисел:", count_positive)
print("Доля которая прибавляется к каждому из них:", T/count_positive)
print("Массив после модификации:", lst)
