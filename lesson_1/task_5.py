# Задание 5
# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.


revenue = int(input("Укажите значение выручки: "))
cost = int(input("Укажите значение издержек: "))

if revenue > cost:
        print("Выручка больше издержек")
elif revenue < cost:
    print("Издержки больше выручки")
else:
    print("Результат равен или неизвестен")