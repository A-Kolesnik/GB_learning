def revert_pairs(users_list):
    """
    Попарно меняет местами элементы списка
    При нечетном количестве элементов в списке, крайний элемент не меняет позицию
    :param users_list: список чисел, введенных пользователем
    :return:
    """
    len_list = len(users_list)
    for ind in range(0, len_list, 2):
        if len_list-1 == ind:
            continue
        users_list[ind], users_list[ind+1] = users_list[ind+1], users_list[ind]