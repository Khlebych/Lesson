# Сделайте так, чтобы число секунд отображалось в виде:
# дни:часы:минуты:секунды.
#  «%» - Остаток — это оставшаяся после целочисленного деления часть числа.
#  «//»- целочисленное деление.

from random import randint

def calc(second):                       #  = 150000
    _day = second // (24 * 3600)        # 1
    second %= 24 * 3600
    _hour = second // 3600              # 17
    second %= 3600
    _min = second // 60                 # 40
    second %= 60                        # 0
    print(f'{_day} days : {_hour} h : {_min} min : {second} sec')


random_number = randint(1, 999999)
print(f' {random_number} sec ')
calc(random_number)

