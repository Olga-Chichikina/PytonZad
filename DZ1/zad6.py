#  Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

diap = [0,1]
flag = True
for x in diap:
    for y in diap:
        for z in diap:
            dn = not(x or y or z) 
            fn = not(x) and not(y) and not(z) 
            print(x,y,z , dn == fn)
            if dn != fn:
                flag = False
if flag:
    print('доказано')
else:
    print('это не так')
    

             