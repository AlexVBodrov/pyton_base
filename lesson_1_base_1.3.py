# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

set_n = input('Введите число n : ')
'''
1 вариант
n = int(set_n)
nn = set_n+set_n
nn = int(nn)
nnn = set_n+set_n+set_n
nnn = int(nnn)
print(n+nn+nnn)
'''
'''
2. вариант
t = int(set_n)+int(set_n+set_n)+ int(set_n+set_n+set_n)
print(t)
'''
# 3. вариант в 2 строки
print(int(set_n)+int(set_n+set_n)+ int(set_n+set_n+set_n))
