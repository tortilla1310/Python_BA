# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих
# типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
# соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def get_result_a(self):
        return self.size / 6 + 0.5

    def get_result_b(self):
        return self.height * 2 + 0.3

    @property
    def get_result_full(self):
        return str(f'Общая площадь ткани '
                   f'{round(self.size / 6 + 0.5) + round(self.height * 2 + 0.3)}')


class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.result_a = round(self.size / 6 + 0.5)

    def __str__(self):
        return f'Площадь ткани на пальто {self.result_a}'


class Suit(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.result_b = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь ткани на костюм {self.result_b}'


coat = Coat(7, 8)
suit = Suit(3, 9)

print(coat)
print(suit)
print(coat.get_result_a())
print(suit.get_result_b())
print(coat.get_result_full)
print(suit.get_result_full)
