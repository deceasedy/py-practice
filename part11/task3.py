"""
Известно, что сейф открывается при правильном вводе кода из 3-x цифр в диапазоне от 0 до 9. 
Задайте код и затем откройте сейф, используя метод перебора с помощью цикла for.
"""

code = input('Введите трехзначное число: ')

attempts = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            attempts += 1
            if str(i) + str(j) + str(k) == code:
                print(f'Потребовалось {attempts} попыток.')

# В чем смысл этого перебора? Можно было проверить все числа от 0 до 999