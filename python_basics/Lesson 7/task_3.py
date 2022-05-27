class Cell:
    """
    Класс клетка
    Перегружены методы, осуществляющие математические операции, указанные в задании
    """
    def __init__(self, count_area):
        self._count_area = count_area

    def __add__(self, cell_other):
        return Cell(self._count_area + cell_other._count_area)

    def __sub__(self, cell_other):
        sub_cells = self._count_area - cell_other._count_area
        if sub_cells < 0:
            print('Разность количества ячеек 2 клеток - отрицательное число')
        else:
            return Cell(sub_cells)

    def __mul__(self, cell_other):
        return Cell(self._count_area * cell_other._count_area)

    def __truediv__(self, cell_other):
        return Cell(self._count_area // cell_other._count_area)

    def make_order(self, cnt_cells_row):
        """
        Формирование строки, описывающей клетку для вывода на эран
        :param cnt_cells_row: количество ячеек в строке
        :return: строка, описывающая клетку
        """
        res_str = ''
        if cnt_cells_row > self.count_area:
            print(
                'Нельзя сформировать ни одного ряда, поскольку количество ячеек в ряду больше количества ячеек в клетке')
            return res_str

        count_row = self.count_area // cnt_cells_row
        remainder = self.count_area - count_row * cnt_cells_row

        res_str = ['|*| ' * cnt_cells_row for _ in range(count_row)]
        res_str = "\n".join(res_str)
        res_str = f"{res_str}\n{'|*| ' * remainder}"
        return res_str

    @property
    def count_area(self):
        """
        Функция getter
        :return:
        """
        return self._count_area

    @count_area.setter
    def count_area(self, value):
        """
        Функция setter
        :param value: новое значение
        :return:
        """
        self._count_area = value

def wrapper():
    cell_1 = Cell(100)
    cell_2 = Cell(6)

    print(cell_1.make_order(10))

    res_add = (cell_1 + cell_2).count_area
    print(f"Количество ячеек в новой клетке(сложение): {res_add}")

    res_sub = cell_1 - cell_2
    if res_sub:
        res_sub = res_sub.count_area
        print(f"Количество ячеек в новой клетке(вычитание): {res_sub}")

    res_multi = (cell_1 * cell_2).count_area
    print(f"Количество ячеек в новой клетке(умножение): {res_multi}")

    res_div = (cell_1 / cell_2).count_area
    print(f"Количество ячеек в новой клетке(деление): {res_div}")

if __name__ == '__main__':
    wrapper()