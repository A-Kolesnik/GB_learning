def calculate_variant_1(x, y):
    """
    Возводит число x в степень y при помощи оператора **
    :param x: действительное положительное число
    :param y: целое отрицательное
    :return: результат возведения x в степень y
    """
    if not x > 0:
        raise ValueError('Число x должно быть > 0')

    if not y < 0:
        raise ValueError('Число y должно быть < 0')

    if not y % 1 == 0:
        raise ValueError('Число y должно быть целым')

    return x ** y

def calculate_variant_2(x, y):
    """
    Возводит число x в степень y при помощи собственной реализации возведения в степень
    :param x: действительное положительное число
    :param y: целое отрицательное
    :return: результат возведения x в степень y
    """

    if not x > 0:
        raise ValueError('Число x должно быть > 0')

    if not y < 0:
        raise ValueError('Число y должно быть < 0')

    if not y % 1 == 0:
        raise ValueError('Число y должно быть целым')

    y = abs(y)

    result_pow = 1
    while y:
        result_pow *= x
        y -= 1

    result_pow = 1/result_pow

    return result_pow