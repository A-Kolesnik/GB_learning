class Stationery:
    """
    Класс концелярская принадлежность
    """
    def __init__(self, title):
        self.title = title

    def draw(self):
        """
        Отрисовка
        :return:
        """
        print(f"Запуск отрисовки ({self.title})")

class Pen(Stationery):
    """
    Класс ручка - дочерний от Stationery
    """
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        """
        Отрисовка
        :return:
        """
        print("Экземпляр класса Pen метод draw")

class Pencil(Stationery):
    """
    Класс карандаш - дочерний от Stationery
    """
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        """
        Отрисовка
        :return:
        """
        print("Экземпляр класса Pencil метод draw")

class Handle(Stationery):
    """
    Класс маркер - дочерний от Stationery
    """
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        """
        Отрисовка
        :return:
        """
        print("Экземпляр класса Handle метод draw")

def wrapper():
    """
    Функция-обертка приложения
    :return:
    """
    pen = Pen("Ручка")
    pen.draw()

    pencil = Pencil("Карандаш")
    pencil.draw()

    handle = Handle("Маркер")
    handle.draw()

if __name__ == '__main__':
    wrapper()