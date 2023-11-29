def all_uniq(num):
    return len(num) == len(set(num))


num = (1, 2, 1, 3, 6, 5, 2, 3, 6, 9, 8, 7)
print(all_uniq(num))

