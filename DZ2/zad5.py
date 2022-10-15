#Реализуйте алгоритм перемешивания списка.

sp = [ 2,3,5,68,15]
ls = [ 16,19,20,6]
spis = sp + ls
print (spis)
n = len(spis)
print(n)
k = int (len(spis)) / 2
print(k)
i = 0
while i < k :
    temp = spis[i]
    spis[i] = spis[n-1]
    spis[n-1] = temp
    i = i + 1
    n = n - 1
print(spis)

