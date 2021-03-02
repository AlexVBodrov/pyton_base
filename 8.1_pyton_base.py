# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:

    def __init__(self, day_month_year):

        self.day_month_year = str(day_month_year)
        date_parts =day_month_year.split('-')
        self.day = date_parts[0]
        self.month = date_parts[1]
        self.year = date_parts[2]
        self.data_validator(int(self.day), int(self.month), int(self.year))


    @classmethod
    def extract_number_data(cls, day_month_year):
        day = int(day_month_year[0:2])
        month = int(day_month_year[day_month_year.find('-')+1:day_month_year.rfind('-')])
        year = int(day_month_year[-4:])
        cls.data_validator(day, month, year)
        return day, month, year


    @staticmethod
    def data_validator(day, month, year):

        if 1 <= day <= 30 and month in [4,6,9]:
            True
        elif 1 <= day <= 31 and month not in [4, 6, 9]:
            True
        elif month==2:
            True

        else:
            print(f'Ошибка, число дня должно быть соответствующее месяцу, ваше {day:02}')
            return


        if month==2:
            if year % 4 != 0 or (year % 100 == 0 and y % 400 != 0):
                if day >= 1 and day <= 28:
                    True
                else:
                    print(
                        f'Ошибка, если месяц {month:02}, число дня должно быть 1 до 28 соответствующее месяцу, ваше {day:02}')
                    return
            else:
                if day >= 1 and day <= 29:
                    True
                else:
                    print(
                        f'Ошибка, если месяц {month:02} и год {year} високостный, число дня должно быть от 1 до 29 соответствующее месяцу, ваше {day:02}')
                    return

        elif 1 <= month <= 12:
            True
        else:
            print(f'Ошибка, число месяца должно быть от 1 до 12, ваше {month:02}')
            return



d1= Data('2-2-2021')
Data.extract_number_data('12-12-1211')
d1.data_validator(10,10,2000)
d2 = Data('30-2-2020')



