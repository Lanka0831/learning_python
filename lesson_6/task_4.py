# Задание 4
# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.


class Car:
    def __init__(self, name, speed, color, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"Машина {self.name} поехала"

    def stop(self):
        return f"Машина {self.name} остановилась"

    def turn(self, derection):
        return f"{self.name} повернула {derection}"

    def show_speed(self):
        return f"Скорость {self.name} равна {self.speed}"


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return "Превышение скорости"
        else:
            return f"Скорость {self.name} равна {self.speed}"


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return "Превышение скорости"
        else:
            return f"Скорость {self.name} равна {self.speed}"


class PoliceCar(Car):
    pass


town = TownCar('Skoda', 50, 'white', False)
print(f'1:\n{town.go()}\n{town.show_speed()}\n{town.turn("налево")}\n{town.turn("направо")}\n{town.stop()}')

sport = SportCar('Ferrari', 120, 'red', False)
print(f'2:\n{sport.go()}\n{sport.show_speed()}\n{sport.turn("на лево")}\n{sport.stop()}')

work = WorkCar('Ford', 40, '', False)
print(f'3:\n{work.go()}\n{work.show_speed()}\n{work.turn("на право")}\n{work.stop()}')

police = PoliceCar('BMW', 80, 'blue', True)
print(f'4:\n{police.go()}\n{police.show_speed()}\n{police.turn("на право")}\n{police.stop()}')
