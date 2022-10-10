#  Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

def LogSum(list):
    sum=0
    for i in range(len(list)):
        sum= sum + list[i]
    if sum == 0:     #  инверсия .....
        sum = 1
    else:
        sum = 0
    return sum

def LogProiz(list):
    proiz=1
    for i in range(len(list)): #  логическое умножение
        if list[i] == 0:    # инверсия
            list[i] = 1
        else:
            list[i] = 0
        proiz= proiz*list[i]
    return proiz

print('проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ') 
print('левая часть = правая часть ')
res=[0,0,0]  
left=LogSum(res)
right=LogProiz(res) 
print ('   ', left , '           ',  right )
res=[0,1,0] 
left=LogSum(res)
right=LogProiz(res) 
print ('   ', left , '           ',  right )
res=[0,0,1] 
left=LogSum(res)
right=LogProiz(res) 
print ('   ', left , '           ',  right )
res=[0,1,1] 
left=LogSum(res)
right=LogProiz(res) 
print ('   ', left , '           ',  right )
res=[1,0,0] 
left=LogSum(res)
right=LogProiz(res) 
print ('   ', left , '           ',  right )
res=[1,1,0] 
left=LogSum(res)
right=LogProiz(res) 
print ('   ', left , '           ',  right )
res=[1,0,1] 
left=LogSum(res)
right=LogProiz(res) 
print ('   ', left , '           ',  right )
res=[1,1,1] 
left=LogSum(res)
right=LogProiz(res) 
print ('   ', left , '           ',  right )

