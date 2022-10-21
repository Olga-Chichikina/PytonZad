#Задайте список из вещественных чисел. Напишите программу,
#которая найдёт разницу между максимальным и минимальным значением 
#дробной части элементов.
#Пример:- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

ls = [1.1, 1.2, 3.1, 5, 10.01]
print(' исходный список' + str(ls))
ks = []
for i in range(len(ls)):
    elem =round((ls[i] - int(ls[i])) , 2)
    ks.append(elem)
print(ks)
maxim = ks[0]
minim = ks[0]
for i in range(len(ks)):
    if ks[i] > maxim:
        maxim = ks[i]
        print(maxim)
    if ks[i] < minim and ks[i] != 0 : 
        minim = ks[i]
        print(minim)
print(' разницу между максимальным и минимальным значением дробной части элементов= ')
print (maxim - minim)


