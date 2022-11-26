import logger as log
from func_csv_txt import read_txt_file

def find_surname():
    daty = read_txt_file()
    ls = daty.split(")")
    find = input('Введите фамилию: ')
    for elem in ls:
        if find in elem:
            print(elem)

def find_phone():
    daty = read_txt_file()
    ls = daty.split(")")
    find = input('Номер телефона: ')
    for elem in ls:
        if find in elem:
            print(elem)
 

def find_name():
    daty = read_txt_file()
    ls = daty.split(")")
    find = input('Введите Имя: ')
    for elem in ls:
        if find in elem:
            print(elem)
           
