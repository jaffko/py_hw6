# Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


first = int(input('Первый элемент: '))
diff = int(input('Разность: '))
count = int(input('Кол-во элементов: '))

def progression(a,n,d):
    result = []
    result.append(a)
    for i in range(2,n+1):
        result.append(a + (i-1) * d)
    return result

print(*progression(first,count,diff))
    