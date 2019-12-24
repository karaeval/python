import random

N = 11
B = -1
C = 1


def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(-3, 3))
        list_size = list_size - 1

    return list


lst = init_random_list(N)
count_positive = 0
print("Исходный массив:        ", lst)
print("Промежуток [%s, %s]:" % (B, C))

for element in lst:
    if element >= 0:
        count_positive += 1

i = 0
j = len(lst)
while i < j:
    if B <= lst[i] <= C:
        del lst[i]
        j -= 1
    else:
        i += 1

print("Массив после модификации:", lst)
