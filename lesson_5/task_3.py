# Задание 3
# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32


money = []
with open('test.txt', 'r', encoding='utf-8') as f:
    print ('Оклад менее 20 тысяч имеют:')
    for i in f:
        b = i.split()
        i = int(i.split(' ')[1])
        if i < 20000:
            print (f' {b}')
        money.append(i)
total = 0
line = len(money)
for number in money:
    total += number
medium = total / line
print(f'Средняя величина дохода: {medium}')
