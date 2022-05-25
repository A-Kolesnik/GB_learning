import sys
import json

MODE_FILE_R = "r"
MODE_FILE_A = "a"

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

def form_info(lines:list)->list:
    """
    Считает прибыль каждой компании
    Считает среднюю прибыль
    Формирует список словарей согласно формату, указанному в задании
    :param lines: список строк из файла
    :return: список словарей
    """
    firms_info = [
        {},
        {}
    ]
    sum_profit = 0
    cnt_not_profit = 0

    try:
        for line in lines:
            line_split = line.split()
            profit = float(line_split[-2].strip()) - float(line_split[-1].strip())
            firms_info[0][line_split[0]] = profit
            if profit > 0:
                sum_profit += profit
            else:
                cnt_not_profit += 1
    except TypeError as err:
        print(err)

    firms_info[1]['average_profit'] = sum_profit/(len(lines) - cnt_not_profit)

    return firms_info

def json_save(path:str, info:list):
    """
    Формирует json-объект
    Сохраняет сформированный json в файл
    :param info: итоговый список
    :param path: путь к файлу
    :return:
    """
    try:
        with open(path, MODE_FILE_A) as w_file:
            w_file.write(json.dumps(info))
    except IOError as err:
        print(err)

def wrapper():
    """
    Функция-обертка приложения
    :return:
    """

    if len(sys.argv) < 3:
        raise Exception("Указаны не все параметры для запуска")

    f_data = get_f_data(sys.argv[1])
    firms_info = form_info(f_data)
    json_save(sys.argv[2], firms_info)

if __name__ == '__main__':
    wrapper()