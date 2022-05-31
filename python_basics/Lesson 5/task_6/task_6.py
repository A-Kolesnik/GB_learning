"""
** Читает данные о количестве занятий из файла
** Путь к файла передается в качестве параметра при запуске скрипта
** Формат представления данных в файле должен иметь следующий вид:
    Предмет Лекции Практика Лабораторные

Created: 22.05.2022
Author: A.S.Kolesnik
"""

import sys

MODE_FILE_R = "r"

def get_f_data(path:str)->list:
    """
    Читает строки из файла - формирует список строк
    :param path: путь к файлу
    :return: список строк из файла
    """
    try:
        with open(path, MODE_FILE_R, encoding='utf-8') as r_file:
            return r_file.readlines()
    except IOError as err:
        print(err)

def calc_sum_lessons(f_lines:list)->dict:
    """
    Формирует словарь, в котором ключ - наименование предмета, значение: количнство занятий
    Считает количество занятий по каждому предмету
    :param f_lines: список строк из файла
    :return: словарь наименование_предмета : количество_занятий
    """
    rep_info = {}
    for line in f_lines:
        line_split = line.split()
        name_subject = line_split[0]
        try:
            cnt_lesson = sum([float(cnt.strip()) for cnt in line_split[1:]])
            rep_info[name_subject] = cnt_lesson
        except TypeError as err:
            print(err)

    return rep_info

def report(rep_data:dict):
    """
    Выводит результирующий словарь
    :param rep_data: словарь, описывающий предметы
    :return:
    """
    for name, cnt in rep_data.items():
        print(f"{name}: {cnt:.0f}")


def wrapper():
    """
    Функция-обертка приложения
    :return:
    """

    if len(sys.argv) < 2:
        raise Exception("Указаны не все параметры для запуска")

    f_data = get_f_data(sys.argv[1])

    if not f_data:
        return

    rep_data = calc_sum_lessons(f_data)
    report(rep_data)

if __name__ == "__main__":
    wrapper()