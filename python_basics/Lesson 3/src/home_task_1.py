def get_users_nums():
    """
    Запрашивает у пользователя 2 числа, проверяет введенные данные на сответствие числовому типу
    :return: список, содержащий 2 числа: [0] - делимое [1] - делитель
    """
    users_nums = [
        input('Делимое: '),
        input('Делитель: ')
    ]
    try:
        users_nums = [float(num) for num in users_nums]
    except Exception:
        raise TypeError('Для выполнения операции необходимо, чтобы делитель '
                        'и делимое были числами')

    return users_nums

def division_nums(n1, n2):
    """
    Принимает 2 числа, введенных пользователем и выполняет их деление.
    При деление на 0 генерится исключение.
    :param n1: делимое
    :param n2: делитель
    :return: результат деления
    """
    try:
        return n1/n2
    except ZeroDivisionError as div_error:
        raise ZeroDivisionError
