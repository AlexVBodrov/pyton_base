'''
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
 значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
 Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
'''

s_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
s_list2 = [_ for num, _ in enumerate(s_list) if s_list[num] > s_list[num-1] and num > 0]
print(f'Исходный список {s_list}')
print(f'Новый список - Результат: {s_list2}')