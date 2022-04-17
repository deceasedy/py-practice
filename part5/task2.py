"""
Напишите программу, которая выводит на экран таблицу стоимости, например, яблок в диапазоне от 100 г до 1 кг с шагом 100 г.
"""

# Фиксированное количество нулей после запятой
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

price = float(input("Введите цену яблок за 1кг.: "))
print("Вес\tСтоимость\n(г)\t (грн.)")
for i in range(1, 11):
    print(f"{i * 100}\t{toFixed(price * (i / 10), 2)}")