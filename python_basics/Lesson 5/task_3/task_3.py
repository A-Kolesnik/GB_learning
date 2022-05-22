"""
Приложение:
    1. Определяет сотрудников, оклад которых < 20000
    2. Выполняет подсчет средней величины окладов сотрудников

Created: 22.05.2022
Author: A.S.Kolesnik
"""
import sys

MODE_FILE_R = "r"
WAGE_THRESHOLD = 20000.00

def get_user_wage(line:str)->dict:
    if len(line.split()) != 2:
        raise ValueError("Строка должна иметь формат -> Фамилия Доход")

    line = line.strip()

    try:
        info = line.split()
        return {info[0]:float(info[1])}
    except ValueError as err:
        print(err)

def get_wages_info(path_file:str)->dict:
    """
    Читает содержимое файла
    Формирует словарь из полученной информации
    :param path_file: путь к файлу с данными о доходах
    :return: словарь вида ключ - фамилия сотрудника, значение-его доход
    """
    wages_info = {}
    try:
        with open(path_file, MODE_FILE_R,encoding="utf-8") as r_file:
            f_data = r_file.readlines()
            for line in f_data:
                for surname, wage in get_user_wage(line).items():
                    wages_info[surname] = wage
    except IOError as err:
        print(err)

    return wages_info

def report(users:list, average_wage):
    """
    Выводит в консоль фамилии сотрудников, доход которых ниже 20000
    Выводит в консоль средний доход сотрудников
    :return:
    """
    sep = "\n\t\t"
    print(f"Доход ниже {WAGE_THRESHOLD} имеют следующие сотрудники\n\t\t{sep.join(users)}")
    print(f"Средний доход сотрудников: {average_wage:.2f}")

def wrapper():
    """
    Функция-обертка приложения
    :return:
    """
    if len(sys.argv) < 2:
        raise Exception("Отсутствует путь к файлу")

    path_file = sys.argv[1]

    wages_info = get_wages_info(path_file)
    user_before_threshold = [surname for surname, wage in wages_info.items() if wage < WAGE_THRESHOLD]
    average_wage = sum([wage for _, wage in wages_info.items()])/len(wages_info)
    report(user_before_threshold, average_wage)

if __name__ == '__main__':
    wrapper()