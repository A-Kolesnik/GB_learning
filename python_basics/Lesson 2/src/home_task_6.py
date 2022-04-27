def check_digit(control_str:str):
    """
    Принимает строку. Если содержимое строки не является числом,
    генерится исключение
    :param control_str: строка, которую необходимо проверить на содержимое (только число или нет)
    :return:
    """
    if not control_str.isdigit():
        raise TypeError('Вводимое значение должно быть числом')

def check_digit_value(control_num):
    """
    Принимает число. Если число отрицательное или не является целым, генерируется исключение.
    :param control_num: число, которое необходимо проверить на соответствие условию "положительное целое"
    :return:
    """
    if control_num < 0 or not 'int' in str(type(control_num)):
        raise ValueError('Вводимое значение должно быть целым положительным числом')

def generate_list_products():
    """
    Запрашивает у пользователя информацию о товарах, которые
    необходимо добавить. На основе полученных данных формирует
    список кортежей, содержащих порядковый номер товара,
    начиная с 1 и словарь с информацией о товарах.
    :return: список кортежей, содержащих информацию о товарах
    """
    count_products = input('Укажите количество товаров, которое необходимо добавить: ')
    check_digit(count_products)

    count_products = int(count_products)
    check_digit_value(count_products)

    print('Заполните информацию о добавляемых товарах\n'
          'Формат ввода информация о отдельном товаре => название,цена,количество,единица измерения')

    added_products = []
    save_orig_count_products = count_products

    while count_products:
        product_info = input(f'Товар {save_orig_count_products - count_products + 1}: ')
        product_info = product_info.split(',')
        product_info = list(map(str.strip, product_info))
        if len(product_info) < 4:
            print('Указана не вся информация о товаре. Товар не добавлен')
            continue

        if not product_info[1].isdigit():
            raise TypeError('Парметр \'цена\' должен быть числовым значением')

        if not product_info[2].isdigit():
            raise TypeError('Парметр \'количество\' должен быть числовым значением')

        added_products.append(
            (
                save_orig_count_products - count_products + 1,
                {
                    'Название': product_info[0],
                    'Цена': product_info[1],
                    'Количество': product_info[2],
                    'Ед.': product_info[3],
                },
            )
        )
        count_products-=1

    return added_products

def analitic_report(products:list):
    """
    Принимает список товаров, которые указал пользователь.
    Формирует словарь => ключ - наименование характеристики товара,
    значение - массив значений, соответствующих данному ключу у всех товаров

    :param products: список товаров с информацией о них,
    которую указал пользователь
    :return: сформированный словарь
    """
    if not products:
        return None

    names = [key for key, value in products[0][1].items()]
    report = {characteristic: [] for characteristic in names}

    for product_info in products:
        num, info = product_info
        for name in names:
            report[name].append(info[name])

    return report