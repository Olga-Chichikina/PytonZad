# Напишите программу, которая принимает на вход цифру,
#  обозначающую день недели, и проверяет, является ли этот день выходным.

a = int(input('Введите день недели и мы подскажем выходной в этот день или нет  :  '))
if a == 0 or a>7:
    print('День недели от 1 до 7 - введите правильно ')
else:
    if a<6:
        print('            Сегодня рабочий день             ')
    else:
        print('            Это выходной день                ')
