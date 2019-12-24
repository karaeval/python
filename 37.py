import random
import math

N = 11

def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(-100, 100))
        list_size = list_size - 1

    return list


lst = init_random_list(N)
print("Исходный массив:        ", lst)

sum = 0
positive_num = 0

for i in range(len(lst)):
    sum += lst[i]
    if lst[i] > 0:
        positive_num += 1

# можно вставить в начало списка вычисленные значения
# lst.insert(0, sum)
# lst.insert(1, positive_num)

# а можно заменить первый и второй элемент списка
lst[0] = sum
lst[1] = positive_num



print("Модифицированный массив:", lst)
