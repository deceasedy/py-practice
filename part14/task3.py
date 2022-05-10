"""
Напишите программу, которая считывает целые числа, которые рандомно генерируются в диапазоне от 1 до 72. 
Для каждого считанного числа ваша программа должна вывести строку, содержащую соответствующее количество звёздочек. 
Например, если ваша программа считала число 7, то она должна вывести 7 звёздочек: *******.
"""

import random

array = [random.randint(1, 72) for i in range(10)]
for i in array: print(f'{i}:', '*' * i)
