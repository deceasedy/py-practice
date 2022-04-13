"""
Сэндвич с мороженым — это строка, образованная двумя одинаковыми концами и разной серединой. Например:

AABBBAA
3&&3
yyyyymmmmmmmmyyyyy
hhhhhhhhmhhhhhhhh

Обратите внимание, что левый и правый концы сэндвича идентичны как по длине, так и по повторяющимся символам. Середину составляет третий (отличный от первых двух) набор символов.

Следующее не является сэндвичем с мороженным:

BBBBB // вы не можете иметь только мороженное (без сэндвича)
AAACCCAA // вы не можете иметь неравные по длине окончания в сэндвиче
AACDCAA // вы не можете иметь начинку из разных символов
A // ваш сэндвич не может быть менее трех символов

Напишите программу, которая возвращает true, если строка, введенная пользователем, является сэндвичем с мороженым, и false — в противном случае.

Примеры:

isIcecreamSandwich ("CDC") ➞ true
isIcecreamSandwich ("AAABB") ➞ false
isIcecreamSandwich ("AA") ➞ false
"""

def isIcecreamSandwich(text):

    # Сэндвич не может быть менее трех символов.
    if len(text) < 3: 
        return False

    # Достигли ли мы центра?
    center = False
    ch = text[0]

    
    for i in range(int((len(text) / 2) + 1)):
        # Если первый символ сменился, значит мы достигли символов центра.
        if text[i] == ch:
            if center: return False
            center = True
            ch = text[i]

        # Символы должны быть симметрично равны с разных сторон.
        if text[i] != text[-i-1]: return False

    # Если цикл завершился, но центр не был достигнут, то строка нам не подходит.
    return center


def test():
    print(isIcecreamSandwich("CDC"), "== True")
    print(isIcecreamSandwich("AAABB"), "== False")
    print(isIcecreamSandwich("AA"), "== False")


test()
