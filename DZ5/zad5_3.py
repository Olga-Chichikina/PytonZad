# Создайте программу для игры в ""Крестики-нолики"".
from random import randint
st = [[1,2,3], [4,5,6], [7,8,9]]

print ('                        ИГРА "Крестики-нолики"')

def vvod(arr, x , met):    # функция заполнения поля 
    if x == 1 :
        arr[0][0] = met
    elif x ==2:
        arr[0][1] = met
    elif x == 3:
        arr[0][2] = met
    elif x== 4:
        arr[1][0] = met
    elif x == 5:
        arr[1][1] = met
    elif x == 6:
        arr[1][2] = met
    elif x == 7:
        arr[2][0] = met
    elif x == 8:
        arr[2][1] = met
    elif x == 9:
        arr[2][2] = met
    return arr

def pecharr(arr):     # функция печати , pecharr(st)  вызов функции печати
    for elem in arr:
        print(*elem)

def f_prov(st, met, name):    # функция проверки полей после ввода
    for i in range(3):
        for j in range(3):
            if st[0][0]== st[0][1]==st[0][2] == met :
                print ('Игра закончена. Выиграл', name)
                return True
            elif st[1][0]== st[1][1]==st[1][2] == met :
                print ('Игра закончена. Выиграл', name)
                return True
            elif st[2][0]== st[2][1]==st[2][2] == met :
                print ('Игра закончена. Выиграл' , name)
                return True
            if st[0][0]== st[1][0]==st[2][0] == met :
                print ('Игра закончена. Выиграл', name)
                return True
            elif st[0][1]== st[1][1]==st[2][1] == met :
                print ('Игра закончена. Выиграл', name)
                return True
            elif st[0][2]== st[1][2]==st[2][2] == met :
                print ('Игра закончена. Выиграл' , name)
                return True
            elif st[0][0]== st[1][1]==st[2][2] == met :
                print ('Игра закончена. Выиграл', name)
                return True
            elif st[2][0]== st[1][1]==st[0][2] == met :
                print ('Игра закончена. Выиграл' , name)
                return True
    return 


n1 = input ('  Введите имя 1 игрока : ')
n2 = input ('  Введите имя 2 игрока : ')

def func():                    #  определение первого игрока
    return randint(0,1)
r = func()

if r == 0:
    name1 = n1
    name2 = n2
else:
    name1 = n2
    name2 = n1

print( ' .... Игровое поле ... ')
pecharr(st)

i = 0
while i < 10:
    print(name1)
    r1 = int(input(' где поставить  o , введите номер ячейки   '))
    pecharr(vvod(st, r1 , 'o'))
    if  f_prov(st, 'o', name1) == True:
        break

    print()
    print(name2)
    r2 = int(input(' где поставить  x , введите номер ячейки   '))
    pecharr(vvod(st, r2 , 'x'))
    if  f_prov(st, 'x', name2) == True:
        break
    print()
    i+=1
print(' Ничья, мирный исход ')








