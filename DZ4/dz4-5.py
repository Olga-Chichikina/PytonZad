#Даны два файла, в каждом из которых находится запись 
#многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('3.txt','r') as file:
    ls1 = file.read()
    print(ls1)

with open('4.txt','r') as file:
    ls2 = file.read()
    print(ls2)

ls1 = ls1[: -3]
print(ls1)
ls2 = ls2[: -3] 
print(ls2)

ls1 = ls1.replace('x' , '-')
ls1 = ls1.replace('^', '-')
ls1 = ls1.replace('+','-')
ls2 = ls2.replace('x' , '-')
ls2 = ls2.replace('^', '-')
ls2 = ls2.replace('+','-')

res1 =ls1.split('-')
del res1[2]
print(res1)
res2 =ls2.split('-')
del res2[2]
print(res2)

kof = []
for i in range(len(res1)):
    if res1[i] == '' and res2[i] == '':
        continue
    kof.append(int(res1[i])+int(res2[i]))

print(kof)
k = 2       #  степень многочлена 2
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

with open ('5.txt', 'w') as f: f.write(st)

