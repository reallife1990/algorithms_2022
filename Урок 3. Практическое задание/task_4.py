"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""
import hashlib


dct_cash = {}
salt = 'my_salt'


def cash_url():
    url = input("Введите url,\n0 для выхода,\n'i' для просмотра количества записей в кэше")
    if url == '0':
        return

    elif url == 'i':
        print(f'Записей в кэше {len(dct_cash)}')
        cash_url()
    else:
        url_hash = hashlib.sha512((url+salt).encode('utf-8'))
        if dct_cash.get(url):
            print(f'Хэш ссылки - {dct_cash[url]}')
        else:
            dct_cash[url] = url_hash.hexdigest()
            print('Добавлено в кэш')
    cash_url()


cash_url()
