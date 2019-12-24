import random


def init_random_list(list_size):
    list = []
    while list_size > 0:
        list.append(random.randint(1, 100))
        list_size = list_size - 1

    return list


lst = init_random_list(9)
print("Исходный массив:", lst)

# range(5) создаст список (0,1,2,3,4)
# for i in range значит что
# при первой итерации i будет равен 0,
# при второй итерации i будет равен 1,
# ...
# при пятой итерации i будет равен 4,
# таким образом, указывая lst[i] мы можем обращаться к элементам списка
for i in range(len(lst) - 1):
    if i % 2 == 0:
        lst[i], lst[i+1] = lst[i+1], lst[i]

print("Модифицированный массив:", lst)
