#  Напишите программу, которая принимает на вход координаты точки (X и Y), и выдаёт номер
#  четверти плоскости,#  в которой находится эта точка (или на какой оси она находится).

x = int(input('Введите координату точки Х ='))
y = int(input('Введите координату точки Y ='))
if x > 0 and y > 0:
    print('        точка с координатами ',(x,y),' в 1 четверти плоскости')
elif x < 0 and y > 0:
     print('       точка с координатами ',(x,y),' в 2 четверти плоскости')
elif x < 0 and y < 0: 
     print('       точка с координатами ',(x,y),' в 3 четверти плоскости')
else:
     print('       точка с координатами ',(x,y),' в 4 четверти плоскости')


