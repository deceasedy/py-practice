"""
Игра «Быки и коровы». Правила:
   программа генерирует случайным образом 4-значное число;
   пользователю предлагают угадать сгенерированное программой число;
   за каждую угаданную пользователем цифру, стоящую на правильной позиции, он получает «корову»;
   за каждую угаданную пользователем цифру, стоящую на неправильной позиции, он получает «быка»;
   после каждого предположения пользователю должно выводиться количество «коров» и «быков», которые он заработал;
   игра окончена тогда, когда пользователь угадал все цифры.
"""

import random

num = 0
pc = random.randint(1000, 9999)
while True:
    num = int(input('Ваше число: '))
    bools = 0
    for i in str(num):
        bools += str(pc).count(i)
    
    cows = 0
    for i in range(4):
        if str(num)[i] == str(pc)[i]: cows += 1

    print(f'{cows} коров, {bools} быков.')
    if num == pc: break
print(f'Вы угадали число {pc}!')


