# 4.Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

koef = []
stroka = ''

for i in range(101):
    koef.append(random.randint(0, 100))

k = int(input('Введите число: '))

for i in range(k, 1, -1):
    stroka = stroka + str(koef[i]) + ' ' + 'x ^ ' + str(i) + ' + '
stroka = stroka + str(koef[i+1]) + 'x ' str(koef[i+2])

with open('file_task4.txt', 'w') as f:
    f.write(stroka)
f.close()
