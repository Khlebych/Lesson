"""
При заданном целом числе n посчитайте n + nn + nnn.
"""


def summa_n(n):
    a = n
    b = n + n
    c = n + n + n
    res = int(a) + int(b) + int(c)
    print(res)


summa_n(input("enter integer number: "))
