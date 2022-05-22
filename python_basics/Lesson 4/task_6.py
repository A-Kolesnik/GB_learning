from itertools import count, cycle

const_stop      = 100
start_val_part1 = 1
stop_val_part1 = const_stop + start_val_part1

count_repeat_part2 = 10

list_part2 = [
    'Toyota',
    'Suzuki',
    'Dodge',
    'Nissan',
]

def part_1():
    """
    Итератор, генерирующий целые числа, начиная с указанного
    Каждое число печатает в консоль
    Условие окончания: достижение значения (начальное значение + const_step)
    :return:
    """
    global start_val_part1
    it = count(start_val_part1)

    print("Итератор, генерирующий целые числа, начиная с указанного")

    while start_val_part1 < stop_val_part1:
        print(next(it), end=' | ')
        start_val_part1 += 1

def part_2():
    """
    Итератор, повторяющий элементы некоторого списка, определенного заранее
    :return:
    """
    global count_repeat_part2
    it = cycle(list_part2)

    print("\n\nИтератор, повторяющий элементы некоторого списка, определенного заранее")
    while count_repeat_part2:
        print(next(it))
        count_repeat_part2 -= 1


def wrapper_program():
    """
    Обвязка программы
    :return:
    """
    part_1()
    part_2()


if __name__ == '__main__':
    wrapper_program()