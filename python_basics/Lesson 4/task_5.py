from functools import reduce

start_range = 100
stop_range  = 1000

def report(res):
    """
    Выводит результат работы программы в консоль
    :param res:
    :return:
    """
    print(
        f"Произведение всех элементов сформированного списка: {res}"
    )

def multi_it(it):
    """
    Произведение всех элементов сформированного ранее списка
    :param it: сформированный список
    :return: произведение всех элементов
    """
    res_multi = reduce(lambda drive,item: drive*item, it)
    report(res_multi)


def get_even_nums():
    """
    Формирование списка четных чисел в диапазоне [start_range, stop_range]
    :return: сформированный список четных чисел из заданного диапазона
    """
    return [item for item in range(start_range, stop_range + 1) if item%2 == 0]

def wrapper_program():
    """
    Обвязка программы
    :return:
    """
    multi_it(get_even_nums())

if __name__ == '__main__':
    wrapper_program()