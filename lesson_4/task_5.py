# Задание 5
#  Реализовать формирование списка, используя функцию range() и возможности генератора.
#  В список должны войти чётные числа от 100 до 1000 (включая границы).
#  Нужно получить результат вычисления произведения всех элементов списка.


from functools import reduce

first_list=[x for x in range(100,1001, 2)]


def my_func(prev_el, el):
    return prev_el * el


print(f"Первый список: {first_list}")
print(f"Результат: {reduce(my_func, first_list)}")

