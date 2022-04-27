seasons_lst = [
    'Зима',
    'Зима',
    'Весна',
    'Весна',
    'Весна',
    'Лето',
    'Лето',
    'Лето',
    'Осень',
    'Осень',
    'Осень',
    'Зима',
]

seasons_dict = {
    '1': 'Зима',
    '2': 'Зима',
    '3': 'Весна',
    '4': 'Весна',
    '5': 'Весна',
    '6': 'Лето',
    '7': 'Лето',
    '8': 'Лето',
    '9': 'Осень',
    '10': 'Осень',
    '11': 'Осень',
    '12': 'Зима',
}

def get_season_from_list(month_number):
    """
    Возвращает время года, используя для поиска список
    :param month_number: введенная пользователем инфформация
    :return:
    """
    if not month_number.isdigit():
        raise TypeError('Указанное значение не является числовым')

    if not 0 < int(month_number) <= 12:
        raise ValueError('Вводимое значение должно быть в диапазоне [1:12]')
    return seasons_lst[int(month_number) - 1]

def get_season_from_dict(month_number):
    """
    Возвращает время года, используя для поиска словарь
    :param month_number: введенная пользователем инфформация
    :return:
    """
    if not month_number.isdigit():
        raise TypeError('Указанное значение не является числовым')

    if not 0 < int(month_number) <= 12:
        raise ValueError('Вводимое значение должно быть в диапазоне [1:12]')
    return seasons_dict[month_number]