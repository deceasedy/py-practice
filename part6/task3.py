"""
Напишите программу, которая содержит текущую информацию о десяти заявках на авиабилеты. Каждая заявка должна иметь:
   пункт назначения;
   номер рейса;
   ФИО пассажира;
   желаемую дату вылета.

Программа должна обеспечивать:
   хранение всех заявок в виде списка;
   добавление и удаление заявок;
   вывод всех заявок.
   """

import datetime

class Ticket:
    def __init__(self, destination, race, fullname, date):
        self.destination = destination
        self.race = race
        self.fullname = fullname
        self.date = date

    def info(self):
        print(f"\nПункт назначения: {self.destination}")
        print(f"Номер рейса: {self.race}")
        print(f"ФИО пассажира: {self.fullname}")
        print(f"Дата вылета: {self.date}")

def tickets():
    for i in alltickets:
        i.info()

alltickets = []
alltickets.append(Ticket("Пункт 1", 1, "ФИО 1", datetime.date(1990, 12, 24)))
alltickets.append(Ticket("Пункт 2", 2, "ФИО 2", datetime.date(2011, 5, 30)))

tickets()

# alltickets.append(Ticket(destination, race, fullname, datetime.date(date))) - добавление заявки
# alltickets.pop(id) - удаление заявки
# tickets() - вывод всех заявок