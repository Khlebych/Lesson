# Вы принимаете от пользователя последовательность чисел,
# разделённых запятой. Составьте список и кортеж с этими числами.

if_OK: bool = False
while not if_OK:
    try:
        _str = input("Введите числа через запятую\n Для выхода нажмите 'n' :")
        if _str != 'n':
            _str_lst = _str.split(",")
            ints = map(int, _str_lst)
            lst = list(ints)
            tpl = tuple(lst)
            print(f'cool!!! Your result:\n\t list  : {lst}\n\t tuple : {tpl}')
        else:
            exit('thank you!!')

    except Exception as ex:
        print(ex)
