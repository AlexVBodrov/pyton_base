"""1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""
my_f = open('5.1_test.txt', 'w',encoding="utf-8")
line = input('Введите текст \n')+'\n'
while line:
    my_f.writelines(line)
    line = input('Введите текст \n')+'\n'
    if line=="\n":
        break

my_f.close()
my_f = open('5.1_test.txt', 'r',encoding="utf-8")
content = my_f.read()
print(content)
my_f.close()