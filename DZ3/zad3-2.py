#Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

ls = [2,3,5,6]
# ls = [2,3,4,5,6]
ks = []
n = round(len(ls) / 2)
k = len(ls)
if len(ls) % 2 == 0:
    for i in range(n):
        ps = ls[i] * ls[-1-i]
        ks.append(ps)
else:
    for i in range(0 , n+1):
        ps = ls[i] * ls[-1-i]
        ks.append(ps)
        
print(ks)
