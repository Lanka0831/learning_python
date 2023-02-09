# Задание 5
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.


with open('test_5.txt', 'w+', encoding='utf-8') as f:
    numbers = input('Введите цифры через пробел ')
    f.writelines(numbers)
    result = numbers.split()
    print(sum(map(int, result)))
