def report_element_types(input_list:list):
    """
    Принимает список и выводит в консоль информацтю о списке(Размер, значения элементов, типы каждого элемента)
    :param input_list: список, содержащий переменные разных типов
    :return:
    """
    in_list_types = [f"\tЗначение элемента: {element}\n" \
                     f"\tТип: {type(element)}\n\n" for element in input_list]
    print(f"\n\t\tИнформация о списке\n"
          f"Размер: {len(input_list)}\n"
          f"Содержимое: {input_list}\n"
          f"Информация о типах:\n")
    print ("".join(in_list_types))
