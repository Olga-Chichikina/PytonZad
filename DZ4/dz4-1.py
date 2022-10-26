#Вычислить число пи c заданной точностью d
## Пример:- при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}

# вычисление числа пи методом ряд Лейбница

i = 1
number = 0
while i < 2000:
    number = number + 4 / i
    i = i + 2
    number = number - 4 / i
    i = i + 2
print(round(number, 3))








#from math import pi
#n = int (input( ' Введите точность числа пи = '))
#print ( round (pi, n ))


