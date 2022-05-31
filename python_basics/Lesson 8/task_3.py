class RedefineValueError(Exception):
    """
    Класс-исключение
    Поднимается, если данные не являются числом
    """

    def __str__(self):
        return "Вводимое значение должно быть числовым"


def check_num(u_data: str):
    """
    Проверка введенных пользователем данных на соответствие
    числовому значению
    В противном случае, генерится исключение RedefineValueError
    """
    try:
        float(u_data)
    except Exception:
        raise RedefineValueError()


def wrapper():
    """
    Функция-обертка для приложения
    Запрашивает у пользователя ввод чисел
    Проверяет введенные данные на соответствие числовому значению
    Если введенные данные - не числовое значение, генерится исключение RedefineValueError
    В противном случае, число добавляется в список
    """
    print("Введите список чисел\nКаждое число необходимо подтверждать нажатие Enter\nstop-команда остановки программы\n")
    users_numbers = []
    while True:
        user_data = input()
        if user_data == 'stop':
            break
        try:
            check_num(user_data)
        except RedefineValueError as err:
            print(err)
            continue

        users_numbers.append(user_data)

    print(f"Введенный пользователем список: {' '.join(users_numbers)}")


if __name__ == '__main__':
    wrapper()