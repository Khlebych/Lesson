"""
Напишите программу, которая выводит чётные числа из заданного списка
и останавливается, если встречает 237.
"""

from random import sample

""" заполняем лист 10 произвольными числами"""
random_lst = sample(range(1, 240), 10)
even_lst = []

for i in random_lst:
    if i == 237:
        print(f'there is a number {i} in the list. Еhe program stops working')
        exit()
    elif i % 2 == 0:
        even_lst.append(i)
print("OK. list =", even_lst)
