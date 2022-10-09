# 2.Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

n = int(input('Введите число: '))
simple_num = []


def is_simple(j):
    i = 2
    m = 0
    while (i < j):
        if(j % i == 0):
            m = m + 1
        i += 1
    
    if(m >= 1):
        return False
    else: 
        return True

for i in range(2, n):
    if(n % i == 0 and is_simple(i)):
        simple_num.append(i)

print(simple_num)