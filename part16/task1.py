"""
Напишите программу, которая выводит на экран наименьший элемент введенного пользователем массива целых чисел.
"""

array = input('Введите массив целых чисел: ').split()
for i in range(len(array)): array[i] = int(array[i])
print(f'Наименьшее число: {min(array)}')
