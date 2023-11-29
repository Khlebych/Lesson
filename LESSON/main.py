"""
 Задача 1
Выведите все элементы, которые меньше 5
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print("lesson 1 : ", [el for el in a if el < 5])

"""
 Задача 2
Нужно вернуть список, который состоит из общих элементов
для данных списков.
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for el in a:
    for i in b:
        if el == i:
            c.append(el)
print("lesson 2 : ", c)

"""
Задача 3
Отсортируйте словарь по значению в порядке возрастания и убывания.
"""

import operator as op

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
res = dict(sorted(d.items(), key=op.itemgetter(1)))
res1 = dict(sorted(d.items(), key=op.itemgetter(1), reverse=True))
print("lesson 3 :\tsorted up -\t", res,
      '\n\t\t\tsorted down-', res1)

"""
Задача 4
Напишите программу для слияния нескольких словарей в один.
"""

# way1
dict_a = {1: 10, 2: 20}
dict_b = {3: 30, 4: 40}
dict_c = {5: 50, 6: 60}
res_way1 = {**dict_a, **dict_b, **dict_c}
print("lesson 4 :  way1 - ", res_way1)

# way2
res_way2 = {}
for d in (dict_a, dict_b, dict_c):
    res_way2.update(d)
print("\t\t\tway2 - ", res_way2)

"""
Задача 5
Найдите три ключа с самыми высокими значениями в словаре my_dict
"""

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
max_key = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
print("lesson 5 : ", max_key)

"""
Задача 6
Напишите код, который переводит целое число в строку, 
при том что его можно применить в любой системе счисления.
"""

print("lesson 6 : ")
a = str(input("Enter integer number : "))
print("lesson 6 : ", a, 'type ', type(a))

""" Задача 7
Нужно вывести первые n строк треугольника Паскаля. 
В этом треугольнике на вершине и по бокам стоят единицы, 
а каждое число внутри равно сумме двух расположенных над ним чисел.
"""

print("lesson 7 : ")


def pascal_triangle(n):
    row = [1]
    y = [0]
    for x in range(max(n, 0)):
        print(row)
        row = [left + right for left, right in zip(row + y, y + row)]


pascal_triangle(6)
