"""
Создает файл
Записывает в него набор псевдослучайных чисел
Считает сумму чисел, считывая их из файла
Выводит результат на экран

* Путь к файлу указать в параметре при запуске
* Также необходимо указать флаг создания файла:
    0 - не создавать (файл создан ранее. Необходимо посчитать только сумму чисел)
    1 - создавать
* Пример команды для запуска скрипта -> task_5.py ./my_file.txt 1
Created: 22.05.2022
Author: A.S.Kolesnik
"""
import sys
from random import randint

MODE_FILE_A = "a"
MODE_FILE_R = "r"

FLAG_NOT_CREATE_FILE = "0"
FLAG_CREATE_FILE = "1"

CNT_NUMS = 10

MIN_NUM = 1
MAX_NUM = 100

def check_flag(in_flag:str):
    """
    Проверяет корректность введенного пользователем флага
    :param in_flag: введенный пользователем флаг
    :return:
    """
    if in_flag != FLAG_CREATE_FILE and in_flag != FLAG_NOT_CREATE_FILE:
        raise TypeError("Возможные значения флага: 0 1")

def create_write_file(path):
    """
    Создает файл
    Генерит список псевжослучайных числовых значений
    Записывает список в файл
    :param path: путь к файлу
    :return:
    """
    nums = []
    for ind in range(CNT_NUMS):
        nums.append(str(randint(MIN_NUM, MAX_NUM)))


    line_to_file = ' '.join(nums)

    try:
        with open(path, MODE_FILE_A) as w_file:
            w_file.write(line_to_file)
    except IOError as err:
        print(err)

def do_file(path):
    """
    Читает содержимое файла
    Считает сумму чисел, записанных в файл
    Выводит сумму
    :param path:
    :return:
    """
    try:
        with open(path, MODE_FILE_R) as r_file:
            f_data = r_file.read()
            nums = [float(num) for num in f_data.split()]
            print(f"Сумма чисел, записанных в файле: {sum(nums)}")
    except Exception as err:
        print(err)


def wrapper():
    """
    Функция-обертка приложения
    :return:
    """

    if len(sys.argv) < 3:
        raise Exception("Указаны не все параметры для запуска")

    path_file = sys.argv[1]
    flag_create_file = sys.argv[2]

    check_flag(flag_create_file)

    if flag_create_file == FLAG_CREATE_FILE:
        create_write_file(path_file)

    do_file(path_file)

if __name__ == '__main__':
    wrapper()