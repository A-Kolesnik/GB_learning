original_list = [
    2,
    2,
    2,
    7,
    23,
    1,
    44,
    44,
    3,
    2,
    10,
    7,
    4,
    11,
]

def report(orig_list, nums):
    """
    Выводит в консоль результат работы
    :param nums:
    :return:
    """
    print(
        f"Исходный список: {orig_list}\n"
        f"Числа, не имеющие повторений в исходном списке\n"
        f"         ||\n"
        f"         ||\n"
        f"         ||\n"
        f"         ||\n"
        f"        \\\\//\n"
        f"         \\/\n"
        f"{nums}"
    )

def do_list(orig_list):
    """
    Формирование списка из неповторяющихся в исходом списке чисел
    :param orig_list: исходный список
    :return:
    """
    result_list = [item for item in orig_list if orig_list.count(item)==1]
    report(orig_list, result_list)

if __name__ == '__main__':
    do_list(original_list.copy())