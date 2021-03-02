# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
class Storage:
    """
    class Storage
    класс, описывающий склад
    get objekts
    keep objekts
    info objekts
    output objekts
    """
    name = 'The_Storage'
    address = 'Москва, 5-я Магистральная улица, д.6, стр. 1'

    width = 100
    length = 1000
    area = width * length
    length_of_row_space = 2
    count_of_row = length / length_of_row_space / 2
    count_of_stack = count_of_row * 4
    height_оf_stack = 3
    max_volume_Storage = int(count_of_stack * height_оf_stack)  # count_of_shelf_space =  max_volume_Storage = 3000 item

    count_of_fill_shelf_space = 0

    def get_goods(self, quantity_goods=0, name_Office_equipment='name_Office_equipment', model='model'):
        if count_of_fill_shelf_space < max_volume_Storage:
            count_of_fill_shelf_space = count_of_fill_shelf_space + quantity_goods
        else:
            print('Storage => FULL !!!')

        """
        add info objekts
        add структура данных
        """
        return count_of_fill_shelf_space

    def keep_goods(self):
        print('Охрана на постах')
        print('Сигнализация влючена')
        print('Пожарные системы на готове')
        print('Системы регулировки влажности и температуры, вентиляция активны')
        print('Уровни загазованности, влажности и температуры в норме')
        print('Все нормы складирования и хранения соблюденны')
        print(f'На хранение {count_of_fill_shelf_space} единиц товаров')

    def to_info_of_goods(self):
        print('выдать инфо о товарах на складе')
        pass

    def output_goods(self):
        print('Выдать товары со склада')
        pass


class Office_equipment:
    def __init__(self, brand='manufacturer', name_equipment='принтер', model='model',
                 year_production=2020, guarantee=12, country_of_manufacture='China'):
        self.brand = brand
        self.name_equipment = name_equipment
        self.model = model
        self.year_production = year_production
        self.guarantee = guarantee
        self.country_of_manufacture = country_of_manufacture

    def __str__(self):
        return f"{self.brand} {self.name_equipment} {self.model} {self.year_production}"

    def get_data(self):
        print('Получить входные данные')
        pass

    def create_document(self):
        return f'Создать документ'
        pass


class Printer(Office_equipment):
    def to_print(self, smth='smth'):
        return f'to print {smth}'

    pass


class Scanner(Office_equipment):
    def to_scan(self, smth='smth'):
        return f'to scan {smth}'

    pass


class Xerox(Office_equipment):
    def to_copier(self, smth='smth'):
        return f'to copier {smth}'

    pass


a2d2 = Printer()
print(a2d2)
print(a2d2.to_print())
print(a2d2.create_document())
a2d2.get_data()
