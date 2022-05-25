class Worker:
    """
    Класс работник
    Экземпляр класса содержит аттрибуты
        имя сотрудника
        фамилия сотрудника
        ддолжность сотрудника
        доход сотрудника
    """
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            'wage': wage,
            'bonus': bonus,
        }

class Position(Worker):
    """
    Класс-наследник класса Worker
    """
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        """
        Формирует строку, содержащую полное имя сотрудника
        :return:
        """
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        """
        Вычисляет доход сотрудника с учетом премии
        :return:
        """
        try:
            self._income['wage']    = float(self._income['wage'])
            self._income['bonus']   = float(self._income['bonus'])
        except TypeError as err:
            print(err)
        return self._income['wage'] + self._income['bonus']

def report(fullname:str, wage_plus_bonus:float):
    """
    Выводит отчет о полном имени и доходе сотрудника
    :param fullname: полное имя сотрудника
    :param wage_plus_bonus: доход сотрудника
    :return:
    """
    print(f"Сотрудник: {fullname}\nДоход: {wage_plus_bonus}")

def wrapper():
    """
    Функция-обертка приложения
    :return:
    """
    position_1 = Position('Andrey', 'Ivanov', 'Manager', 85000, 2000)
    position_2 = Position('Fedor', 'Sharov', 'Data Scientiest', 124000, 87000)

    report(position_1.get_full_name(),position_1.get_total_income())
    report(position_2.get_full_name(), position_2.get_total_income())

if __name__ == '__main__':
    wrapper()
