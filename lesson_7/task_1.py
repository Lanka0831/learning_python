# Задание 1
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.


class Matrix:
    def __init__(self, *args):
        self.new_lst = list(args)

    def __str__(self):
        result = '\n'.join(map(str, self.new_lst))
        '''result -> [1 2 3] 
                     [4 5 6] 
                     [7 8 9]'''
        result = result.replace(',', '').replace('[', '').replace(']', '')
        '''result -> 1 2 3
                     4 5 6
                     7 8 9'''
        return result

    def __add__(self, other):
        new_sum = []
        line_sum = []
        for x in range (len(self.new_lst)):
            for y in range(len(self.new_lst[x])):
                line_sum.append(self.new_lst[x][y] + other.new_lst[x][y])
            new_sum.append(line_sum)
            line_sum = []
        return Matrix ('\n'.join(map(str, new_sum)))


M_OBJ_1 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(M_OBJ_1)
print()

M_OBJ_2 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(M_OBJ_2)
print()

print(f'Сумма матриц: \n{M_OBJ_1 + M_OBJ_2}')
print()
print(M_OBJ_1)
print()
print(M_OBJ_2)

