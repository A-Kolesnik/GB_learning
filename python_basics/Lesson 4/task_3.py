
start_range     = 20
stop_range      = 240

multiply_num_20 = 20
multiply_num_21 = 21

def report(nums):
    """
    Выводит в консоль результат работы
    :param nums:
    :return:
    """
    print(
        f"В диапазоне [{start_range}, {stop_range}] список чисел кратных {multiply_num_20} или {multiply_num_21}\n"
        f"                                   ||\n"
        f"                                   ||\n"
        f"                                   ||\n"
        f"                                   ||\n"
        f"                                  \\\\//\n"
        f"                                   \\/\n"
        f"{nums}"
    )


def get_multiplicity():
    """
    Формирует список чисел из диапазона [20,240]
    которые кратны 20 или 21
    :return: сформированный список
    """
    nums = [num for num in range(start_range, stop_range+1) if num%multiply_num_20 == 0 or num%multiply_num_21 == 0]
    return nums

if __name__ == '__main__':
    m_nums = get_multiplicity()
    report(m_nums)
