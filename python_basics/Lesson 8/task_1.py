from abc import ABC, abstractmethod

class ErrorDateFormat(Exception):
    def __str__(self):
        return "Invalid date format. Required format -> day-month-year"

class InvalidDay(Exception):
    def __str__(self):
        return "Invalid date value"

class InvalidMonth(Exception):
    def __str__(self):
        return "Invalid month value"

class InvalidYear(Exception):
    def __str__(self):
        return "Invalid year value"

class RedefineDateTime(ABC):
    """
    Абстрактный класс дата/время
    """
    @abstractmethod
    def convert(self):
        """
        Преобразование компонентов даты и времени
        :return:
        """
        pass

    @classmethod
    @abstractmethod
    def check_valid(cls, date_components:dict):
        """
        Проверка на валидность компонентов даты и времени
        :param date_components: компоненты введенных пользователем данных
        :return:
        """
        pass

class Date(RedefineDateTime):
    """
    Класс-наследник RedefineDateTime
    Класс, описывающий дату
    """
    valid_date = [num_day for num_day in range(1,32)]
    valid_month = [num_month for num_month in range(1,13)]

    def __init__(self, date:str):
        self.date = date
        self.date_components = None

    def decompose_date(self):
        """
        Преобразование даты к списку, словарю,
        содержащему день, месяц, год
        :return:
        """
        day_month_year = self.date.split('-')
        if not len(day_month_year) == 3:
            raise ErrorDateFormat()
        else:
            self.date_components = {
                'day'   : day_month_year[0],
                'month' : day_month_year[1],
                'year'  : day_month_year[2],
            }

    def convert(self):
        try:
            self.decompose_date()
        except ErrorDateFormat as err:
            print(err)
            return

    @staticmethod
    def check_num_day(day:str, valid_nums:list):
        """
        Проверка на валидность значение дня
        :param day: день -> значение, введенное пользователем
        :param valid_nums: валидные значения дней
        :return:
        """
        try:
            int(day)
            if not int(day) in valid_nums:
                raise InvalidDay()
        except Exception as err:
            raise InvalidDay()


    @staticmethod
    def check_num_month(month: str, valid_nums: list):
        """
        Проверка на валидность значение месяца
        :param month: месяц -> значение, введенное пользователем
        :param valid_nums: валидные значения месяцев
        :return:
        """
        try:
            int(month)
            if not int(month) in valid_nums:
                raise InvalidMonth()
        except Exception as err:
            raise InvalidMonth()

    @staticmethod
    def check_num_year(year: str):
        """
        Проверка валидности значения года
        :param year: год -> значение, введенное пользователем
        :return:
        """
        try:
            int(year)
        except Exception as err:
            raise InvalidYear()

    @classmethod
    def check_valid(cls, date_components:dict):
        try:
            cls.check_num_day(date_components['day'], cls.valid_date)
            cls.check_num_month(date_components['month'], cls.valid_month)
            cls.check_num_year(date_components['year'])
        except Exception as err:
            print(err)

class DateTimeFactory:
    """
    Класс предназначени для реализации паттерна - фабричный метод
    Приложение работает только с форматом данных - дата -> дд-мм-гг
    Интерфейс подразумевает обработку данных других форматов - пока заглушки
    """
    @staticmethod
    def create(value, datetime_type):
        """
        Создание объекта дата/время
        :param value: значение в строковом формате
        :param datetime_type: тип объекта : время, дата или дата+время
        :return:
        """
        if datetime_type == 'date':
            return Date(value)
        elif datetime_type == 'time':
            pass
        elif datetime_type == 'datetime':
            pass
        else:
            pass

def wrapper():
    """
    Фнкция-обертка приложения
    :return:
    """
    user_date = input('Введите дату в формате дд-мм-гг: ')
    date = DateTimeFactory().create(user_date, 'date')
    date.convert()

    if not date.date_components:
        return

    """
    !!!!!!!!!!!!!!
    Илья, обрати здесь особое внимание плиз
    Правильно ли обращаться к методу , к которому применен декоратор @classmethod
    через экземпляр класса ????????
    !!!!!!!!!!!!!!
    """
    date.check_valid(date.date_components)

if __name__ == '__main__':
    wrapper()