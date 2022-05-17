
static_rating = [9,8,8,7,6,5,4,4,4]

def get_rating():
    """
    1. Запрашивает у пользователя натуральное число
    2. Формирует рэйтинг, учитывая введенное число
    3. Печатает рэйтинг в консоль
    4. Запросы у пользователя будут продолжатся, пока пользователь
    не введет команду stop вместо натурального числа
    :return:
    """

    global static_rating
    users_input = None

    while users_input != 'stop':
        if users_input == 'stop':
            break

        cur_rating = static_rating.copy()

        users_input = input('Введите натуральное число(или stop для выхода из программы): ')

        if not users_input.isdigit():
            raise TypeError('Введенное значение должно быть числом')

        users_input = int(users_input)
        indices_input_num = [num for num, value in enumerate(static_rating) if value == users_input]

        if indices_input_num:
            cur_rating.insert(indices_input_num[-1], users_input)
        else:
            cur_rating.append(users_input)
            cur_rating = sorted(cur_rating, reverse=True)
        print(f'Рэйтинг, учитывая введенное Вами число: {cur_rating}')