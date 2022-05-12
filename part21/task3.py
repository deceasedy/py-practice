"""
Напишите генератор паролей. Составьте три уровня сложности генерации паролей (включая их длину) и спрашивайте
у пользователя, какой уровень сложности ему нужен. Проявите свою изобретательность: надежные пароли должны состоять
из сочетания строчных букв, прописных букв, цифр и символов. Пароли должны генерироваться случайным образом каждый
раз, когда пользователь запрашивает новый пароль.
"""

import random

hard = [i for i in 'qwertyuiop[]asdfghjkl;zxcvbnm,./1234567890-=_,./<>!@#$%^&*()_+']
normal = [i for i in 'qwertyuiopasdfghjklzxcvbnm1234567890']
easy = [i for i in 'qwertyuiopasdfghjklzxcvbnm']
num = [i for i in '1234567890']

difficulties = [num, normal, easy, hard]
ask = int(input('Выберите сложность (0 - 3): '))

for i in range(4 * (ask + 1)): print(end = random.choice(difficulties[ask]))
print()

