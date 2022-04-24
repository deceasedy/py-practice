"""
Пользователь вводит натуральное четырехзначное число. Выясните, является ли оно палиндромом (читается одинаково как слева направо, так и справа налево).
"""

def isPallindrome(number):
    number = [i for i in str(number)]
    for i in range(len(number)):
        if number[i] != number[-i - 1]: return False
    return True

number = int(input('Введите число: '))
print(number, 'не' if not isPallindrome(number) else '-', 'палиндром' )