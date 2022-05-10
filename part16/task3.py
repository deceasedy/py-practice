"""
На первом курсе M = 40 студентов. Каждый из студентов в понедельник получает оценку по программированию, 
во вторник — оценку по математике, в среду — по физике в пределах от 2 до 5 каждая. Всего в году N = 35 недель,
когда студенты учатся. Лучшим считается студент, который наибольшее количество недель продержался без троек
(т.е. получал не ниже 4). Сформируйте три целочисленных массива нужного размера. Задайте оценки с помощью 
генерации случайных чисел. Найдите лучшего студента.
"""


import random

class Student:
    def __init__(self):
        self.it = [random.randint(2, 5) for i in range(35)]
        self.math = [random.randint(2, 5) for i in range(35)]
        self.physics = [random.randint(2, 5) for i in range(35)]
        self.highest = highest(self)

def highest(student):
    highest = 0
    count = 0
    for i in range(35):
        if student.it[i] > 3 and student.math[i] > 3 and student.physics[i] > 3: 
            count += 1
            if count > highest: highest = count
        else: count = 0
    return highest


students = []

for i in range(40):
    students.append(Student())
    print(f'\n{i}>>\n{students[i].it}\n{students[i].math}\n{students[i].physics}\nhighest: {students[i].highest}')
best = students[0]
for i in range(40):
    if best.highest < students[i].highest: best = students[i]

print(f'\n\n--\nbest>>\n{best.it}\n{best.math}\n{best.physics}\nhighest: {best.highest}')





