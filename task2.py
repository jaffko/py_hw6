# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

list1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
max_number = int(input('Максимальный элемент: '))
min_number = int(input('Минимальный элемент: '))
res = []
for i in range(len(list1)):
    if min_number < list1[i] < max_number:
        res.append(i)
print(res)