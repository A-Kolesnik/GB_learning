from abc import ABC, abstractmethod

CONST_DIVISION = 6.5
CONST_MULTIPLE = 2
CONST_ADDING_COAT = 0.5
CONST_ADDING_COSTUME = 0.3


class Clothing(ABC):
    """
    Абстрактный базовый класс Одежда
    Дочерний от метакласса ABCMeta
    """
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def calc_consumption(self, size_param):
        """
        Расчет общего расхода ткани
        """

    @property
    def name(self):
        """
        функция getter
        :return: наименование одежды одного из типа
        """
        return self._name

    @name.setter
    def name(self, name_clothing):
        """
        Функция setter
        :param name_clothing: новое наименование одежды
        :return:
        """
        self._name = name_clothing


class Coat(Clothing):
    """
    Класс пальто - дочерний от Clothing
    """
    def __init__(self, name):
        super().__init__(name)

    def calc_consumption(self, size):
        """
        Вычисляет общий расход ткани
        :return:
        """
        return size / CONST_DIVISION + CONST_ADDING_COAT


class Costume(Clothing):
    def __init__(self, name):
        super().__init__(name)

    def calc_consumption(self, height):
        return height * CONST_MULTIPLE + CONST_ADDING_COSTUME


def wrapper():
    my_coat = Coat('Mustang')
    my_costume = Costume('GJ')

    print(f"{my_coat.calc_consumption(52):.1f}")
    print(f"{my_costume.calc_consumption(198):.1f}")

    # Демонстрация работы функции setter
    my_coat.name = "Handerson"
    print(f'New name coat: {my_coat.name}')

if __name__ == '__main__':
    wrapper()

