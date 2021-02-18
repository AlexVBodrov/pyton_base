# 3. Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {"wage": 2000, "bonus": 1000}

class Position(Worker):
    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        return full_name

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        return total_income

loader = Position()
loader.name = 'Bob'
loader.surname = 'Marly'
loader.position = 'loader'
print(loader.name)
print(loader.surname)
print(loader.position)
print(f'full name : {loader.get_full_name()}')
print(f'total_income : {loader.get_total_income()}')