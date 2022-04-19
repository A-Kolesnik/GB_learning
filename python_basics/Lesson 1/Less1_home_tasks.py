import sys
from random import randint
from random import uniform


def check_str_isdigit(data:str):
    """
    Функция:
        1. Проверяет условия "переданная строка содержит число"
        2. Если условие не выполняется, генерится исключение

    :param data: строка, которую необходимо проверить
    """
    if not data.isdigit():
        raise TypeError('Вводимое значение должно быть целым положительным числом')

def print_variable_info(v_type:str, value):
    """
    Функция выводит в консоль информацию о типе и значении
    переменной, переданной в качестве параметра

    :param v_type: тип передаваемого значения(строка). Необходим только для формирования сообщения, выводимого в консоль
    :param value: значение
    :return:
    """
    print(f"Переменная типа {v_type}\nЗначение: {value}\nТип: {type(value)}")
    print('_' * 20,'\n')

def create_and_print_variables_various_types():
    """
    Функция позволяет создать, инициализировать переменные
    различных встроенных типов python (int, str, float, bool, list, tuple,
    dictionary, set), а также вывести значения созданных переменных в консоль
    """
    variable_int    = randint(0, 100)                           # Случайное целое число
    variable_float  = uniform(2, 150)                           # Случайное вещественное число
    variable_bool   = False                                     # Булево значение (ложь)
    variable_str    = 'Значение строковой переменной'           # Строка
    variable_list   = [randint(0,100) for num in range(10)]     # Список, содержащий 10 случайных целых чисел
                                                                # в диапазоне [0,100]
    variable_tuple  = ('Toyota', 'Subaru', 'Suzuki', 'Toyota')  # кортеж. Два элемента, имеющие одинаковые значения,
                                                                # записаны умышленно, чтобы далее в программе показать
                                                                # эффект преобразования данного кортежа к множеству
    variable_set    = set(variable_tuple)                        # множество, полученное из кортежа variable_tuple
    variable_dict   = {'user_1':
                           {'name': 'Anna',
                            'age': 25,
                            'is_car': True
                            },
                       'user_2':
                           {'name': 'Anton',
                            'age': 20,
                            'is_car': False
                            },
                       }                                        # Словарь из двух элементов. Вложенные элементы - словари

    print_variable_info('int',  variable_int)
    print_variable_info('float', variable_float)
    print_variable_info('bool', variable_bool)
    print_variable_info('str', variable_str)
    print_variable_info('list', variable_list)
    print_variable_info('tuple', variable_tuple)
    print_variable_info('set', variable_set)
    print_variable_info('dict', variable_dict)

def handle_user_input_data():
    """

    Функция обеспечивает работу с информацией, введенной пользователем.
    В частности, запрашивает у пользователя ввод любых данных и
    выводит полученные данные в консоль. Предложения о вводе новых данных
    прекратятся, когда пользователь в качестве данных укажет слово "stop" (нижний регистр)
    """
    status = 'processed'

    while status:
        user_data = input('Ввод: ')
        if user_data == 'stop':
            status = None
            continue
        print(f"Вы ввели => '{user_data}'")
    else:
        print('Ввод пользовательских данных закончен')

def get_time_update_format(sec:int):
    """
    :param sec: время в секундах, введенное пользователем
    :return: результат - время в формате чч:мм:cc
    """
    hour_sec = 3600
    minute_sec = 60

    hours = sec // hour_sec
    minutes = (sec % 3600) // 60
    secs = sec - (hours*3600 + minutes*60)
    return f"{hours}:{minutes}:{secs}"

def user_number_sum(num_original:str, num_str:str, result):
    """
    Функция вызывается рекурсивно:
        1. Формирует новую строку, содержащую число, путем конкатенации строк
        2. Сумирует полученное число с результатои предыдущих итераций

    :param num_original: строка, содержащая число, которое ввел пользователь
    :param num_str: конкатенация строки, которую ввел пользователь с собой же. Количество конкатенаций зависит
                    от количества итераций
    :param result: результат - сумма значение
    :return: результат - сумма значение
    """
    if num_str == num_original*4:
        return result
    result += int(num_str)
    result = user_number_sum(num_original, f"{num_str}{num_original}", result)
    return result

def found_number_day(cnt_day, distance, border_distance):
    """
    :param cnt_day: номер дня пробежки
    :param distance: преодоленная дистанция в этот день
    :param border_distance: пограничная дистанция
    :return: номер дня, в который атлет преодолел пограничную дистанцию
    """
    if distance >= border_distance:
        return cnt_day
    distance = distance + distance*0.1
    cnt_day += 1
    cnt_day = found_number_day(cnt_day, distance, border_distance)
    return cnt_day

def func_task_1():
    print('Часть 1. Создание переменных различных типов и их вывод в консоль\n')
    create_and_print_variables_various_types()

    print('Часть 2. Запрос любой информации у пользователя и вывод ее в консоль')
    handle_user_input_data()

def func_task_2():
    """
    Функция
        1. Запрашивает у пользователя время в секундах
        2. Преобразует к формату чч:мм:сс
        3. Выводит в консоль время в новом формате
    """
    user_time = input('Введите время в секундах: ')

    check_str_isdigit(user_time)

    user_time = int(user_time)
    update_time_format = get_time_update_format(user_time)

    print(f"Время в формате чч:мм:сс => {update_time_format}")

def func_task_3():
    """
    Функция:
        1. Запрашивает у пользователя число n
        2. Вычисляет n + nn + nnn
    """
    sum_result = 0

    user_number = input('Введите число: ')
    check_str_isdigit(user_number)

    sum_result = user_number_sum(user_number, user_number, sum_result)
    print(f"Вы ввели число: {user_number}\nВычисляемое выражение: {user_number} + "
          f"{user_number}{user_number} + {user_number}{user_number}{user_number}\n"
          f"Результат: {sum_result}")

def func_task_4():
    """
    Функция:
        1. Запрашивает у пользователя число.
        2. Проверяет условие  "введенное число - целое и положительное"
        3. Выполняет поиск самой большой цифры в числе
        4. Результат выводит в консоль
    """

    user_number = input("Введите число: ")
    check_str_isdigit(user_number)

    max_number = int(user_number[0])
    len_user_number = len(user_number)
    len_user_number_save = len_user_number

    while len_user_number_save > 0:
        id_symbol = len_user_number - len_user_number_save
        if int(user_number[id_symbol]) > max_number:
            max_number = int(user_number[id_symbol])
        len_user_number_save -= 1

    print(f"В числе {user_number} самая большая цифра {max_number}")

def func_task_5_6():
    """
    Функция:
        1. Запрашивает у пользователя два показателя: выручка, издержки, количество сотрудников
        2. Отображает сообщение в консоль о состоянии дел в фирме: прибыль/убыток, рентабельности фирмы,
           прибыли в расчете на одного сотрудника фирмы
        *** Условимся, что вводимые значения должны быть целыми положительными числами
    :return:
    """
    revenue = input("Введите значение показателя 'выручка': ")
    check_str_isdigit(revenue)

    costs = input("Введите значение показателя 'издержки': ")
    check_str_isdigit(costs)

    count_persons = input('Введите количество сотрудников в фирме: ')
    check_str_isdigit(count_persons)

    revenue = int(revenue)
    costs = int(costs)

    status = None
    profitability = None
    profit_per_person = None

    if revenue > costs:
        status = 'Прибыльное дело'
        profitability = (revenue - costs) / revenue

        check_str_isdigit(count_persons)
        count_persons = int(count_persons)
        profit_per_person = (revenue - costs) / count_persons
    elif revenue < costs:
        status = 'Необходимо пересмотреть подход. Дело в убытке'
        profitability = 'фирма не рентабельна'
        profit_per_person = '-'
    else:
        status = 'Поднажмите. Пока в нуле'
        profitability = 'фирма не рентабельна'
        profit_per_person = '-'

    print(f"\n\t\tОтчет о компании\nВыручка: {revenue}\nИздержки: {costs}\nЧисленность: {count_persons} сотрудников\n"
          f"Финансовый результат: {status}\nРентабельность: {profitability}\n"
          f"Прибыль в расчете на одного сотрудника: {profit_per_person}")

def func_task_7():
    """
    Функция:
        1. Запрашивает у пользователя два значения: расстояние в километрах(в первый день пробежки), расстояние,
            для которого необходимо определить день, в который атлет его осилит.
        2. Вызывает функцию, которая расчитывает расстояние для каждого из дней пробежки
    :return:
    """

    begin_distance = input('Укажите дистанцию, которую атлет преодолел в первый день: ')
    check_str_isdigit(begin_distance)

    border_distance = input('Укажите пограничную дистанцию: ')
    check_str_isdigit(border_distance)

    begin_distance = int(begin_distance)
    border_distance = int(border_distance)

    result_cnt_day = 1
    result_cnt_day = found_number_day(result_cnt_day, begin_distance, border_distance)

    print(f"Спортсмен достиг результата - 'не менее {border_distance} км' на {result_cnt_day} день")


def main():
    """
    В зависимости от переданного аргумента при запуске программы
    вызывается функция, соответствующая аргументу.
    Аргумент - номер задания с префиксом 'task_'
        task_1   - задание 1
        task_2   - задание 2
        task_3   - задание 3
        task_4   - задание 4
        task_5_6 - задание 5,6
        task_7   - задание 7

    :return:
    """
    if len(sys.argv) < 2:
        print('В качестве аргумента при запуске программы необходимо указать номер(-а) задания')
        return

    for task_id in range(1, len(sys.argv)):
        if sys.argv[task_id] == 'task_1':
            print('\nЗадание 1')
            func_task_1()
        elif sys.argv[task_id] == 'task_2':
            print('\nЗадание 2')
            func_task_2()
        elif sys.argv[task_id] == 'task_3':
            print('\nЗадание 3')
            func_task_3()
        elif sys.argv[task_id] == 'task_4':
            print('\nЗадание 4')
            func_task_4()
        elif sys.argv[task_id] == 'task_5_6':
            print('\nЗадание 5, 6')
            func_task_5_6()
        elif sys.argv[task_id] == 'task_7':
            print('\nЗадание 7')
            func_task_7()

if __name__ == '__main__':
    main()