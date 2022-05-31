class RedefineComplex:
    def __init__(self, real_a, real_b):
        self.real_a = real_a
        self.real_b = real_b

    def __add__(self, complex_two):
        return RedefineComplex(
            self.real_a + complex_two.real_a,
            self.real_b + complex_two.real_b
        )

    def __mul__(self, complex_two):
        return RedefineComplex(
            (self.real_a*complex_two.real_a - self.real_b*complex_two.real_b),
            (self.real_a*complex_two.real_b + self.real_b*complex_two.real_a)
        )

    def __str__(self):
        return f"{self.real_a} + {self.real_b}i"


def wrapper():
    """
    Функция-обертка приложения
    :return:
    """
    complex_num_1 = RedefineComplex(10, 5)
    complex_num_2 = RedefineComplex(8, 9)

    print(
        f"({str(complex_num_1)}) + ({str(complex_num_2)}) = {str(complex_num_1 + complex_num_2)}"
    )

    print(
        f"({str(complex_num_1)}) * ({str(complex_num_2)}) = {str(complex_num_1 * complex_num_2)}"
    )


if __name__ == '__main__':
    wrapper()