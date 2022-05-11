"""
Пользователь вводит целое число N. Создайте массив из N целых чисел (числа генерируются рандомно). 
Определите индекс наибольшего элемента массива.
"""

import random

n = int(input('Введите размер массива: '))
array = []
for i in range(n):
    array.append(random.randint(0, 100))

print(array)
print(f'Индекс максимального элемента: {array.index(max(array))}')
