"""
Напишите программу, которая удаляет из строки, введенной пользователем, все пробелы и знаки препинания.
"""

symbols = '.,?! ;-:'
text = input('Введите строку: ')
toprint = ''
for i in text:
    toprint += i if i not in symbols else ''
print(f'Ваша строка без пробелов и знаков препинания: "{toprint}"')

