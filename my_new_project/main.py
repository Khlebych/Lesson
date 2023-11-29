"""
Задача 8
Напишите проверку на то, является ли строка палиндромом.
"""

""" 
убираем пробелы и переводим в нижний регистр 
"""


def reduc(_s):
    str_low = _s.lower()
    str_rep = str_low.replace(" ", '')
    return str_rep


""" 
разворачиваем строку 
"""


def reverse(_s):
    rev = reduc(_s)[::-1]
    return rev


def is_palindrome(_s):
    if reduc(_s) != reverse(_s):
        return False

    else:
        return True


_s = input("Введите строку для проверки на палиндромность - ")
# s = "Z роза упала на лапу Азора"
# s = "qwertyqwe asds reqwwq"
ans = is_palindrome(_s)
if not ans:
    print("Это не палиндром")
else:
    print("Это палиндром")
