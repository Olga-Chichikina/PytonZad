#Задача: предложить улучшения кода для уже решённых задач:
#с помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

#Напишите программу, которая принимает на вход число N и выдает набор
#  произведений чисел от 1 до N.  Пример:
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# from math import factorial
# n = int( input(' введите целое число  '))
# f = lambda x: ((x == 1) and 1) or x * factorial(x -1)
# sp = list( f(i) for i in range(1, n +1))
# print(sp)

#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# n = int(input( ' введите целое число '))
# ls =list(round(((1 + i / n ) ** n), 0) for i in range (1, n+1))
# res = list(map(lambda x: x+x, ls))
# for x,y in enumerate(res, start=1):
#     print(f'{x}:{y}')


#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:- для k = 8 
# def fib(n):
#     if n == 1:
#         return 1
#     if n == 0:
#         return 0
#     else:
#         return fib(n-1) + fib(n-2)
# ls = list( fib(i) for i in range(10))
# print(ls)

#Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

#ls1 = list(map(int, input("Введите числа через пробел:\n").split()))
#print( ls1)
#ls2 = []
#[ls2.append(i) for i in ls1 if i not in ls2]
#print(f"Список из неповторяющихся элементов: " + str(ls2))

