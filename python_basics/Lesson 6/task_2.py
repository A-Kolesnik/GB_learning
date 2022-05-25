"""
Приложение выполняет расчет массы асфальта, необходимого для ремонта дороги
Параметры дороги (длина, ширина) указывает пользователь в ПАРАМЕТРАХ СКРИПТА ПРИ ЗАПУСКЕ
Ex. .../task_2.py length width

Author: Kolesnik A.S.
Created: 24.05.2022
"""
import sys

MASS_ON_CENT    = 25
THICKNESS       = 5

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width  = width
        self._mass   = None

    def calc_mass(self):
        """
        Расчитвает массу асфальта
        :return:
        """
        self._mass = (self._length * self._width * MASS_ON_CENT * THICKNESS)/1000

    def report(self):
        """
        Вывод результата в консоль
        :return:
        """
        print(
            f"Для покрытия {self._length} метров(-а) дороги шириной {self._width} "
            f"метра(-ов) необходимо {self._mass} тонн асфальта"
        )

def wrapper():
    """
    Функция-обертка приложения
    :return:
    """
    if len(sys.argv) < 3:
        raise Exception("Указаны не все параметры. Для запуска необходимы длина и ширина дороги")

    try:
        road_info = Road(float(sys.argv[1]), float(sys.argv[2]))
        road_info.calc_mass()
        road_info.report()
        del road_info
    except TypeError as err:
        print(err)

if __name__ == '__main__':
    wrapper()
