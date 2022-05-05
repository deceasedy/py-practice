"""
Создайте класс с именем Student, содержащую следующие поля:
   Name — ФИО;
   Year — курс;
   Rating — успеваемость (массив из пяти элементов).

Напишите программу, выполняющую:
   Ввод с клавиатуры данных в массив students, состоящий из 10 объектов типа Student;
   Вывод на экран записей списка студентов, средний бал которых превышает общий средний бал;
   Если таких студентов нет — выведите соответствующее сообщение.
"""


class Student:
    def __init__(self, name, year, rating):
        self.name = name
        self.year = year
        self.rating = list(map(int, rating.split()))
        self.average = sum(self.rating) / len(self.rating)

students = []

for i in range(int(input('Сколько записей вы хотите ввести: '))):
    print('Студент', i + 1)
    students.append(Student(input('  > ФИО: '), int(input('  > Год: ')), input('  > Успеваемость (5 чисел через пробел): ')))

average = sum([i.average for i in students]) / len([i.average for i in students])
print('\n\n')

for i in students:
    if i.average > average:
        print(f'Студент {students.index(i) + 1}')
        print(f'  > ФИО: {i.name}\n  > Год: {i.year}\n  > Средний бал: {i.average}')

if sum(map(lambda x : x > average, [i.average for i in students])) == 0:
    print('Подходящий студентов нет.')
