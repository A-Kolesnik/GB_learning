def my_func(num_1, num_2, num_3):
    """
    Принимает три аргумента
    Осуществлят проверку на соответствие каждого аргумента числовлму типу
    Выбирает 2 наибольших аргумента
    Суммирует их
    :param num_1: число 1
    :param num_2: число 2
    :param num_3: число 3
    :return: сумма 2 наибольших чисел
    """
    if not float(num_1) or not float(num_2) or not float(num_3):
        raise TypeError('Все аргументы должны быть числами')
    list_nums = [num_1, num_2, num_3]
    list_nums.remove(min(list_nums))
    return sum(list_nums)