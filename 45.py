import random

N = 11


def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(-3, 3))
        list_size = list_size - 1

    return list


lst = init_random_list(N)
sum_positive = 0
sum_negative = 0

print("Исходный массив:        ", lst)

for element in lst:
    if element >= 0:
        sum_positive += element
    else:
        sum_negative += element * -1

if sum_positive > sum_negative:
    lst.append(sum_negative - sum_positive)
elif sum_positive < sum_negative:
    lst.append(sum_negative - sum_positive)

print("Сумма положительных чисел", sum_positive)
print("Модуль суммы отрицательных чисел", sum_negative)
print("Массив после модификации", lst)
