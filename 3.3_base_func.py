# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
a = int(input('a : '))
b = int(input('b : '))
c = int(input('c : '))

def my_func(a, b, c):
    all_arg = [a, b, c]
    min_1 = min(all_arg)
    all_arg.remove(min_1)
    print(sum(all_arg))

my_func(a, b, c)