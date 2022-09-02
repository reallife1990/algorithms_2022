"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего

Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""

from collections import namedtuple


def start():
    name_tuple = 'profit_info'
    n = int(input('Введите кол-во предприятий'))
    companies = namedtuple(name_tuple, " name , per_1, per_2, per_3, per_4")
    profit_avr = {}
    for i in range(n):
        company = companies(name=input("Введите название предприятия: "),
                            per_1=int(input("Введите прибыль за первый квартал: ")),
                            per_2=int(input("Введите прибыль за второй квартал: ")),
                            per_3=int(input("Введите прибыль за третий квартал: ")),
                            per_4=int(input("Введите прибыль за четвертый квартал: ")))
        profit_avr[company.name] = (sum(list(company[1:])))/4

    print(profit_avr)
    average_all = 0
    for value in profit_avr.values():
        average_all += value
    average_all = average_all / n
    report = [[], []]
    print(f'Средняя годовая прибыль всех предприятий:{average_all}')
    for key, value in profit_avr.items():
        print(value)
        if value > average_all:
             report[0].append(key)
        elif value < average_all:
             report[1].append(key)

    return print(f'Предприятия, с прибылью выше среднего значения: {",".join(report[0])}\n'
                 f'Предприятия, с прибылью ниже среднего значения: {",".join(report[1])}')


start()
