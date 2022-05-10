"""Возьмите любое слово, например, «корова». Используя генерацию рандомных чисел, переставьте буквы этого слова
в рандомном порядке. Делайте это до тех пор, пока полученное слово не совпадет с начальным словом.
Используя массив, укажите при перестановке букв их индексы. Программа должна корректно работать с любым словом.
"""

import random

word = input('Введите слово: ')
splitted = [i for i in word]
attempt = []
text = generated = ''
count = 1

while True:
    attempt = [i for i in range(len(word))]
    random.shuffle(attempt)
    for i in attempt:
        generated += word[i]
        text += str(i)
    print(f'{count}. {text} > {generated}')
    if generated == word: break
    generated = text = ''
    count += 1
