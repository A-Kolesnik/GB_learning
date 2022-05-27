import sys

import src.home_task_1 as ht1
import src.home_task_2 as ht2
import src.home_task_3 as ht3
import src.home_task_4 as ht4
import src.home_task_5 as ht5
import src.home_task_6 as ht6

def task_1():
    input_list = [
        45399,
        'Второй элемент в списке',
        (8, 9, 'обучение'),
        {
            'friend_1':
                {
                    'name': 'Victor',
                    'age': 25,
                    'city': 'Krasnodar',
                },
            'friend_2':
                {
                    'name': 'Xsenia',
                    'age': 24,
                    'city': 'Krasnodar',
                },
        },
        {4, 4, 5, 6, 6, 3,3},
        98.8888999,
    ]
    ht1.report_element_types(input_list)

def task_2():
    users_input = input('Введите набор чисел в формате 1,2,3,... : ')
    users_list = [int(num) for num in users_input.split(',') if num.isdigit()]
    print(f'Ваш список: {users_list}')

    ht2.revert_pairs(users_list)
    print(f'Преобразованный список: {users_list}')

def task_3():
    users_month = input('Укажите номер месяца: ')
    season_list = ht3.get_season_from_list(users_month)
    season_dict = ht3.get_season_from_dict(users_month)
    print(f"Указанный месяц относится в времени года =>\n\tИспользуя list: {season_list}"
          f"\n\tИспользуя dict: {season_dict}")

def task_4():
    ht4.print_each_word(input('Введите строку из нескольких слов, разделенных пробелом: '))

def task_5():
    ht5.get_rating()

def task_6():
    products_info = ht6.generate_list_products()
    report = ht6.analitic_report(products_info)
    print(report)

def main():
    if len(sys.argv) < 2:
        print('В качестве аргумента при запуске программы необходимо указать номер(-а) задания')
        return

    for task_id in range(1, len(sys.argv)):
        if sys.argv[task_id] == 'task_1':
            print('\nЗадание 1')
            task_1()
        elif sys.argv[task_id] == 'task_2':
            print('\nЗадание 2')
            task_2()
        elif sys.argv[task_id] == 'task_3':
            print('\nЗадание 3')
            task_3()
        elif sys.argv[task_id] == 'task_4':
            print('\nЗадание 4')
            task_4()
        elif sys.argv[task_id] == 'task_5':
            print('\nЗадание 5')
            task_5()
        elif sys.argv[task_id] == 'task_6':
            print('\nЗадание 6')
            task_6()


if __name__ == '__main__':
    main()