def get_set_numbers():
    """
    Запрашивает у пользователя числа, указанные через пробел
    :return: список, содержащий введенные значения (преобразованные к числовому формату)
    """
    users_set = input('Введите произвольное количество чисел. В качестве разделителя должен использоваться пробел: ')
    if users_set == 'exit':
        exit()
    users_set = users_set.split()
    if users_set:
        try:
            users_set = [float(num) for num in users_set]
        except Exception:
            raise TypeError('Указанные через пробел значения должны быть числовыми')

    return users_set

def sum_users_number():
    """
    Суммирует введенные пользователем значения
    :return:
    """
    print('Для выхода из программы в поле ввода укажите exit')
    users_sum = 0
    while True:
        users_sum += sum(get_set_numbers())
        print(f'Сумма введенных чисел (считаются все итерации): {users_sum}')