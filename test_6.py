# Задание
# Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Предусмотрите условие его завершения. #### Например, в первом задании выводим целые числа, начиная с 3.
# При достижении числа 10 — завершаем цикл. Вторым пунктом необходимо предусмотреть условие,
# при котором повторение элементов списка прекратится.

# Решение_1
from itertools import count, islice, cycle

num_start = int(input('Enter the initial number:'))
num_stop = int(input('Enter the number of repetitions'))
my_list = [el_list for el_list in islice(count(num_start), num_stop)]
print(my_list)
my_list_2 = [el_list for el_list in islice(cycle(my_list), num_stop)]
print(my_list_2)
