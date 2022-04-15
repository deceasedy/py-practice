"""
Напишите программу, вычисляющую скорость, с которой бегун пробежал дистанцию.
"""

# Ввод нужных переменных
distance = int(input("Введите дистанцию в метрах: "))
time = float(input("Введите время (минуты.секунды): "))

# Перевод времени в секунды и подсчет скорости
minutes = int(time)
seconds = (time - minutes) * 100 + (minutes * 60)
speed = distance / seconds * 3.6

# Вывод скорости округленной до сотых
print(f"Вы бежали со скоростью: {round(speed, 2)} км/ч")