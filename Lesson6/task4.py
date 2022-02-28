# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f' скорость {self.name} {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f' скорость {self.name} {self.speed}')
        if self.speed > 60:
            return f'Превышение скорости'
        else:
            return f'все хорошо, вы в рамках скоростного режима'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f' скорость {self.name} {self.speed}')
        if self.speed > 40:
            return f'Превышение скорости'
        else:
            return f'все хорошо, вы в рамках скоростного режима'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return 'это полиция'
        else:
            return 'машина не из участка'


Smart_car = TownCar(60, 'white', 'Smart Car', 'False')
BMW = SportCar(120, 'red', 'BMW', 'False')
Volkswagen = WorkCar(80, 'black', 'Volkswagen', 'False')
Volvo = PoliceCar(100, 'white', 'Volvo', 'True')

print(BMW.go())
print(Smart_car.show_speed())
print(Volkswagen.stop())
print(f'когда {BMW.turn_right()}, {Volvo.go()} \n')
print(f' {BMW.go()} со сокростью {BMW.show_speed()}')
print(Volkswagen.show_speed())
print(f' {Volvo.name} {Volvo.color}')
print(f' {Volvo.name} полицейская машина?{Volvo.is_police}')
print(f' {BMW.name} полицеская машина?{BMW.is_police}')
