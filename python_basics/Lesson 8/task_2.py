class RedefineZeroDivision(Exception):
    """
    Класс-исключение
    Поднимается при делении на 0
    """

    def __str__(self):
        return "Деление на ноль недопустимо"


def check_type(divident: str, divider: str):
    """
    Проверка возможности преобразования введенных пользователем
    данных к типу float
    При отсутствии такой возможности, поднимается исключение TypeError

    """
    try:
        float(divident)
        float(divider)
    except ValueError as err:
        return 1
    return 0


def check_value_divider(divider: str):
    """
    Проверяет значение делителя
    Если равен 0, поднимается исключение RedefineZeroDivision
    """
    if float(divider) == 0:
        raise RedefineZeroDivision()


def report(res_division: float):
    """
    Печатает результат деления на экран
    """
    print(
        f"Результат деления: {res_division}"
    )


def wrapper():
    """
    Функция-обертка приложения
    1. Запрашивает у пользователя ввод делимого и делителя
    2. Проверяет типы введенных данных. Всмысле возможности их преобразования
        к типу float.
    3. Проверяет значение делителя на предмет равенства 0
    4. Выполняет деление и печатает отчет
    """

    divident = input("Делимое: ")
    divider = input("Делитель: ")

    if check_type(divident, divider):
        print("Делимое и делитель - числовые значения !!!")
        return

    try:
        check_value_divider(divider)
    except RedefineZeroDivision as err:
        print(err)
        return

    report(
        float(divident) / float(divider)
    )


if __name__ == '__main__':
    wrapper()