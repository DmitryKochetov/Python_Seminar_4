
# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача -
# сформировать файл, содержащий сумму многочленов.

# 4x^2+2x+5
# 6x^2+4x+8


with open('file_task5_1.txt', 'r') as f:
    line_1 = f.readline()
with open('file_task5_2.txt', 'r') as f:
    line_2 = f.readline()


line_1_splitted = []
line_2_splitted = []
result = ''

m = 0
for i in line_1:
    m = m + 1
    if i == 'x':
        line_1_splitted.append(line_1[m-2])
line_1_splitted.append(line_1[m-1])

m = 0
for i in line_2:
    m = m + 1
    if i == 'x':
        line_2_splitted.append(line_2[m-2])
line_2_splitted.append(line_2[m-1])

result1 = int(line_1_splitted[0]) + int(line_2_splitted[0])
result2 = int(line_1_splitted[1]) + int(line_2_splitted[1])
result3 = int(line_1_splitted[2]) + int(line_2_splitted[2])

result = str(result1) + 'x^2+' + str(result2) + 'x+' + str(result3)

print(result)

with open('file_task5_3.txt', 'w') as f:
    f.write(result)
f.close()