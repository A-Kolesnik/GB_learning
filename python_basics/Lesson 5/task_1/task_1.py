"""
Построчная запись в файл формата txt пользовательской информации
Приложение завершает работу, когда пользователь в качестве данных указал пустую строку

Created: 22.05.2022
Author: A.S.Kolesnik

"""

P_FILE = r'./users_data.txt'
MODE_WRITE_A = "a"

def write_line(line:str, path_file:str):
    """
    Запись line в файл
    :param path_file: файл для записи
    :param line: данные для записи
    :return:
    """
    try:
        with open(path_file, MODE_WRITE_A) as w_file:
            w_file.write(f"{line}\n")
    except IOError as err:
        print(err)

def get_line()->str:
    """
    Запрашивает данные у пользователя
    :return: Введенные пользователем данные
    """
    return input("Введите данные для записи: ")

def wrapper():
    """
    Функция-обертка для приложения
    :return:
    """

    while True:
        in_line = get_line()
        if not in_line: break

        write_line(in_line, P_FILE)

    print("Запись в файл завершена")


if __name__ == '__main__':
    wrapper()