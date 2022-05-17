import sys

'Количество параметров, требуемое для запуска скрипта'
num_require_param = 3

def report(wage):
    """
    Печать информации о заработной плате сотрудника
    :param wage: заработная плата
    :return:
    """
    print(
        f"Зарплата сотрудника: {wage}"
    )


def calc_wages(production, rate, prize):
    """
    Расчет заработной платны сотрудника
    :param production: выработка в часах
    :param rate: ставка в час
    :param prize: премия
    :return:
    """

    wage = (production*rate) + prize
    report(wage)

def wrappers_interface(args):
    """
    Обертка для функции вычисления заработной платы
    Производит операции с переданными при запуске скрипта параметрами
    :param args: параметры, переданные пользователем
    :return:
    """
    if len(args) != num_require_param + 1:
        raise Exception(f"Требуемое количество параметров для запуска: {num_require_param}\n"
                        f"\t1. Выработка в часах\n\t2. Ставка в час\n\t3. Премия\n")

    try:
        args = [float(arg) for arg in args[1:]]
    except Exception:
        raise Exception("Указанные в качестве параметров значения должны быть числовыми")
    calc_wages(*args)

if __name__ == '__main__':
    wrappers_interface(sys.argv)