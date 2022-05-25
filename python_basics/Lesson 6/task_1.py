"""
Приложение СВЕТОФОР
Имитация работы устройства - светофор
Светофор описан с использованием класса TrafficLight
Приложение после запуска НЕ останавливает свою работу самостоятельно
Остановка пользователем

Светофор имеет 3 состояния - красный, желтый, зеленый

Author: Kolesnik A.S.
Created: 24.05.2022
"""
import time
import os


'Количество секунд работы каждого состояния светофора'

SECS_RED    = 7
SECS_YELLOW = 2
SECS_GREEN  = 10

'Описание состояний светофора'

COLOR_RED       = 'Красный'
COLOR_YELLOW    = 'Желтый'
COLOR_GREEN     = 'Зеленый'

SET_COLORS = [
    COLOR_RED,
    COLOR_YELLOW,
    COLOR_GREEN
]

class TrafficLight:

    def __init__(self, set_colors:list):
        self.set_colors = set_colors
        self.secs_colors = [SECS_RED,SECS_YELLOW,SECS_GREEN]
        self.__color = None

    def running(self):
        """
        Запускает работу светофора
        Изменяет состояние светофора через предустановленные промежутки времени
        :return:
        """
        while True:
            for cid in range(len(self.set_colors)):
                self.__color = self.set_colors[cid]
                print(f"\r{self.__color}", end='')
                time.sleep(self.secs_colors[cid])


def wrapper():
    """
    Функция-обертка для приложения
    :return:
    """
    traffic_light = TrafficLight(SET_COLORS)
    traffic_light.running()

if __name__ == '__main__':
    wrapper()