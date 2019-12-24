import random
import math

N = 11
M = 3
K = 7
P = 1

def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(1, 100))
        list_size = list_size - 1

    return list


lst = init_random_list(N)
print("Исходный массив:", lst)

lst[K:K+M], lst[P:P+M] = lst[P:P+M], lst[K:K+M]

print("Модифицированный массив:", lst)
