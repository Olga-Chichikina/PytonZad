
from datetime import datetime  as dt

def log_info (act):
    action = ''
    if act == 1:
        action = 'record'
    if act == 2:
        action = 'read'    
    time = dt.now().strftime ("%d %B %Y (%A)")
    with open ('loger.txt', 'a', encoding = 'utf-8') as rec:
        rec.write(f"{action} \n {time}\n")
