'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно
 — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
'''


class Matrix():
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        return self.draw_Matrix()

    def draw_Matrix(self):
        string = ''
        for list in self.lst:
            for index in list:
                string = string + '%s\t' % (index)
            string = string[:-1]
            string = string + '\n'
        string = string[:-1]
        return f"{string}\n\n"

    def addition(A, B):
        d = []
        n = 0
        while n < len(B):
            c = []
            k = 0
            while k < len(A[0]):
                c.append(A[n][k] + B[n][k])
                k = k + 1
            n += 1
            d.append(c)
        return d

    def __add__(self, other):
        return Matrix(Matrix.addition(self.lst, other.lst))

    def __repr__(self):
        return str(self.lst)


A = Matrix([[1, 2, 3], [44, 51, 6], [7, 8, 9]])
B = Matrix([[3, 21, 1], [6, 5, 4], [9, 81, 7]])
print(A,B)
print(A + B)




