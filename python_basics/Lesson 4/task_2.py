stat_list_numbers = [
    300,
    2,
    12,
    44,
    1,
    1,
    4,
    10,
    7,
    1,
    78,
    123,
    55,
]

def report(result_list):
    """
    Отчет о результате работы программы
    :param result_list: сформированный список
    :return:
    """
    print(
        "Список из элементов, каждый из которых больше совего рпедыдущего элемента в исходном списке: \n"
        f"{result_list}"
    )

def do_list(orig_list):
    """
    Формирование списка из элементов, каждый из которых больше своего предыдущего в исходном списке
    Используется генератор списков
    :param orig_list: исходный список
    :return:
    """
    result_list = [orig_list[ind] for ind in range(1, len(orig_list)) if orig_list[ind] > orig_list[ind-1]]
    report(result_list)

if __name__ == "__main__":
    do_list(stat_list_numbers.copy())