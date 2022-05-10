"""
Целочисленный массив заполняется девятью рандомными элементами. 
Поменяйте местами максимальный и минимальный элементы массива.
"""

import random

array = [random.randint(0, 100) for i in range(9)]
index_of_max = array.index(max(array))
index_of_min = array.index(min(array))
maxn = array[index_of_max]
print(array)
array[index_of_max] = array[index_of_min]
array[index_of_min] = maxn
print(array)
