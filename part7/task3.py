"""
Напишите программу учета оценок студентов. Для этого создайте текстовый файл с именем input_data.txt,
содержащий список из 10 студентов и их оценки по трем предметам: математика, физика и информатика.

Содержимое файла:
   в первой строке находится общее количество студентов;
   в каждой последующей строке находится ФИО студента и три целых числа (оценки);
   данные в строке разделены пробелами, а оценки варьируются в диапазоне от 1 до 5.

Затем создайте класс, с помощью которого вы будете считывать данные из файла. На экран выведите ФИО студентов с оценками и их средним баллом.
"""

import os

class Student:
    def __init__(self, fullname, math, physics, informatics):
        self.fullname = fullname
        self.math = math
        self.physics = physics
        self.informatics = informatics[0:-1]
        self.average = round((int(math) + int(physics) + int(informatics)) / 3, 1)

    def info(self):
        print(f"| {self.fullname[0] + ' ' + self.fullname[1] + ' ' + self.fullname[2]:40}", end = '')
        print('|     ', self.math, '     |      ', self.physics, '     |      ', self.informatics, '      |        ', self.average, '       |')
        print('-------------------------------------------------------------------------------------------------------------')


students = []
splitted = []
with open(os.getcwd() + "\part7\students.txt", encoding = 'utf-8', mode = 'r') as f:
    for line in f.readlines():
        splitted = line.split(' ')
        students.append(Student(splitted[0:3], splitted[3], splitted[4], splitted[5]))

print('-------------------------------------------------------------------------------------------------------------')
print('|               FULLNAME                  |     MATH    |    PHYSICS   |  INFORMATICS  |       AVERAGE      |')
print('-------------------------------------------------------------------------------------------------------------')
for i in students:
    i.info()