"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв

Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.

Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""

import hashlib

res_txt = set()


def get_hash(s):
    for i in range(1, len(s)+1):
        if i == len(s):
            return
        res_txt.add(hash(s[:i]))
        res_txt.add(hash(s[i:]))
        get_hash(s[i:])


def hash(s):
    return hashlib.sha512(s.encode('utf-8')).hexdigest()


get_hash('1234')
print(res_txt)
