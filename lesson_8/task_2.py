# Задание 2
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

new_data = (input("Введите два числа (делимое и делитель) через пробел: ")).split()
try:
    if int(new_data[1]) == 0:
        raise OwnError("Делить на ноль нельзя")
    result = int(new_data[0]) / int(new_data[1])
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Результат {result}")

