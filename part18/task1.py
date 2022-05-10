"""
Напишите программу, которая вычисляет стоимость яблок.
"""

price = float(input('Цена за 1кг яблок: '))
weight = float(input('Вес яблок в кг: '))
print(f'Стоимость {weight}кг яблок: {round(price * weight, 2)}')

