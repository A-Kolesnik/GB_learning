from math import factorial

up_range = 7

def do_gen(border):
    """
    Возвращает генератор
    :param border: верхняя граница счетчика
    :return: генератор
    """
    for n in range(1, border+1):
        yield factorial(n)

def wrapper_program(border):
    """
    Обвязка программы
    Печатает в консоль результат вычисления для чисел из диапазона [1, up_range]
    :param border:
    :return:
    """
    for num_factorial in do_gen(border):
        print(num_factorial)

if __name__ == '__main__':
    wrapper_program(up_range)
