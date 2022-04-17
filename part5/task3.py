"""
Напишите программу-таймер, которая по истечении заданного промежутка времени (который вводит пользователь) выдает текстовый сигнал.
"""

from time import sleep

def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format)
        sleep(1)
        num_of_secs -= 1
        
    print('Время истекло!')
        
countdown(int(input("Введите количество секунд: ")))