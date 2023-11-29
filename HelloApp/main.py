#       ДЗ
# Списки и словари в Python


# 1 создаем список из 10 последовательных натуральных чисел, начиная с 5.

list_natural_number = []

for i in range(10):
    list_natural_number.append(i + 5)

print('#1', list_natural_number)

# 2 список из чисел п.1, стоящих на чётных индексах

list_evenNumber = []
for i in list_natural_number:
    if i % 2 != 0:
        list_evenNumber.append(i)
print('#2', list_evenNumber)

# 3 полное произведение чисел из списка п.2

multiply = 1
for i in list_evenNumber:
    multiply = i * multiply
print('#3', multiply)

# 4 полная сумма чисел из списка п.2

summa = 0
for i in list_evenNumber:
    summa = summa + i
print('#4', summa)

# 5 список из чисел п.2, 3, 4, отсортированных по убыванию.

new_list = sorted([summa] + [multiply] + list_evenNumber, reverse=True)
print('#5', new_list)

# 6 Перевести каждый элемент списка п.5 в строку

str_new_list = []
for i in new_list:
    i = str(i)
    str_new_list.append(i)
    print('#6 i = ', i)
print('#6', str_new_list)

# 7 соединяем через =

vowels_new_list = "=".join(str_new_list)
print('#7 - ', vowels_new_list)

# задание 2

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 5, 9, -7, -10]
b = []

for i in a:
    if i < 5:
        i = str(i)
        b.append(i)

b1 = ", ".join(b)

print('# задание 2 - ', b1)

# Задание 3
"""
вернуть список, который состоит из элементов, общих для этих двух списков.
Список должен содержать только уникальные значения и быть отсортирован по возрастанию.
Вывод через запятую без кавычек.
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 11]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 34, 11, 12, 13]
c = list(set(a) & set(b))
c1 = sorted(c)
c2 = []
for i in c1:
    i = str(i)
    c2.append(i)

c3 = ", ".join(c2)
print('# Задание 3 - ', c3)

# 4 Задание 4. Считаем слова в строке

s = 'kafka python course stack flow dict list python stack course star product ' \
    'star product analytics flow star kafka stack flow ython list set ist fit predict ' \
    'dict list python ourse ython ourse star product ist fit predict analytics kafka stack ' \
    'flow product ist fit predict analytics star flow dict flow list python course stack ' \
    'flow dict list python stack course'

# создаем из строки список слов s_word_list

s_word_list = []
for word in s.split():
    s_word_list.append(word)

# из списка s_word_list создаем словарь s_dict (слово -- это ключ, а их количество  -- значение

s_dict = {}
for item in s_word_list:
    s_dict.setdefault(item, s_word_list.count(item))
print(f'#4 Задание 4 - ', max(s_dict, key=s_dict.get))

# 5 Задание 5 Словарь из двух списков. Выведи профессию maria.

names = ['igor', 'dasha', 'martin', 'vladimir', 'rishat', 'maria', 'marat',
         'petr', 'dima', 'polina', 'katya', 'elena']
occupations = ['smm', 'developer', 'analyst', 'president', 'analyst',
               'ceo', 'customer development', 'founder', 'developer',
               'ml engineer', 'product manager', 'cmo']

dict_name_occ = dict(zip(names, occupations))
print(f'#5 Задание 5 - ', dict_name_occ.get('maria'))

# 6 Задание 6. Три в одном


dict1 = {1: 10, 2: 20, 3901: 11, 384: 13, 8489: 1, 48: 10}

dict2 = {3: 30, 4: 40, 93: 12, 91: 41, 95: 1, 841: 11, 584: 11}

dict3 = {5: 50, 6: 60, 9: 90, 3: 13, 7: 11}

dict_united = {**dict1, **dict2, **dict3}

track = {}
for key, value in dict_united.items():
    if value not in track:
        track[value] = 0
    else:
        track[value] += 1

print(f'#6 Задание 6 - {len(dict_united)},{max(track, key=track.get)}')

"""
7 Задание 7. Самая непопулярная буква
"""

given_string = 'Python Star Course for beginners and experts \
                for data science and analytics without sql with code'
a = dict((letter, given_string.count(letter)) for letter in given_string)
a1 = {}
for k, v in a.items():
    a1.setdefault(v, []).append(k)
""" print(a1[min(a1)])  __ здесь бы мы вывели ЗНАЧЕНИЕ словаря a1 с минимальным ключом = 1,
        то есть это символы, которые встретились в тексте given_string ровно 1 раз 
        (в порядке расположения в тексте)). Их оказалось 8. Если бы по условию задания нужно 
        было вывести первые  например, 10 символов, тогда бы нужно было взять из следующего ключа
        недостающие символы
тогда:
"""

valuesList = list(a1.values())  # превращаем в список
vL = []
for i in valuesList:
    i = str(i)
    vL.append(i)

# превращаем vL в строку
my_str = ''.join(vL)

# удалим всякие скобки пробелы запятые из my_str
my_res_str = my_str.translate({ord(i): None for i in "[]', "})
print(f'#7 Задание 7 - ', my_res_str[:8])
