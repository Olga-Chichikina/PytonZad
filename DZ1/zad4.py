#Напишите программу, которая по заданному номеру четверти,
#показывает диапазон возможных координат точек в этой четверти (x и y).

a =int(input('Введите номер четверти ( от 1 до 4 ) '))
if  a == 1:
    input( ' Диапозон координет точек в этой четверти  x> 0  , y > 0')
elif a == 2:
    input( ' Диапозон координет точек в этой четверти  x < 0  , y > 0')
elif a == 3:
    input( ' Диапозон координет точек в этой четверти  x < 0  , y < 0')
elif a == 4:
    input( ' Диапозон координет точек в этой четверти  x > 0  , y < 0')
else:
    input( ' Введите правильно номер четверти  от 1 до 4 ')

