'''1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
'''

class TrafficLight:
    def __init__(self):
        self.__color_TrafficLight = ('(0) - red', '(0) - yellow', '(0) - green')
        self.__stop_TrafficLight = False
    def running(self):
        import time
        def delay(delay):
            r = 0
            while not r == delay:
                r += 1
                time.sleep(1)


        while self.__stop_TrafficLight == False:
            print("\033[1m\033[31m{}\033[0m".format(self.__color_TrafficLight[0]))
            delay(7)
            print("\033[1m\033[33m{}\033[0m".format(self.__color_TrafficLight[1]))
            delay(2)
            print("\033[1m\033[32m{}\033[0m".format(self.__color_TrafficLight[2]))
            delay(7)


a = TrafficLight()
print(type(a))
print(isinstance(a,TrafficLight))
a.running()


