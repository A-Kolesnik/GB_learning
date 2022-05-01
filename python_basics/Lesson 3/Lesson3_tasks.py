import sys

import src.home_task_1 as ht1
import src.home_task_2 as ht2
import src.home_task_3 as ht3
import src.home_task_4 as ht4
import src.home_task_5 as ht5
import src.home_task_6 as ht6
import src.home_task_7 as ht7

def task_1():
    num1, num2 = ht1.get_users_nums()
    res_dev = ht1.division_nums(num1, num2)
    print(f"Результат деления: {res_dev}")

def task_2():
    user_info = ht2.get_users_info()
    ht2.print_users_info(**user_info)

def task_3():
    num1, num2, num3 = 8, 9, 3
    res_bigger_num = ht3.my_func(num1, num2, num3)
    print(f"Сумма наибольших 2 чисел из {num1, num2, num3} : {res_bigger_num}")


def task_4():
    x = 2
    y = -8
    print(f"{x} в степени {y}\n"
          f"Результат при использовании оператора **: {ht4.calculate_variant_1(x, y)}\n"
          f"Результат при использовании собственной реализации: {ht4.calculate_variant_2(x, y)}")


def task_5():
    ht5.sum_users_number()

def task_6():
    users_word = ht6.get_users_word()
    changed_word = ht6.int_func(users_word)
    print(f"{users_word} => {changed_word}")

def task_7():
    users_words = ht7.get_users_words()
    changed_words = [ht6.int_func(word) for word in users_words]
    print(' '.join(changed_words))

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
        elif sys.argv[task_id] == 'task_7':
            print('\nЗадание 7')
            task_7()


if __name__ == '__main__':
    main()