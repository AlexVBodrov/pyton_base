# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:
    title = ''
    def draw(self):
        print('Запуск отрисовки.')
class Pen(Stationery):
    title = 'Pen'
    def draw(self):
        print(f'Создать надпить инструметом {self.title}')

class Pencil(Stationery):
    title = 'Pencil'
    def draw(self):
        print(f'Создать чертеж инструметом {self.title}')

class Handle(Stationery):
    title = 'Handle'
    def draw(self):
        print(f'Зарисовать область инструметом {self.title}')

stationery = Stationery()
stationery.draw()
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
