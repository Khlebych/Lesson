_load_number = input(' Enter number separated by commas - ')
# lst_as_str = _load_number.split(",")
# lst_int = map(int, lst_as_str)
lst = list(map(int, _load_number.split(",")))
tpl = tuple(lst)
print(f'list =\t{lst}\ntuple = {tpl}')
print(f'first element of list = {lst[0]}\n\tlast element = {lst[-1]}')

