# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
name = input('Введите имя')
s_name = input('Введите фамилию')
year_bith = input('Введите год рождения')
city = input('Введиет город проживания')
email = input('Введите ваш Email')
Tel = input('Введите номет телефона')

def print_1line(name, s_name, year_bith, city, email, Tel):
    print(name, s_name, year_bith, city, email, Tel)

print_1line (name=name, s_name = s_name, year_bith = year_bith, city = city, email= email, Tel = email)