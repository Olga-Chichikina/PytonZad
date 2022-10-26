#Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
#Пример:- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('Введите степень многочлена = '))
kof = [randint(-10, 10) for i in range (k+1)]
print (kof)
st = ''
for i in range(len(kof)):
        if len(kof) > 0 and kof[i] > 0:
                st = st + ' + '
        if kof[i] == 0:
                continue
        st = st + str(kof[i]) + 'x^'+str(k-i) 
if kof != 0:
        st = st[:len(st) - 3]
st = st + '=0'
print (st)

with open ('2.txt', 'w') as f: f.write(st)
