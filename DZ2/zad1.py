#Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:  - 6.782 -> 23    - 0,56 -> 11
import re
n = input ( 'Введите вещественное число :' )
for ch in ['.','.','0','-']:
    if ch in n:
        n = n.replace( ch, '')
print ( n)
sum = 0
for i in range( len(n)):
    sum = sum + int(n[i])
print( sum)





    


        










