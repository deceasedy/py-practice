"""
Напишите программу, которая генерирует последовательность из 10 случайных чисел в диапазоне от 1 до 10,
выводит эти числа на экран и вычисляет их среднее арифметическое.
"""

import random

nums = [random.randint(0, 10) for i in range(10)]
print(f'{nums}\n{sum(nums) / len(nums)}')

