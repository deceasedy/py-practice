"""
Есть 2 текстовых файла. В них нужно найти и удалить числа, которые дублируются. Первый файл .txt содержит список
всех простых чисел от 0 до 1000, а второй файл .txt содержит список всех «счастливых чисел» от 0 до 1000.
"""

with open("prime.txt", "r") as prime:
	primes = [int(i) for i in prime.read().splitlines()]

with open("happy.txt", "r") as happy:
    happies = [int(i) for i in happy.read().splitlines()]

print(set(primes + list(set(primes) - set(happies))))
