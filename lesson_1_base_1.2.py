# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
seconds = int(input('Введите время в секундах : '))
a=seconds//3600
b=seconds%3600//60
c=seconds%3600%60
d="{}:{}:{}".format(a, b, c) # ['{} часов {} минут {} секунд']
print(d)