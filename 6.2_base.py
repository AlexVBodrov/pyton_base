#2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т
class Road:
    def __init__(self,length=0, width=0):
        self._length_Road = length
        self._width_Road = width

    def calculation_mass_of_asphalt(self, weight_asphalt = 25, high_ground_Road = 0.05):
        mass_of_asphalt = self._length_Road*self._width_Road*weight_asphalt*high_ground_Road
        return mass_of_asphalt
m1 = Road(100,5)

print(f'масса асфальта - {m1.calculation_mass_of_asphalt()} кг')
