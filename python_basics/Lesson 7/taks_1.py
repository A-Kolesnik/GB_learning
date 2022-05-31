from task_1_src.exceptions import ErrorMatrixSize, ErrorMatrixAdd

class Matrix:
    """
    Класс Матрица
    Параметром конструктора является список списков(иначе -> список строк), описывающий матрицу
    ** Все длины строк долдны быть одинаковой рвзмерности
    check_add_matrix_format(...) - функция осуществляет проверку матриц на одинаковую размерность.
    ** Если размерность разная, генерится исключение
    В классе перегружен метод сложения двух матриц __add__
    В классе перегружен метод __str__


    """
    def __init__(self, matrix_data: list):

        # длина первой строки
        self.begin_line_len = len(matrix_data[0]) if len(matrix_data) > 0 else 0

        # представление матрицы в формате для вывода на экран
        self.matrix_str = ''

        # если длина одной из строк не равна длине первой строки, генерится исключений
        for line in matrix_data[1:]:
            if not len(line) == self.begin_line_len: raise ErrorMatrixSize()

        self.matrix_data = matrix_data

    def __str__(self):
        for line in self.matrix_data:
            line = [str(val) for val in line]
            self.matrix_str = f"{self.matrix_str}{'  '.join(line)}\n"
        return self.matrix_str

    @staticmethod
    def check_add_matrix_format(matrix_1, matrix_2):
        """
        Проверяет на соответствие размерностей 2 матриц
        Если размерности не совпадают, генерится исключение
        :param matrix_1: матрица 1
        :param matrix_2: матрица 2
        :return:
        """
        if not matrix_1.begin_line_len == matrix_2.begin_line_len:
            raise ErrorMatrixAdd()
        elif not len(matrix_1.matrix_data) == len(matrix_2.matrix_data):
            raise ErrorMatrixAdd()

    def __add__(self, otherMatrix):
        Matrix.check_add_matrix_format(self, otherMatrix)

        add_res = []

        for line_mtrx1, line_mtrx2 in zip(self.matrix_data, otherMatrix.matrix_data):
            line = [v_mtrx1 + v_mtrx2 for v_mtrx1, v_mtrx2 in zip(line_mtrx1, line_mtrx2)]
            add_res.append(line)

        return Matrix(add_res)


def wrapper():
    """
    Функция - обертка приложения
    :return:
    """
    # Матрица 2x2
    matrix_1_2 = Matrix([[1, 2, 3], [2, 1,3]])

    # Матрица 2x2
    matrix_2_2 = Matrix([[2, 4,3], [5, 6,3]])

    print(matrix_1_2)
    print(matrix_2_2)

    matrix_add = matrix_1_2 + matrix_2_2

    # Вывод результата сложения
    print(matrix_add)

if __name__ == '__main__':
    wrapper()



