import requests
from requests import HTTPError


# На вход принимаем нужный http-код, по умолчанию - 200 (Нормальное завершение запроса)
def send_request(status_code=200):
    # Функция requests.get отправляет GET-запрос по-указанному URL и возвращает ответ.
    response = requests.get("https://httpstat.us/%d" % status_code)

    # По-умолчанию библиотека requests не выбрасывает исключения у кодов, означающих ошибку.
    # Исключение нужно вызвать самому при помощи функции raise_for_status.
    response.raise_for_status()
    # Возвращаем код ответа
    return response.status_code


# Читаем ввод пользователя и преобразуем строку из input в int

while True:
    try:
        code: int = int(input("Введите http код для проверки >>>"))
        break

    except ValueError as ex:
        print(f'{ex}\nБудьте внимательны!!\nВводим ТОЛЬКО цифры!!')

response_code = None
try:
    # Отправляем запрос и получаем ответ
    response_code = send_request(code)

# Обработаем HTTPError https://requests.readthedocs.io/en/latest/api/
# requests.HTTPError

except HTTPError as ex:
    # Выводим текст ошибки
    print("Произошла ошибка при отправке HTTP-запроса: %s" % str(ex))

    # Меняем переменную response_code
    response_code = ex.response.status_code

finally:
    print("Получен код:")
    # Выводим на экран response_code
    print(response_code)
