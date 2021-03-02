# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class Storage:
    """
    class Storage
    класс, описывающий склад
    get objekts
    keep objekts
    info objekts
    output objekts
    """

    def __init__(self, name_Storage='The_Storage_Office_equipment',
                 address='Москва, 5-я Магистральная улица, д.6, стр. 1'):
        self.name_Storage = name_Storage
        self.address = address
        """
        width = 100
        length = 1000

        self.area = width * length
        # count_of_shelf_space =  max_volume_Storage = int(count_of_stack * height_оf_stack)
        length_of_row_space = 2
        count_of_row = length / length_of_row_space / 2
        count_of_stack = count_of_row * 4
        height_оf_stack = 3
        # max_volume_Storage = 3000 item
        """
        self.max_volume_Storage = 3000
        self.count_of_fill_shelf_space = 0
        self.goods = []

    def add_goods(self, item: "OfficeEquipment", quantity_of_item):
        if not isinstance(item, Office_equipment):
            raise ValueError(f"Вы пытаетесь добавить на склад не оргтехнику")
        if not isinstance(quantity_of_item, int):
            raise ValueError(f"Кол-во должно быть положительным числом")
        elif not quantity_of_item > 0:
            raise ValueError(f"Кол-во должно быть положительным числом")

            #return


        self.count_of_fill_shelf_space = self.count_of_fill_shelf_space + quantity_of_item
        if self.count_of_fill_shelf_space < self.max_volume_Storage:

            self.goods.append({item: quantity_of_item})
            print(f'На склад {self.name_Storage} добавленно {quantity_of_item} товаров')


        else:
            print("can't add_goods Storage => is FULL !!!")
            self.count_of_fill_shelf_space = self.count_of_fill_shelf_space - quantity_of_item

    def keep_goods(self):
        print('Охрана на постах')
        print('Сигнализация, датчики движения, камеры наблюдения включены')
        print('Пожарные системы на готове')
        print('Системы регулировки влажности и температуры, вентиляция активны')
        print('Уровни загазованности, влажности и температуры в норме')
        print('Все нормы складирования и хранения соблюденны')
        print(f'На хранение {self.count_of_fill_shelf_space} единиц товаров')

    def info_goods(self):
        print(f'На хранение {self.count_of_fill_shelf_space} единиц товаров')
        print(self.goods)

    def output_goods(self, id_index, name_Department, item: "OfficeEquipment", del_quantity_of_item):

        if not isinstance(del_quantity_of_item, int) and not isinstance(id_index, int):
            raise ValueError(f"значение должно быть положительным числом")
        elif not del_quantity_of_item > 0:
            raise ValueError(f"Кол-во должно быть положительным числом")

        name_item_transh = self.goods[id_index].copy()
        key = item
        name_item_transh[key] = del_quantity_of_item

        self.count_of_fill_shelf_space = self.count_of_fill_shelf_space - del_quantity_of_item
        output_goods_list = [name_item_transh]

        rest_goods_in_item = self.goods[id_index][key] - name_item_transh[key]
        if rest_goods_in_item == 0:
            del self.goods[id_index]
        elif rest_goods_in_item < 0:
            print(f"can't output_goods more than {self.goods[id_index][key]}")
            self.count_of_fill_shelf_space = self.count_of_fill_shelf_space + del_quantity_of_item
        else:
            self.goods[id_index][key]=rest_goods_in_item

        print(f'Передать товары: \n{output_goods_list} -\nсо склада {self.name_Storage}  в => {name_Department} отдел')


class Office_equipment:
    def __init__(self, brand, model, year_production=2020, guarantee=12, country_of_manufacture='China'):
        self.brand = brand
        self.model = model
        self.year_production = year_production
        self.guarantee = guarantee
        self.country_of_manufacture = country_of_manufacture

    def __str__(self):
        return f"{self.brand} {self.type_equipment} {self.model}, год выпуска {self.year_production}, " \
               f"гарантия {self.guarantee} месяцев, страна производитель: {self.country_of_manufacture}"

    def get_data(self):
        print('Получить входные данные')
        pass

    def create_document(self):
        return f'Создать документ'
        pass


class Printer(Office_equipment):
    type_equipment = 'Printer'

    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        return f"{self.brand} {self.type_equipment} {self.model}, год выпуска {self.year_production}, " \
               f"гарантия {self.guarantee} месяцев, страна производитель: {self.country_of_manufacture}"

    def __repr__(self):
        return f"{self.brand} {self.type_equipment} {self.model}, год выпуска {self.year_production}, " \
               f"гарантия {self.guarantee} месяцев, страна производитель: {self.country_of_manufacture}"

    def to_print(self, smth='smth'):
        return f'to print {smth}'


class Scanner(Office_equipment):
    type_equipment = 'Scanner'

    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        return f"{self.brand} {self.type_equipment} {self.model}, год выпуска {self.year_production}, " \
               f"гарантия {self.guarantee} месяцев, страна производитель: {self.country_of_manufacture}"

    def __repr__(self):
        return f"{self.brand} {self.type_equipment} {self.model}, год выпуска {self.year_production}, " \
               f"гарантия {self.guarantee} месяцев, страна производитель: {self.country_of_manufacture}"

    def to_scan(self, smth='smth'):
        return f'to scan {smth}'


class Xerox(Office_equipment):
    type_equipment = 'Xerox'

    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        return f"{self.brand} {self.type_equipment} {self.model}, год выпуска {self.year_production}, " \
               f"гарантия {self.guarantee} месяцев, страна производитель: {self.country_of_manufacture}"

    def __repr__(self):
        return f"{self.brand} {self.type_equipment} {self.model}, год выпуска {self.year_production}, " \
               f"гарантия {self.guarantee} месяцев, страна производитель: {self.country_of_manufacture}"

    def to_copier(self, smth='smth'):
        return f'to copier {smth}'


printer_1 = Printer("Samsung", 'iq200')
#print(printer_1)
xerox_2 = Xerox("LG", 'qwerty2020')
storage = Storage()

storage.add_goods(printer_1, 340)
storage.add_goods(xerox_2, 100)
#storage.info_goods()

storage.info_goods()
storage.output_goods(0, 'IT', printer_1, 50)
storage.info_goods()
storage.output_goods(1, 'Marketing', xerox_2, 100)

