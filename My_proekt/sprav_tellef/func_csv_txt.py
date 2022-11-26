import os.path
import csv
from logger import log_info

def write_csv_txt_file():
    if not os.path.exists('data.csv'):
        with open ('data.csv', 'w', encoding='utf-8') as dt: 
            st = csv.writer(dt, delimiter = ";")
            st.writerow(('surname','name', 'phone','info'))
    res = ''
    if  res != 'q':
        data_user = [
            (input('Введите фамилию '), input('Введите имя  '), input('Введите номер телефона   '), input('Введите информацию  '))
        ]
        with open ('data.csv', 'a', encoding = 'utf-8') as dt:
            st = csv.writer(dt, delimiter = ";")
            st.writerow(data_user)
            log_info(1)
        file = 'data.txt'
        with open (file, 'a', encoding = 'utf-8') as dt1:
            dt1.write(f'{data_user}\n')
        
def read_txt_file():
    with open ('data.txt', 'r', encoding = 'utf-8') as f:
            data = f.read()
            return data

def read_csv_file():
    with open('data.csv', encoding='utf-8') as f:
        data = []
        st = f.readlines()
        for i in st:
            st_in = i.split(';')
            tpl = tuple(j.strip() for j in st_in)
            data.append(tpl)
            return data

