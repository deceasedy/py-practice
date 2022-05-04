"""
Рейтинг бакалавра заочного отделения при поступлении в магистратуру определяется средним баллом диплома, 
умноженным на коэффициент стажа работы по специальности, который равен: нет стажа — 1, меньше 2 лет — 13, от 2 — 16.
Напишите программу расчета рейтинга студента при заданном среднем балле диплома (от 3 до 5) 
и выведите сообщение о приеме в магистратуру (при проходном балле равном 45).
"""

def confirmed(grade, years):
    return grade * coefficient(years) >= 45

def coefficient(years):
    if years == 0: return 0
    return 13 if years <= 2 else 16

grade = int(input("Введите ваш средний балл диплома (1 - 5): "))
experience = int(input("Введите ваш рабочий стаж (в годах): "))

print(f"Вы {'' if confirmed(grade, experience) else 'не '}приняты.")