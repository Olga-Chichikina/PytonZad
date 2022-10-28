#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#Входные и выходные данные хранятся в отдельных текстовых файлах.

# чтение из файла 
with open('file1.txt', 'r') as data:
    st = data.readline()

print(' Строка из файла fil1.txt')
print(st)


# сжатие данных 
ls = []
n = len(st)
j = 1
i = 0
while i < (n-1):
    if st[i] == st[i+1]:
        j = j + 1
        h = str(j)
        i = i + 1
    else:
        h = str (j)
        a = h + st[i] 
        i = i + 1
        j = 1
        ls.append(a)
b = str(j)
a1 = b + st[-1] 
ls.append(a1)
stro = ''.join(ls)
print(stro)

with open('file2.txt', 'w') as f:   f.write(stro)  # запись сжатых данных в файл

# распаковка данных
num = 0
nov_str =[] 
for i in range(len(stro)):
    if stro[i].isdigit():
        elem = int(stro[i])
    else:
        nov_str.append(stro[i] * elem)  
nov_str1 = ''.join(nov_str)
print(nov_str1)      

