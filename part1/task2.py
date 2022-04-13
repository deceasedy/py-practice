"""
Напишите программу, которая определяет минимальное число в последовательности положительных чисел, которую ввел пользователь.
Если в последовательности есть отрицательные числа, то вы должны сообщить об этом пользователю и предложить повторить ввод еще раз.
"""

# Цикл будет активен до тех пор, пока пользователь не введет правильную длину.
while True:
    try:
        num = int(input("Введите длину последовательности: "))
        if num > 0:
            break
    except:
        continue

list = []
i = 0
tmp = 0

# Каждое введенное число должно быть положительным.
while i < num:
    tmp = int(input(str(i + 1) + " число: "))
    if tmp > 0:
        list.append(tmp)
        i += 1

print("Минимальное число с последовательности", list, ":", min(list))