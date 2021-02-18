"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
class Car:
    speed = 0
    color = 'black'
    name = 'auto'
    is_police = False

    def go(self, speed):
        self.speed = speed
        print(f'Машина {self.name} поехала')
        self.show_speed()


    def stop(self):
        print(f'Машина {self.name} остановилась')
        self.speed = 0
        self.show_speed()


    def turn(self, direction="",speed=20):
        print(f'Машина {self.name} повернула {direction}')
        self.speed = speed
        self.show_speed()


    def show_speed(self):
        print(f'Cкорость машины {self.name} сейчас = {self.speed}')


class TownCar(Car):
    speed = 60

    def show_speed(self):
        print(f'Cкорость машины {self.name} сейчас = {self.speed}')
        if self.speed > 60:
            print('Превышение скорости !!!')


class WorkCar(Car):
    speed = 40
    color = 'grey'
    name = 'Work_auto'
    is_police = False
    def show_speed(self):
        print(f'Cкорость сейчас = {self.speed}')
        if self.speed > 40:
            print('Превышение скорости !!!')


class SportCar(Car):
    speed = 250
    color = 'Red-white-black'
    name = 'SportAuto'

class PoliceCar(Car):
    speed = 150
    color = 'blue-white-black'
    name = 'Police'
    is_police = True


mazda = TownCar()
mazda.name = 'Mazda'
mazda.speed = 150
mazda.go(100)
mazda.stop()
mazda.turn(direction='на право', speed=45)

ford = PoliceCar()
ford.go(150)
ford.turn(direction='За машиной превысившей скорость', speed=100)

kamaz = WorkCar()
kamaz.name = "Kamaz"
kamaz.go(speed=50)

lotos = SportCar()
lotos.name = 'Lotos'
lotos.go(200)






