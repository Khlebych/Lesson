def is_palindrome2(_s):
    _sLow = _s.lower()
    _sJo = _sLow.replace(" ", '')
    for i in range(0, int(len(_sJo) / 2)):
        if _sJo[i] != _sJo[len(_sJo) - 1 - i]:
            return False
    return True


_s =input("Введите выражение - : ")
print("Yes's" if is_palindrome2(_s) else "No")
