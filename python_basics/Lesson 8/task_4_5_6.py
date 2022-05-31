import hashlib

class ErrorScannerType(Exception):
    def __str__(self):
        return "Допутимые значения параметра 'тип сканера': планшетный, протяжной, слайд-сканнер"


class ErrorScannerColorDepth(Exception):
    def __str__(self):
        return "Допустимые значения параметра 'глубина цвета': внутренняя, внешняя"

class OrgTech:
    """
    Класс, описывающий оргтехнику
    Параметры конструктора класса - параметры, общие для всех видов оргтехники
        1. Количество, поступившее на склад
        2. Цвет
        3. Состояние - новое, б/у
    """
    def __init__(self, name, count, color, status):
        self.count  = count
        self.color  = color
        self.status = status
        self.name   = name

    @staticmethod
    def get_org_tech_info()->dict:
        """
        Формирование словаря, содержащего информацию,
        общую для всех типов оборудование
        :return: словарь с общей информацией о продукте
        """
        try:
            return {
                'name':     input('Наименование товара: '),
                'count':    int(input('Количество товара: ')),
                'color':    input('Цвет товара: '),
                'status':   input('Состояние товара: '),
            }
        except ValueError as err:
            print(err)
            return {}

class Printer(OrgTech):
    """
    Класс, описывающий технику принтер
    В качестве параметров конструктор принимает следующие показатели:

        #### Наследуемые от родительского класса ####
        1. count
        2. color
        3. status

        #### Относящиеся только к принтерам ####
        1. dpi - максимальное количество точек на квадратный дюйм
        2. speed - скорость печати
    """
    def __init__(self, name, count, color, status, dpi, speed):
        super().__init__(name, count, color, status)
        self.dpi    = dpi
        self.speed  = speed

    def __str__(self):
        return  f"name: {self.name}, " \
                f"count: {self.count}," \
                f"color: {self.color}," \
                f"status: {self.status}," \
                f"dpi: {self.dpi}," \
                f"speed: {self.speed}"

class Scanner(OrgTech):
    """
    Класс, описывающий технику сканер
    В качестве параметров конструктор принимает следующие показатели:

        #### Наследуемые от родительского класса ####
        1. count
        2. color
        3. status

        #### Относящиеся только к сканерам ####
        1. scanner_type - тип сканера: планшетный, протяжной, слайд-сканнер
        2. color_depth - глубина цвета: внутрення, внешняя
    """

    valid_types       = ['планшетный', 'протяжной', 'слайд-сканнер']
    valid_color_depth = ['внутренняя', 'внешняя']

    def __init__(self, name, count, color, status, scanner_type, color_depth):
        super().__init__(name, count, color, status)
        self.scanner_type = scanner_type
        self.color_depth = color_depth

    def __str__(self):
        return  f"name: {self.name}, " \
                f"count: {self.count}," \
                f"color: {self.color}," \
                f"status: {self.status}," \
                f"scanner_type: {self.scanner_type}," \
                f"color_depth: {self.color_depth}"

class Xerox(OrgTech):
    """
    Класс, описывающий технику Ксерокс
    В качестве параметров конструктор принимает следующие показатели:

        #### Наследуемые от родительского класса ####
        1. count
        2. color
        3. status

        #### Относящиеся только к ксероксам ####
        1. copies_per_cycle - количество копий в цикле работы
        2. scaling - масштабирование исходного документа (%)
    """
    def __init__(self, name, count, color, status, copies_per_cycle, scaling):
        super().__init__(name, count, color, status)
        self.copies_per_cycle = copies_per_cycle
        self.scaling = scaling

    def __str__(self):
        return  f"name: {self.name}, " \
                f"count: {self.count}," \
                f"color: {self.color}," \
                f"status: {self.status}," \
                f"copies_per_cycle: {self.copies_per_cycle}," \
                f"scaling: {self.scaling}"

class StockOrgTech:
    def __init__(self):
        self.products = {}
        self.count_products = 0

    def __str__(self):
        stock_contents = ''

        for _, product in self.products.items():
            stock_contents += f"{str(product)}\n"

        return stock_contents

    @staticmethod
    def get_printer_info(common_info:dict):
        """
        Формирование словаря, описывающего продукт принтер
        :param common_info: словарь с информацией, общей для всех типов оборудования
        :return:
        """
        try:
            common_info['dpi']   = int(input('Количество точек на квадратный дюйм: '))
            common_info['speed'] = float(input('Скорость печати: '))
        except ValueError:
            raise ValueError

    @staticmethod
    def get_scanner_info(common_info:dict):
        """
        Формирование словаря, описывающего продукт сканер
        :param common_info: словарь с информацией, общей для всех типов оборудования
        :return:
        """
        scanner_type    = input('Тип сканера: ')
        color_depth     = input('Глубина цвета: ')

        if not scanner_type in Scanner.valid_types:
            raise ErrorScannerType
        elif not color_depth in Scanner.valid_color_depth:
            raise  ErrorScannerColorDepth

        common_info['type']         = scanner_type
        common_info['color_depth']  = color_depth

    @staticmethod
    def get_xerox_info(common_info:dict):
        """
        Формирование словаря, описывающего продукт ксерокс
        :param common_info: словарь с информацией, общей для всех типов оборудования
        :return:
        """
        try:
            common_info['copies_per_cycle'] = int(input('Количество копий в цикле: '))
            common_info['scaling']          = int(input('Масштабирование исходного документа (%): '))
        except ValueError:
            raise ValueError

    def create_product(self, type_equipment):
        """
        Создание продукта - оборудования для добавления на склад
        :param type_equipment: тип оборудования
        :return:
        """
        common_info = OrgTech.get_org_tech_info()
        if not common_info:
            return
        try:
            if type_equipment == 'printer':
                self.get_printer_info(common_info)
                return Printer(
                    common_info['name'],
                    common_info['count'],
                    common_info['color'],
                    common_info['status'],
                    common_info['dpi'],
                    common_info['speed']
                )
            elif type_equipment == 'scanner':
                self.get_scanner_info(common_info)
                return Scanner(
                    common_info['name'],
                    common_info['count'],
                    common_info['color'],
                    common_info['status'],
                    common_info['type'],
                    common_info['color_depth']
                )
            elif type_equipment == 'xerox':
                self.get_xerox_info(common_info)
                return Xerox(
                    common_info['name'],
                    common_info['count'],
                    common_info['color'],
                    common_info['status'],
                    common_info['copies_per_cycle'],
                    common_info['scaling']
                )
        except Exception as err:
            print(err)
            return

    def accept_equipment(self, equipment):
        """
        Добавление продукта на склад
        :param equipment: объект одного из классов (Scanner, Xerox, Printer)
        :return:
        """
        obj_hash = hashlib.sha512((equipment.name + equipment.status + equipment.color).encode('utf-8')).hexdigest()

        if not obj_hash in self.products:
            self.products[obj_hash] = equipment
        else:
            self.products[obj_hash].count += equipment.count

    @property
    def count_stock_units(self):
        """
        Считает общее количество единиц оборудование на складе
        :return: общее количество единиц оборудования на складе
        """
        return sum(
            [
                equipment.count for equipment in self.products.values()
            ]
        )

    @property
    def count_names_product(self):
        return len(self.products)

def wrapper():
    """
    Функция-обертка приложения
    :return:
    """
    stock = StockOrgTech()

    printer_canon = stock.create_product('printer')
    if printer_canon:
        stock.accept_equipment(printer_canon)

    printer_canon_2 = stock.create_product('printer')
    if printer_canon_2:
        stock.accept_equipment(printer_canon_2)

    scanner_xiaomi = stock.create_product('scanner')
    if scanner_xiaomi:
        stock.accept_equipment(scanner_xiaomi)

    xerox_nikon = stock.create_product('xerox')
    if xerox_nikon:
        stock.accept_equipment(xerox_nikon)

    print(stock.count_stock_units)
    print(stock.count_names_product)
    print(stock)


if __name__ == '__main__':
    wrapper()