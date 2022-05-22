"""
Читает данные из файла
Производит замену английских числительных на русские
Записывает полученные данные в новый файл

* Пути к файлам указываются в качестве параметров при запуске скрипта

Created: 22.05.2022
Author: A.S.Kolesnik
"""
import sys

MODE_FILE_R = "r"
MODE_FILE_A = "a"

rus_nums = {
    "1" : "Один",
    "2" : "Два",
    "3" : "Три",
    "4" : "Четыре",
    "5" : "Пять",
    "6" : "Шесть",
    "7" : "Семь",
    "8" : "Восемь",
    "9" : "Девять",
    "10" : "Десять",
}

def get_f_data(path_in:str)->list:
    """
    Читает строки из файла в список
    Возвращает полученный сптсок
    :param path_in: путь к файлу, строки из которого необходимо прочитать
    :return: список строк из файла
    """
    f_data = None

    try:
        with open(path_in, MODE_FILE_R) as r_file:
            f_data = r_file.readlines()
    except IOError as err:
        print(err)

    return f_data

def put_file(mod:dict, path:str):
    """
    Записывает в файл новое описание чисел
    :param path: Путь к файлу, в который необходимо записать
    :param mod: словарь -> русское нименование числа : число
    :return:
    """
    try:
        with open(path, MODE_FILE_A) as w_file:
            for num_name, num in mod.items():
                w_file.write(f"{num_name} - {num}\n")
    except IOError as err:
        print(err)

def wrapper():
    """
    Функция-обертка приложения
    :return:
    """
    if len(sys.argv) < 3:
        raise Exception("Указаны не все параметры для запуска")

    file_in = sys.argv[1]
    file_out = sys.argv[2]

    file_lines = get_f_data(file_in)

    modify_num = {rus_nums[line.split('-')[1].strip()]:line.split('-')[1].strip() for line in file_lines}
    put_file(modify_num, file_out)

if __name__ == '__main__':
    wrapper()