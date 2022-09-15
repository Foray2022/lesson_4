# Задание
# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

# Решение

from sys import argv
# список аргументов командной строки, которые передаем скрипту.
script, output_hours, rate_per_hour, bonus = argv
# провека на тип данных
try:
    # с помощью функции map передаем параметры скрипта в переменные
    output_hours, rate_per_hour, bonus = map(float, argv[1:])
    salary = output_hours * rate_per_hour + bonus
    print(f'staff salary:,{salary}')
except TypeError:
    print('incorrect value type')
