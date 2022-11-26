import sys
from model import find_surname, find_phone,find_name
from func_csv_txt import write_csv_txt_file , read_txt_file
from logger import log_info

def button_click():
    print ('\nДОБРО ПОЖАЛОВАТЬ В ТЕЛЕФОННУЮ КНИГУ')
    m = -1  
    while m != 0:
        print ('\nПожалуйста, выберите один из следующих пунктов:')  
        print('1. Добавить новый контакт')  
        print('2. Показать контакты')  
        print('3. Поиск по фамилии')
        print('4. Поиск по номеру телефона')
        print('5. Поиск по имени')
        print('0. Выйти из телефонной книги')
        m = int(input('Ваш выбор: '))  
        if m == 1:  
            write_csv_txt_file()
            print('Новый контакт добавлен в книгу')
            continue
        elif m == 2: 
            daty = read_txt_file()
            log_info(2)
            ls = daty.split(")")
            for elem in ls:
                print(*elem)
            continue
        elif m == 3:  
            find_surname()
            continue
        elif m == 4:
            find_phone()
            continue
        elif m == 5:
            find_name()
        elif m == 0:  
            print('Программа завершена.\n')
            sys.exit(0)  
        else:  
            print('Пожалуйста следуйте инструкции')
