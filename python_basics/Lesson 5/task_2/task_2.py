"""
Приложение:
    1. Читает содержимое файла
    2. Считает количество строк в нем
    3. Считает количество слов в каждой строке

* Путь к файлу задается в качестве параметра при запуске приложения
* Разделителем слов в строке является пробел

Created: 22.05.2022
Author: A.S.Kolesnik
"""

import sys

MODE_FILE_R = "r"

def get_count_lines(lines:list)->int:
    """
    Считает количнство строк в файле
    :param lines: строки из файла в виле списка
    :return: количество строк в файле
    """
    return len(lines)

def get_count_words(line:str)->int:
    """
    Считает количество слов в строке
    Разделитель слов - пробел
    :param line: очередная строка из файла
    :return: количество слов в строке
    """
    return len(line.split())

def do_file(path:str)->dict:
    """
    Читает содержимое файла
    Считает количество строк
    Считает количество слов в каждой строке
    :param path: путь к файлу
    :return: словарь, где ключ - номер строки(начиная с 1), значение - количество слов
    """

    lines_info = {}
    try:
        with open(path, MODE_FILE_R) as r_file:
            f_lines = r_file.readlines()
            lines_info = {l_id + 1:get_count_words(f_lines[l_id]) for l_id in range(get_count_lines(f_lines))}
    except IOError as err:
        print(err)

    return lines_info

def report(lines_info:dict):
    """
    Выводит в консоль информацию о файле
        1. Количество строк в файле
        2. Количество слов в каждой строке
    :param lines_info:
    :return:
    """
    print(f"Количество строк в файле: {len(lines_info)}")
    for line_num, words_num in lines_info.items():
        print(f"Количество слов в строке {line_num}: {words_num}")

def wrapper():
    """
    Функция-обертка приложения
    :return:
    """
    if len(sys.argv) < 2:
        raise Exception("Отсутствует путь к файлу")

    path_file = sys.argv[1]

    lines_info = do_file(path_file)
    report(lines_info)

if __name__ == '__main__':
    wrapper()