MAX_SPEED_TOWN = 60
MAX_SPEED_WORK = 40

class Car:
    def __init__(self, color, name, is_police):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        """
        Функция оповещает о начале движения автомобиля
        :return:
        """
        print(f"Автомобиль {self.name} начал движение")

    def stop(self):
        """
        Функция оповещает о прекращении движения автомобиля
        :return:
        """
        print(f"Автомобиль {self.name} прекратил движение")

    def turn(self, direction):
        """
        Функция указывет направление движения автомобиля
        :param direction:
        :return:
        """
        print(f"Направление движения автомобиля {self.name}: {direction}")

    def show_speed(self):
        """
        Функция отображает текущую скорость автомобиля
        :return:
        """
        print(f"Текущая скорость автомобиля {self.name} {self.speed} км/ч")

    def change_speed(self, speed):
        """
        Функция изменяет скорость автомобиля
        :param speed: новая скорость
        :return:
        """
        self.speed = speed

class TownCar(Car):
    def __init__(self, color, name, is_police):
        super().__init__(color, name, is_police)

    def show_speed(self):
        """
        Функция отображает текущую скорость автомобиля
        Если скорость превышена, отображается предупреждение
        :return:
        """
        print(f"Текущая скорость автомобиля {self.name} {self.speed} км/ч")
        if self.speed > MAX_SPEED_TOWN:
            print(f"Предупреждение !!! Скорость превышена !!! Максимально допустимая скорость {MAX_SPEED_TOWN} км/ч")

class SportCar(Car):
    def __init__(self, color, name, is_police):
        super().__init__(color, name, is_police)


class WorkCar(Car):
    def __init__(self, color, name, is_police):
        super().__init__(color, name, is_police)

    def show_speed(self):
        """
        Функция отображает текущую скорость автомобиля
        Если скорость превышена, отображается предупреждение
        :return:
        """
        print(f"Текущая скорость автомобиля {self.name} {self.speed} км/ч")
        if self.speed > MAX_SPEED_WORK:
            print(f"Предупреждение !!! Скорость превышена !!! Максимально допустимая скорость {MAX_SPEED_WORK} км/ч")

class PoliceCar(Car):
    def __init__(self, color, name, is_police):
        super().__init__(color, name, is_police)



def wrapper():
    """
    Функция-обертка для приложения
    :return:
    """

    town_car = TownCar("Белый", "Toyota", False)
    print(f"Характеристики автомобиля\n\tцвет: {town_car.color}\n\tмарка: {town_car.name}\n\t"
          f"полицейский: {town_car.is_police}")
    town_car.go()
    town_car.change_speed(70)
    town_car.show_speed()
    town_car.turn("Право")
    town_car.stop()

    print('\n\n\n')
    work_car = WorkCar("Белый", "Isuzu", False)
    print(f"Характеристики автомобиля\n\tцвет: {work_car.color}\n\tмарка: {work_car.name}\n\t"
          f"полицейский: {work_car.is_police}")
    work_car.go()
    work_car.change_speed(40)
    work_car.show_speed()
    work_car.turn("Прямо")
    work_car.stop()

    print('\n\n\n')
    sport_car = SportCar("Черный", "Subaru", False)
    print(f"Характеристики автомобиля\n\tцвет: {sport_car.color}\n\tмарка: {sport_car.name}\n\t"
          f"полицейский: {sport_car.is_police}")
    sport_car.go()
    sport_car.change_speed(170)
    sport_car.show_speed()
    sport_car.turn("Прямо")
    sport_car.stop()

    print('\n\n\n')
    police_car = PoliceCar("Белый", "Honda", True)
    print(f"Характеристики автомобиля\n\tцвет: {police_car.color}\n\tмарка: {police_car.name}\n\t"
          f"полицейский: {police_car.is_police}")
    police_car.go()
    police_car.change_speed(170)
    police_car.show_speed()
    police_car.turn("Прямо")
    police_car.stop()

if __name__ == '__main__':
    wrapper()