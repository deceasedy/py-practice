"""
Попробуйте программно смоделировать разговор людей. Всего есть 5 людей. Каждый человек имеет имя (строку) и возраст (число). Возраст каждого человека генерируется рандомно из диапазона от 20 до 40, а имена выбираются из следующего списка: Александр, Андрей, Анастасия, Ирина, Наталья, Павел, Роман, Светлана, Сергей, Татьяна.

Любой человек способен выполнять два действия:
   здороваться с другим человеком;
   рассказывать о себе.

Люди делятся на 3 типа (разные классы):
   Тип №1: Формалисты. Здороваются со всеми следующим образом: Здравствуйте, <имя>!, где <имя> — это имя человека, с которым он здоровается.
   Тип №2: Неформалы. Со всеми здороваются: Привет, <имя>!.
   Тип №3: Реалисты. Если возраст собеседника меньше/равен или собеседник старше не более, чем на 5 лет, то здороваются следующим образом: Привет, <имя>!, в противном случае — Здравствуйте, <имя>!.

В программной реализации приветствие должно быть реализовано как полиморфный метод, принимающий человека в качестве параметра и возвращающий строку.

Рассказ о человеке является строкой формата "Меня зовут Александр, мой возраст 21 лет и я неформал" (вместо Александр используется имя любого другого человека из вышеприведенного списка, вместо 21 возраст этого человека, вместо неформал может быть формалист, либо реалист). Как видите у людей с грамматикой не всё в порядке, и они говорят лет после любого числа — непорядок, это нужно обязательно исправить.

Программа должна показать информацию обо всех людях. Затем все люди должны поздороваться друг с другом в следующем порядке: первый здоровается со вторым, затем второй с первым, а затем первый с третьим, третий с первым и т.д. Например:

Александр: Привет, Роман!
Роман: Здравствуйте, Александр!
Александр: Привет, Ирина!
Ирина: Привет, Александр!
"""

import random

names = ['Александр', 'Андрей', 'Анастасия', 'Наталья', 'Ирина', 'Павел', 'Роман', 'Светлана', 'Сергей', 'Татьяна']
types = ['формалист', 'неформал', 'реалист']

class Human:
    def __init__(self, name, age, htype):
        self.name = name
        self.age = age
        self.htype = htype

    def about(self):
        print(f'Меня зовут {self.name}, мой возраст {self.age} и я {self.htype}')

    def say(self, to):
        if self.htype == 'формалист':
            return(f'Здравствуй, {to.name}')
        elif self.htype == 'неформал':
            return(f'Привет, {to.name}')
        else:
            if self.age + 5> to.age:
                return(f'Привет, {to.name}')
            else:
                return(f'Здравствуй, {to.name}')


humans = []
for i in range(5):
    humans.append(Human(random.choice(names), random.randint(20, 40), random.choice(types)))

for i in humans:
    i.about()
print()

for i in range(5):
    for j in range(i + 1, 5):
        print(f'{humans[i].name}: {humans[i].say(humans[j])}')
        print(f'{humans[j].name}: {humans[j].say(humans[i])}')

