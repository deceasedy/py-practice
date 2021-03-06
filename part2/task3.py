"""
Напишите программу, реализующую игру «Угадай число». 
Компьютер загадывает число от 0 до 999 (используйте генерацию случайных чисел), а пользователь угадывает его. 
На каждом шаге угадывающий делает предположение, а задумавший число — сообщает, 
сколько цифр из числа угаданы и сколько из угаданных цифр занимают правильные позиции в числе. 
Например, если задумано число 725 и выдвинуто предположение, что задумано число 523, то угаданы две цифры (5 и 2), и одна из них занимает верную позицию.
"""

import random

# Функция сравнения введенного числа и загаданного компьютером
def compare():
    # Перевод чисел в списки
    pnum = [int(a) for a in playerNumber]
    cnum = [int(a) for a in str(computerNumber)]

    # Сравнение списков для нахождения количества совпадений
    samenum = len(set(pnum) & set(cnum))

    # Сравнение позиций и значений цифр
    samepos = 0
    for i in range(len(pnum)):
        if pnum[i] == cnum[i]:
            samepos += 1

    # Вывод нужной информации
    print(f"Угадано: {samenum}, на своих местах: {samepos}")
    if samepos == 3:
        print(f"Вы угадали число: {computerNumber}!!!")
    
    return samepos == 3

print("Компьютер загадал трехзначное число. Вы должны его отгадать. \nПосле очередного числа вам будет сообщено, сколько цифр угадано и сколько из них находится на своих местах.")
playerNumber = 100
computerNumber = random.randint(100, 999)
guessed = False

while not guessed:
    playerNumber = input("Ваше число: ")
    guessed = compare()