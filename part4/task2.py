"""
Напишите программу, которая вычисляет среднее арифметическое последовательности дробных чисел, вводимых с клавиатуры. 
После ввода пользователем последнего числа программа должна вывести минимальное и максимальное числа из последовательности. 
Количество чисел последовательности вводит пользователь.
"""

print("Введите последовательность чисел (через пробел): ", end='')
array = list(map(float, input().split()))

print(f"Среднее арифметическое: {round(sum(array) / len(array), 2)}")
print(f"Минимальное число: {min(array)}")
print(f"Максимальное число: {max(array)}")