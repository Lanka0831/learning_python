# Задание 7
# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n). Она отвечает за получение факториала числа.
# В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.

from itertools import count


def fact(n):
    factorial = 1

    for x in count(1):
        if x > n:
            break

        factorial = factorial * x
        yield factorial


n = int(input('Укажите целое положительное число: '))
i = 0

for el in fact(n):
    i += 1
    print(f"!{i} = {el}")
