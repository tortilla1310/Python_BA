# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны
# быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()),
# \деление (truediv()). Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
# и целочисленное (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух
# клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
# этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
# ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный
# метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
# *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
# *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.

class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        new_cell_number = self.number + other.number
        new_cell = Cell(new_cell_number)
        return new_cell

    def __sub__(self, other):
        if self.number > other.number:

            new_cell_number = self.number - other.number
            new_cell = Cell(new_cell_number)
            return new_cell
        else:
            raise Exception("Ошибка")

    def __mul__(self, other):
        new_cell_number = self.number * other.number
        new_cell = Cell(new_cell_number)
        return new_cell

    def __truediv__(self, other):
        new_cell_number = self.number // other.number
        new_cell = Cell(new_cell_number)
        return new_cell

    def make_order(self, number_per_row):
        full_rows_amount = self.number // number_per_row
        residual_amount = self.number % number_per_row

        full_row_string = "*"*number_per_row + "\n"
        full_row_final_string = full_row_string * full_rows_amount

        final_string = full_row_final_string + "*"*residual_amount
        return final_string


a = Cell(1700)
b = Cell(12)
print((a+b).number)
print((a-b).number)
print((a*b).number)
print((a/b).number)

print(a.make_order(500))
