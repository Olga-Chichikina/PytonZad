#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение 
#элементов на указанных позициях. Позиции хранятся в файле file.txt в
# одной строке одно число.

with open('1.txt','r') as file:
    ls = file.read()
    print(ls)

sp = []
i=1
for i in range(len(ls)):
    if ls[i] != '\n':
        sp.append(ls[i])
    else:
      i = i + 1
print(sp)

ms = []
for i in range (len(sp)):
    el = int(sp[i]) * int(sp[i])
    ms.append(el)
print(ms)



