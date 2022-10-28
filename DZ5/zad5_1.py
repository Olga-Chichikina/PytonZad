#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

#1 вариант
st = 'gggg nhuuyti  сабвссс  роллпд  абв'
st = st.split()
print( 'Исходный текст                              ' , st)
find = 'абв'
st1 =[]
[st1.append(elem) for elem in st if find not in elem]
print('Текст без слов , содержащих "абв           "' , st1)
print()

#2 вариант
st = 'gggg nhuuyti  сабвссс  роллпд  абв'
st = st.split()
print( 'Исходный текст                              ' , st)
find = 'абв'
st1 =[]
for elem in st:
    if find in elem:
        continue
    st1.append(elem)
print('Текст без слов , содержащих "абв           "' , st1)


