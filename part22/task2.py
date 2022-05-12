"""
Напишите программу, которая спрашивает у пользователя, сколько чисел Фибоначчи нужно сгенерировать, 
а затем генерирует их.
"""

def fib(term):
   if term <= 1: return (term)
   return (fib(term-1) + fib(term-2))

numbers = []
num = int(input('Сколько чисел Фибоначчи сгенерировать: '))
for i in range(num): numbers.append(fib(i))

print('Список чисел Фибоначчи до', num, '-', numbers)
