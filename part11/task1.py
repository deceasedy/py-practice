"""
Напишите программу пересчета веса из фунтов в килограммы (1 фунт = 0.453 кг).
"""

pounds = float(input('Введите вес в фунтах: '))
print(f'{pounds} фт = {round(pounds * 0.453592, 3)} кг')