def get_users_info():
    """
    Запрашивает у пользователя его личную информацию
    :return:
    """
    print('Введите Ваши данные')

    ufname = ''
    while not ufname:
        ufname = input('Имя: ')

    ulname = ''
    while not ulname:
        ulname = input('Фамилия: ')

    year_birth = ''
    while not year_birth:
        year_birth = input('Год рождения: ')

    city = ''
    while not city:
        city = input('Город: ')

    email = ''
    while not email:
        email = input('E-mail: ')

    phone = ''
    while not phone:
        phone = input('Контактный телефон: ')

    return {'ufname': ufname,
            'ulname': ulname,
            'year_birth': year_birth,
            'city': city,
            'email': email,
            'phone': phone,
            }

def print_users_info(*, ufname, ulname, year_birth, city, email, phone):
    """
    Принимает информацию о пользователе и выводит в консоль
    :param ufname: имя пользователя
    :param ulname: фамилия пользователя
    :param year_birth: год рождения пользователя
    :param city: город проживания пользователя
    :param email: электронная почта пользователя
    :param phone: контактный телефон пользователя
    :return:
    """
    print(f"\n\nПользователь {ufname} {ulname} {year_birth}\n\tГород проживания: {city}\n\tE-mail: {email}\n\tPhone: {phone}")

