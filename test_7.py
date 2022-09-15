# Задание
# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n). Она отвечает за получение факториала числа.
# В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.

def create_generator(num):
    mylist = range(num)
    for i in mylist:
        yield i * i


num = int(input('Enter number:'))
my_generator = create_generator(num)  # создаём генератор
for i in my_generator:
    print(i)
