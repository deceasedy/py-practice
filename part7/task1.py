"""
Напишите программу, которая выводит на экран работающие «электронные часы», которые работают в течение, например, 180 секунд.
"""

from time import sleep

def countdown(num_of_secs):
    i = 0
    while i < num_of_secs:
        m, s = divmod(i, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format)
        sleep(1)
        i += 1
        
    print('Время истекло!')
        
countdown(int(input("Введите количество секунд: ")))