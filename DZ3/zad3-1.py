#Задайте список из нескольких чисел. Напишите программу, 
#которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

ls = [2,3,5,9,3]
i = 1
r = len(ls)
s = 0
for i in range(r):
    if i % 2 != 0:
        s = s + ls[i]
        
print('Сумма элементов списка на нечетных позициях = ' + str(s))